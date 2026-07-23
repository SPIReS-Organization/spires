# Packages

This umbrella site is the *portal*; each package is a **subproject** with its
own hosted documentation, reachable under `spires.readthedocs.io/projects/…`
and cross-linked via `intersphinx`. Each package builds independently — a
release in one repo rebuilds only that subproject.

## spires-contract
Data-interface contracts — the `xarray` schemas every package validates against
at its boundaries.
[Repository](https://github.com/SPIReS-Organization/spires-contract) ·
[Docs](https://spires-contract.readthedocs.io/)

## spires-inversion
The core inversion engine (`import spires_inversion`): inverts the
radiative-transfer model against the reflectance LUT to retrieve snow
properties.
[Repository](https://github.com/SPIReS-Organization/spires-inversion) ·
[Docs](https://spires-inversion.readthedocs.io/)

## spires-io
Data loaders and reprojection for MODIS, Sentinel-2, and Landsat.
[Repository](https://github.com/SPIReS-Organization/spires-io) ·
[Docs](https://spires-io.readthedocs.io/)

## spires-lut
Reflectance lookup tables: create, read, and write the Mie-scattering LUTs the
inversion interpolates.
[Repository](https://github.com/SPIReS-Organization/spires-lut) ·
[Docs](https://spires-lut.readthedocs.io/)

## spires-r0
Background (R₀) reflectance production.
[Repository](https://github.com/SPIReS-Organization/spires-r0) ·
[Docs](https://spires-r0.readthedocs.io/)

## spires-postprocess
Cloud gap-fill and tree masking/inpainting of retrieval output.
[Repository](https://github.com/SPIReS-Organization/spires-postprocess) ·
[Docs](https://spires-postprocess.readthedocs.io/)

## spires-batch
Scale-out batch processing: run the retrieval over stacks of granules and
spacetime cubes (dask/slurm), opt-in via `spires[batch]`.
[Repository](https://github.com/SPIReS-Organization/spires-batch) ·
[Docs](https://spires-batch.readthedocs.io/)

```{note}
Each package is a subproject of the parent `spires` Read the Docs project,
sharing one search index and the `spires.readthedocs.io` namespace while
building independently. The scaffold packages (`spires-lut`, `spires-r0`,
`spires-batch`) currently host narrative placeholder pages that grow an API
reference as their code lands.
```
