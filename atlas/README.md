# Atlas

- `parcel_lookup.csv`: parcel id -> name, hemisphere, cortical/subcortical.
  Rows 1-360 (Glasser cortex) still need to be added from the Glasser label table.
  Rows 361-374 are a PROPOSAL for the 14 subcortical parcels; IDs are not final.
- `Glasser360_Subcortex14.dlabel.nii` (not built yet): small enough to commit once it exists.
- Record here: atlas version, where each source file was downloaded from, date.
- Confirm with Felix before committing third-party atlas files; prefer committing a build
  script over the downloaded files.
