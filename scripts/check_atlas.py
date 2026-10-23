"""QC for a combined dlabel atlas against one scan.

  python scripts/check_atlas.py --dlabel atlas/X.dlabel.nii --dtseries scan.dtseries.nii
Checks: grayordinate count matches the scan, 360 cortical parcels (ids 1-360) present,
no empty parcels, every label in the table is used.
"""
import argparse
import os
import sys

import nibabel as nib
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.cifti_utils import load_labels  # noqa: E402


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dlabel", required=True)
    p.add_argument("--dtseries", required=True)
    p.add_argument("--n-cortical", type=int, default=360)
    a = p.parse_args()

    labels, names = load_labels(a.dlabel)
    scan_n = nib.load(a.dtseries).shape[1]
    ok = True

    def check(cond, msg):
        nonlocal ok
        print(("PASS  " if cond else "FAIL  ") + msg)
        ok = ok and cond

    check(labels.size == scan_n, f"grayordinate count atlas={labels.size} scan={scan_n}")
    used = set(labels.tolist()) - {0}
    cortical = set(range(1, a.n_cortical + 1))
    check(cortical <= used, f"all {a.n_cortical} cortical parcels (ids 1-{a.n_cortical}) used")
    unused = set(names) - used - {0}
    check(not unused, f"no label-table entries without grayordinates (unused: {sorted(unused)})")
    sizes = {i: int((labels == i).sum()) for i in used}
    print(f"parcels: {len(used)}, smallest has {min(sizes.values())} grayordinates")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
