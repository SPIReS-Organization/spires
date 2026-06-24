# Architecture

SPIReS is a pipeline of single-purpose packages joined by a shared data
contract. Each stage consumes and produces
[`spires-contract`](https://github.com/SPIReS-Organization/spires-contract)-validated
`xarray` data, so stages stay decoupled: any one can be developed, tested, and
swapped without importing another's internals.

## Dataflow

```
            ┌──────────────┐
   sensor   │  spires-io   │  load + reproject MODIS / Sentinel-2 / Landsat
   granule ─►              ├─────────────► surface reflectance (contract)
            └──────────────┘                       │
                                                    ▼
   ┌──────────────┐   ┌──────────────┐   ┌────────────────────┐
   │  spires-lut  │   │  spires-r0   │   │  spires-inversion   │
   │ reflectance  ├──►│ background   ├──►│  invert RT model    ├──► retrieval
   │ lookup table │   │ R₀           │   │  against the LUT    │    (fsca,
   └──────────────┘   └──────────────┘   └────────────────────┘     grain size,
                                                    │                LAP)
                                                    ▼
                                          ┌────────────────────┐
                                          │ spires-postprocess  │  cloud gap-fill,
                                          │                     ├─► tree masking /
                                          └────────────────────┘    inpainting
```

In short: **io → lut → r0 → inversion → postprocess**, with `spires-contract`
defining the `xarray` schema at every boundary.

## Two ways to run it

- **One unit of work** — the [`spires`](install.md) metapackage's convenience
  layer (`spires.invert`) wires the stages together for a single granule/cube,
  in-process.
- **Many units at scale** —
  [`spires-batch`](https://github.com/SPIReS-Organization/spires-batch) takes
  that same single-unit kernel and parallelizes it across stacks of granules
  and spacetime cubes (dask/slurm). It is opt-in (`pip install spires[batch]`)
  so heavy backends never land in a bare install.
