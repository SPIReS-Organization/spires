# Install

Installing the [`spires`](https://github.com/SPIReS-Organization/spires)
metapackage pulls in the family so you don't install each piece by hand. The
default install is lightweight; functional add-ons are opt-in extras.

```bash
pip install spires              # core: spires-contract + spires-inversion
pip install spires[io]          # + spires-io          (data loaders, reprojection)
pip install spires[lut]         # + spires-lut         (reflectance lookup tables)
pip install spires[r0]          # + spires-r0          (background reflectance)
pip install spires[postprocess] # + spires-postprocess (cloud gap-fill, tree inpainting)
pip install spires[batch]       # + spires-batch       (scale-out: dask/slurm)
pip install spires[all]         # everything
```

## What you get

- **`pip install spires`** installs the core and gives you the `spires` import
  name with the light convenience layer (`import spires; spires.invert(...)`).
- **Extras** add the functional sub-packages you need. They are additive — for
  example `pip install spires[io,lut,r0]`.
- **`spires[batch]`** adds scale-out batch processing. The heavy execution
  backends (dask, slurm) live behind `spires-batch`'s own extras and stay out
  of a bare `spires` install.

```{note}
The family is pre-release scaffolding. Version floors in the metapackage are
unpinned placeholders; they will be pinned to released versions once the
packages publish to PyPI.
```
