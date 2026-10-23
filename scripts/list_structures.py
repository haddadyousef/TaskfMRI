"""Print how many grayordinates each structure has in one HCP task dtseries.

Extracts just that one file from the subject zip into a scratch folder, reads the header,
then deletes the extracted file. Nothing is hardcoded; pass paths as arguments.

Example:
  python scripts/list_structures.py --zip R:/.../100206_3T_tfMRI_MOTOR_preproc.zip \
      --subject 100206 --task MOTOR --phase LR --scratch ~/scratch
"""
import argparse
import os
import sys
import zipfile

import nibabel as nib

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.cifti_utils import structure_counts  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--zip", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--task", required=True, help="e.g. MOTOR")
    p.add_argument("--phase", required=True, choices=["LR", "RL"])
    p.add_argument("--scratch", default=os.path.expanduser("~/scratch"))
    a = p.parse_args()

    run = f"tfMRI_{a.task}_{a.phase}"
    inner = (f"{a.subject}/MNINonLinear/Results/{run}/"
             f"{run}_Atlas_MSMAll_hp0_clean_rclean_tclean.dtseries.nii")
    os.makedirs(a.scratch, exist_ok=True)
    with zipfile.ZipFile(a.zip) as z:
        if inner not in z.namelist():
            print("Not found in zip. dtseries files present:")
            print("\n".join(n for n in z.namelist() if n.endswith(".dtseries.nii")))
            sys.exit(1)
        path = z.extract(inner, a.scratch)
    try:
        img = nib.load(path)
        print("shape (time, grayordinates):", img.shape)
        total = 0
        for name, n in structure_counts(img):
            print(f"{name:45s} {n}")
            total += n
        print("total:", total)
    finally:
        os.remove(path)


if __name__ == "__main__":
    main()
