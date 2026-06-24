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
pip install spires[batch]       # + spires-batch     (scale-out: dask/slurm)
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
| [spires-batch](https://github.com/SPIReS-Organization/spires-batch)           | Scale-out batch processing (dask/slurm, opt-in)   |

Each package communicates with the others only through contract-validated
`xarray` data — never by importing another package's internals.

## Convenience layer

Beyond aggregating installs, `spires` owns the `spires` **import name** and
provides a *light* convenience layer: the unified API that wires
io → lut → r0 → inversion → postprocess for **one** unit of work, plus a CLI
that runs that on a single granule/file.

```python
import spires
result = spires.invert(granule)   # one unit, in-process
```

The line is deliberate, to keep `pip install spires` light:

- **In the metapackage:** the retrieval, wired together, for *one* unit —
  pure orchestration of already-installed sub-packages, no new heavy deps.
- **Not here:** anything that knows about *many* units, schedulers, clusters,
  chunking, or job submission. That is
  [`spires-batch`](https://github.com/SPIReS-Organization/spires-batch),
  which builds on `spires.invert` and is surfaced as the `spires[batch]`
  extra. Heavy backends (dask, slurm) never land in a bare `pip install
  spires`.

## Documentation

The family uses a **landing-site + link-out** model. This metapackage hosts
the umbrella docs — the family's front door: what SPIReS is, the family table,
the install matrix, and an architecture/dataflow overview
(io → lut → r0 → inversion → postprocess). Each sub-package keeps its **own**
hosted API reference; the umbrella links out to them (via Sphinx
`intersphinx`, so cross-references resolve). Meta owns the *map*; each repo
owns its *content*. No unified single-build site that absorbs every
sub-package's API docs — that would re-couple what the architecture keeps
decoupled.

## Open questions (this is a stub — discussion welcome)

The convenience layer and docs site are not built yet. Points still open:

- **`spires.invert` signature.** What is "one unit"? A granule path, a loaded
  contract-validated `xarray`, a sensor + scene id? What does it return?
- **CLI shape.** `spires run config.yaml`? Does it share a CLI surface with
  `spires-batch`, or does batch ship its own? (Mirrored in the spires-batch
  README.)
- **Config / recipes.** Do we want presets for common sensor/region combos
  baked into the convenience layer, or is that out of scope (YAGNI for now)?
- **Import-name ownership.** Settled: the metapackage owns `spires`. Batch is
  a separate dist (`spires-batch`, module `spires_batch`) so its name honestly
  describes its job and stays out of every `spires` install.

> **Status:** scaffolding. The metapackage now owns the `spires` import name
> and ships a stub convenience layer (`spires.invert` raises
> `NotImplementedError`); the real wiring is the next step. Versions are
> unpinned placeholders; pin to released versions once the packages publish to
> PyPI.
