# Data notes

Facts only. Add a source or date when you add a line.

## Subjects (from Aya's dataset doc)
- 1,206 subjects total
- 1,067 have task zips
- 977 have all 14 task runs
- 889 have all modalities (HCP)

## Task runs
- 7 tasks x 2 phase-encoding directions (LR, RL) = 14 runs per subject
- TR = 0.72 s
- MOTOR: 284 frames per run
- Events: EV files (onset, duration, amplitude); timing in `Sync.txt`
- BOLD lags neural activity by roughly 5 s
- LR and RL runs have different phase-encoding distortion, so check both

## CIFTI file (seen for subject 100206, MOTOR LR)
Path inside the zip:
`100206/MNINonLinear/Results/tfMRI_MOTOR_LR/tfMRI_MOTOR_LR_Atlas_MSMAll_hp0_clean_rclean_tclean.dtseries.nii`

Pattern assumed for other tasks (not yet checked on all 14 runs):
`<subject>/MNINonLinear/Results/tfMRI_<TASK>_<LR|RL>/tfMRI_<TASK>_<LR|RL>_Atlas_MSMAll_hp0_clean_rclean_tclean.dtseries.nii`

- 91,282 grayordinates = 59,412 cortical vertices + 31,870 subcortical voxels
- The header (brain model axis) gives, per column, the structure and the vertex index
  (cortex) or voxel (i, j, k) (subcortex). It does NOT give parcel names; those come from
  an atlas (.dlabel.nii).
- Cortical surface: fs_LR 32k mesh.

## Not verified yet
- Whether the task zips contain any .dlabel file (none seen)
- Filenames/suffix for the other 13 runs and other subjects
