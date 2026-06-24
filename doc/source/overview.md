# Overview

**SPIReS** — SPectral Inversion of REflectance from Snow — retrieves snow
properties (fractional snow-covered area, grain size, and light-absorbing
particle concentration) from multispectral surface reflectance by inverting a
radiative-transfer model against a reflectance lookup table.

The implementation is split into a family of small, single-purpose packages.
Each one does one thing, and they communicate only through
[contract](https://github.com/SPIReS-Organization/spires-contract)-validated
`xarray` data — never by importing one another's internals. You install just
the pieces you need.

## The family

| Package                                                                          | Role                                              |
|----------------------------------------------------------------------------------|---------------------------------------------------|
| [spires-contract](https://github.com/SPIReS-Organization/spires-contract)        | Data-interface contracts (xarray schemas)         |
| [spires-inversion](https://github.com/SPIReS-Organization/spires-inversion)      | Core inversion engine (`import spires_inversion`) |
| [spires-io](https://github.com/SPIReS-Organization/spires-io)                    | MODIS/Sentinel-2/Landsat loaders, reprojection    |
| [spires-lut](https://github.com/SPIReS-Organization/spires-lut)                  | Reflectance lookup tables                         |
| [spires-r0](https://github.com/SPIReS-Organization/spires-r0)                    | Background (R₀) reflectance production            |
| [spires-postprocess](https://github.com/SPIReS-Organization/spires-postprocess)  | Cloud gap-fill, tree masking/inpainting           |
| [spires-batch](https://github.com/SPIReS-Organization/spires-batch)              | Scale-out batch processing (dask/slurm, opt-in)   |

The [`spires`](https://github.com/SPIReS-Organization/spires) metapackage ties
these together: it installs the family (see [Install](install.md)) and owns the
`spires` import name, providing a light convenience layer for running the
retrieval on a single unit of work.

See [Architecture](architecture.md) for how data flows through the packages,
and [Packages](packages.md) for where each one's own documentation lives.
