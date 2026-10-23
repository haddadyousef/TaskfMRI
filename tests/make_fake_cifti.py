"""Build a tiny fake dtseries + dlabel pair (random numbers, real CIFTI structure).
Safe to commit; contains no HCP data.

  python tests/make_fake_cifti.py out/fake   -> out/fake_dtseries.dtseries.nii, out/fake_atlas.dlabel.nii
"""
import os
import sys

import nibabel as nib
import numpy as np
from nibabel import cifti2 as ci


def make(prefix, n_vert=20, n_time=30, seed=0):
    rng = np.random.default_rng(seed)
    aff = np.eye(4)
    mask_a = np.zeros((4, 4, 4), bool); mask_a[:2, :2, :2] = True   # 8 voxels
    mask_b = np.zeros((4, 4, 4), bool); mask_b[2:, 2:, 2:] = True   # 8 voxels
    bm = (ci.BrainModelAxis.from_surface(np.arange(n_vert), n_vert, "CIFTI_STRUCTURE_CORTEX_LEFT")
          + ci.BrainModelAxis.from_surface(np.arange(n_vert), n_vert, "CIFTI_STRUCTURE_CORTEX_RIGHT")
          + ci.BrainModelAxis.from_mask(mask_a, "CIFTI_STRUCTURE_THALAMUS_LEFT", affine=aff)
          + ci.BrainModelAxis.from_mask(mask_b, "CIFTI_STRUCTURE_THALAMUS_RIGHT", affine=aff))
    n = len(bm)
    data = rng.normal(size=(n_time, n)).astype(np.float32)
    ts = ci.SeriesAxis(0, 0.72, n_time)
    os.makedirs(os.path.dirname(prefix) or ".", exist_ok=True)
    dt_path = prefix + "_dtseries.dtseries.nii"
    nib.save(ci.Cifti2Image(data, (ts, bm)), dt_path)

    # atlas: parcels 1-2 split left cortex, 3-4 right cortex, 5/6 the two thalami
    labels = np.zeros(n, np.int32)
    labels[:10] = 1; labels[10:20] = 2
    labels[20:30] = 3; labels[30:40] = 4
    labels[40:48] = 5; labels[48:56] = 6
    table = {0: ("???", (0, 0, 0, 0))}
    for i in range(1, 7):
        table[i] = (f"P{i}", (0.1 * i, 0.5, 0.5, 1.0))
    lab_axis = ci.LabelAxis(["atlas"], [table])
    dl_path = prefix + "_atlas.dlabel.nii"
    nib.save(ci.Cifti2Image(labels[None, :], (lab_axis, bm)), dl_path)
    return dt_path, dl_path, data, labels


if __name__ == "__main__":
    print(*make(sys.argv[1] if len(sys.argv) > 1 else "out/fake")[:2])
