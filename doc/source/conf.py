# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "SPIReS"
copyright = "2026, Niklas Griessbaum"
author = "Niklas Griessbaum"

# Version from the installed `spires` dist (setuptools_scm at build time);
# fall back to reading git tags directly in a source checkout.
try:
    from importlib.metadata import version

    release = version("spires")
except Exception:
    try:
        from setuptools_scm import get_version

        release = get_version(root="../..", relative_to=__file__)
    except Exception:
        release = "unknown"

version = release

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",            # MyST markdown
    "sphinx.ext.intersphinx",  # cross-link to each package's own hosted docs
    "sphinx_markdown_tables",
]

templates_path = ["_templates"]
exclude_patterns = []

# Umbrella docs link OUT to each package's own hosted API reference. intersphinx
# resolves cross-references for packages that publish an objects.inv; packages
# without hosted docs yet are reached via plain links (see packages.md).
intersphinx_mapping = {
    "spires_contract":    ("https://spires-contract.readthedocs.io/en/latest/", None),
    "spires_inversion":   ("https://spires-inversion.readthedocs.io/en/latest/", None),
    "spires_io":          ("https://spires-io.readthedocs.io/en/latest/", None),
    "spires_lut":         ("https://spires-lut.readthedocs.io/en/latest/", None),
    "spires_r0":          ("https://spires-r0.readthedocs.io/en/latest/", None),
    "spires_postprocess": ("https://spires-postprocess.readthedocs.io/en/latest/", None),
    "spires_batch":       ("https://spires-batch.readthedocs.io/en/latest/", None),
}

# Don't fail the build when an intersphinx target is unreachable (e.g. a
# sub-package hasn't published docs yet).
suppress_warnings = ["myst.xref_missing"]

# -- HTML output -------------------------------------------------------------
# Match the rest of the family (spires-inversion uses pydata-sphinx-theme).

html_theme = "pydata_sphinx_theme"
