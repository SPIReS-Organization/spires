# spires

Metapackage for [SPIReS](https://github.com/SPIReS-Organization) — SPectral
Inversion of REflectance from Snow. Installing `spires` pulls in the SPIReS
package family so you don't have to install each piece by hand.

## Install

```bash
pip install spires              # core: spires-contract + spires-inversion
pip install spires[io]          # + spires-io        (data loaders, reprojection)
pip install spires[lut]         # + spires-lut       (reflectance lookup tables)
pip install spires[r0]          # + spires-r0        (background reflectance)
pip install spires[postprocess] # + spires-postprocess (cloud gap-fill, tree inpainting)
pip install spires[all]         # everything
```

## The family

| Package                                                                       | Role                                              |
|-------------------------------------------------------------------------------|---------------------------------------------------|
| [spires-contract](https://github.com/SPIReS-Organization/spires-contract)     | Data-interface contracts (xarray schemas)         |
| [spires-inversion](https://github.com/SPIReS-Organization/spires-inversion)   | Core inversion engine (`import spires_inversion`) |
| [spires-io](https://github.com/SPIReS-Organization/spires-io)                 | MODIS/Sentinel-2/Landsat loaders, reprojection    |
| [spires-lut](https://github.com/SPIReS-Organization/spires-lut)               | Reflectance lookup tables                         |
| [spires-r0](https://github.com/SPIReS-Organization/spires-r0)                 | Background (R_0) reflectance production            |
| [spires-postprocess](https://github.com/SPIReS-Organization/spires-postprocess) | Cloud gap-fill, tree masking/inpainting         |

Each package communicates with the others only through contract-validated
`xarray` data — never by importing another package's internals.

This metapackage ships **no importable module of its own**; the import name
`spires` is intentionally left free. The inversion engine imports as
`spires_inversion`.

> **Status:** scaffolding. Versions are unpinned placeholders; pin to released
> versions once the packages publish to PyPI.
