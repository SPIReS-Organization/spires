# Packages

This umbrella site owns the *map*; each package owns its own *documentation*.
Below is where to find each one. As packages publish hosted docs, the "Docs"
link moves from the repository to the package's own site (and is wired into
`intersphinx` in `conf.py` so cross-references resolve).

## spires-contract
Data-interface contracts — the `xarray` schemas every package validates against
at its boundaries.
[Repository](https://github.com/SPIReS-Organization/spires-contract)

## spires-inversion
The core inversion engine (`import spires_inversion`): inverts the
radiative-transfer model against the reflectance LUT to retrieve snow
properties.
[Repository](https://github.com/SPIReS-Organization/spires-inversion) ·
[Docs](https://spipy.readthedocs.io/)

## spires-io
Data loaders and reprojection for MODIS, Sentinel-2, and Landsat.
[Repository](https://github.com/SPIReS-Organization/spires-io)

## spires-lut
Reflectance lookup tables: create, read, and write the Mie-scattering LUTs the
inversion interpolates.
[Repository](https://github.com/SPIReS-Organization/spires-lut)

## spires-r0
Background (R₀) reflectance production.
[Repository](https://github.com/SPIReS-Organization/spires-r0)

## spires-postprocess
Cloud gap-fill and tree masking/inpainting of retrieval output.
[Repository](https://github.com/SPIReS-Organization/spires-postprocess)

## spires-batch
Scale-out batch processing: run the retrieval over stacks of granules and
spacetime cubes (dask/slurm), opt-in via `spires[batch]`.
[Repository](https://github.com/SPIReS-Organization/spires-batch)

```{note}
Only `spires-inversion` publishes hosted docs today. The other packages link to
their repositories until their own sites go live; commented-out `intersphinx`
entries in `conf.py` are ready to enable as they do.
```
