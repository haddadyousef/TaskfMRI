# Decisions and open questions

## Atlas (OPEN - decide with Felix)
Cortex: Glasser HCP-MMP1.0, 360 parcels (keep unchanged).

Subcortex options:
| Option | Nodes | Notes |
|---|---|---|
| A. Glasser only | 360 | No deep structures |
| B. Glasser + CIFTI header structure groups | 379 | 19 subcortical groups from the file header (incl. brainstem, cerebellum, diencephalon); no download needed |
| B'. Glasser + 7 bilateral structures | 374 | thalamus, caudate, putamen, pallidum, hippocampus, amygdala, accumbens (14 parcels) |
| C. Glasser + Tian | varies | Needs atlas download |
| D. Cole-Anticevic (CAB-NP) | ~718 | Needs download; wSubcorGSR vs woSubcorGSR version to pick |

Chosen: _TBD_

## Distance for the graph (OPEN)
Cortex-cortex: geodesic on the surface mesh. Cortex-subcortex and subcortex-subcortex:
3D Euclidean as a proxy. Left/right hemisphere meshes are disconnected, so geodesic is
undefined across them. Record the metric used per edge type.

## Open questions
- Approval to download the extra atlas (Tian / Cole-Anticevic)?
- Which Cole-Anticevic version?
- Verify atlas column order matches the scan's columns before extracting.
- Which HCP subjects to include (977 with all 14 runs?).

## Split of work
- Atlas construction + QC: one person owns, delivers a versioned .dlabel.nii + parcel_lookup.csv
- Extraction + graph + GDAR integration: the other consumes those files
