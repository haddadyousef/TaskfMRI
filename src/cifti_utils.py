"""Helpers for reading CIFTI brain-model info and parcel labels."""
import nibabel as nib
import numpy as np


def structure_counts(img):
    """Return [(structure_name, n_grayordinates)] from a dtseries/dlabel image.

    The brain model axis is the one over grayordinates (the last axis).
    """
    bm = img.header.get_axis(img.ndim - 1)
    out = []
    for name, sl, _ in bm.iter_structures():
        stop = sl.stop if sl.stop is not None else bm.size
        out.append((name, stop - sl.start))
    return out


def load_labels(dlabel_path):
    """Load a .dlabel.nii. Returns (labels, names): labels is an int array of length
    n_grayordinates (0 = unlabeled), names maps label id -> name."""
    img = nib.load(dlabel_path)
    labels = np.asarray(img.get_fdata()).reshape(-1).astype(int)
    table = img.header.get_axis(0).label[0]
    names = {k: v[0] for k, v in table.items()}
    return labels, names
