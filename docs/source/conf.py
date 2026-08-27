# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_readable_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'fama website'
copyright = '2026, famatf'
author = 'famatf'
release = ''
html_title = 'fama website'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.katex',
    'sphinx.ext.githubpages',
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
]

katex_options = r'''{
    strict: false,
}'''

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'readable'
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_static_path = ['_static']

html_baseurl = 'https://famatf.com/'
html_favicon = "_static/favicon.ico"

html_last_updated_fmt = "%Y-%m-%d %H:%M"
