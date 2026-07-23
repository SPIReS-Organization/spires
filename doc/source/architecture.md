# Architecture

SPIReS is a pipeline of single-purpose packages joined by a shared data
contract. Each stage consumes and produces
[`spires-contract`](https://github.com/SPIReS-Organization/spires-contract)-validated
`xarray` data, so stages stay decoupled: any one can be developed, tested, and
swapped without importing another's internals.

## Dataflow

The inversion has **three independent inputs** — surface reflectance (from
`spires-io`), the Mie-scattering lookup table (`spires-lut`), and the background
R₀ reflectance (`spires-r0`). These are not a linear chain: `spires-lut` and
`spires-r0` do not feed each other, and R₀ is built from a **stack of
reflectances** produced by `spires-io`, not from the LUT.

```
   spires-lut ──────────────────────────┐  (reflectance lookup table)
                                         │
                                         ▼
   spires-io ───────────────────► spires-inversion ──► spires-postprocess
   (surface reflectance) ─┐    ┌─►(invert the RT model    (cloud gap-fill,
        │                 │    │  against the LUT)         tree masking /
        │ stack of        │    │        │                  inpainting)
        │ reflectances    │    │ R₀     ▼
        ▼                 │    │   retrieval (fsca, grain size, LAP)
   spires-r0 ─────────────┘────┘
   (background R₀)
```

- **spires-io** produces surface reflectance, which is both the inversion
  *target* and the input `spires-r0` reads (as a reflectance stack).
- **spires-r0** derives the background R₀ and hands it to the inversion.
- **spires-lut** is an independent input: the reflectance LUT the inversion
  interpolates against.

In short: **io + lut + r0 → inversion → postprocess** — io and its derived R₀
plus the standalone LUT converge on the inversion — with `spires-contract`
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
