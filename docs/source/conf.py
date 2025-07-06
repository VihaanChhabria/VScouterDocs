# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'VScouter'
author = 'Vihaan Chhabria'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

myst_enable_extensions = [
    "html_admonition",
    "html_image",
    "attrs_inline",   # enables `{width=40%}` after images
    "attrs_block"     # enables block-level attributes (optional)
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    "navigation_depth": 4,
    "prev_next_buttons_location": "bottom",  # default is bottom
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_favicon = 'favicon.ico'