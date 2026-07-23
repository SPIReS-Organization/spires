"""spires: the SPIReS package family's front door and light convenience layer.

The distribution ``spires`` aggregates the package family (see the extras in
``pyproject.toml``) and owns the ``spires`` import name. Beyond aggregation it
provides a *light* convenience layer: the unified entry point that wires
io + lut + r0 -> inversion -> postprocess for **one** unit of work.

Anything that scales that across **many** units (stacks of granules,
spacetime cubes, dask/slurm) lives in ``spires-batch``, not here, so a bare
``pip install spires`` stays light.

Status: scaffolding. :func:`invert` is a stub; its signature and return type
are still open (see the README's "Open questions").
"""

try:  # version is derived from git tags via setuptools_scm at build time
    from importlib.metadata import version as _version

    __version__ = _version("spires")
except Exception:  # not installed (e.g. running from a source checkout)
    __version__ = "0+unknown"

__all__ = ["invert"]


def invert(granule):
    """Run the SPIReS retrieval for a single unit of work.

    Wires the family together (io + lut + r0 -> inversion -> postprocess) for
    one granule/cube, in-process. This is the light, single-unit kernel that
    ``spires-batch`` parallelizes across many units.

    Not implemented yet — the signature (what "one unit" is) and return type
    are still open design questions; see the README.
    """
    raise NotImplementedError(
        "spires.invert is not implemented yet. The convenience layer is "
        "scaffolding; see the spires README for the open design questions."
    )
