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
io + lut + r0 → inversion → postprocess for **one** unit of work, plus a CLI
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

## Citation

To cite SPIReS as a whole, use the [`CITATION.cff`](CITATION.cff) in this
repository — GitHub's "Cite this repository" button renders BibTeX/APA from it.
It is the canonical, project-wide citation for the package family. Please also
cite the algorithm paper (Bair, Stillinger, & Dozier, 2021), which it references
as the preferred citation.

The [`spires-inversion`](https://github.com/SPIReS-Organization/spires-inversion)
engine additionally carries its own `CITATION.cff` and DOI for citing that
component specifically (e.g. its independent software release on Zenodo).

## Documentation

The family docs are a **unified Read the Docs portal built from subprojects**.
This metapackage is the parent `spires` RTD project — the family's front door:
what SPIReS is, the family table, the install matrix, and an
architecture/dataflow overview (io + lut + r0 → inversion → postprocess). Each
sub-package is a **subproject** with its own independently-built API reference,
served under the shared `spires.readthedocs.io` namespace
(`spires.readthedocs.io/projects/<pkg>/`) with one search index, and
cross-linked via Sphinx `intersphinx`. Meta owns the *map*; each repo owns its
*content* and its own build. This keeps a single reader-facing portal without a
single monolithic build — a release in one repo rebuilds only its subproject,
so the docs stay as decoupled as the architecture.

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
