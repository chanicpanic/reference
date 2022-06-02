# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sphinx_material

 # Register the theme as an extension to generate a sitemap.xml

import os
import sys
sys.path.append(os.path.abspath('./_ext'))


# -- Project information -----------------------------------------------------

project = 'Chanic Panic™'
copyright = '2022'
author = 'chanicpanic'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "chanicpanic"
]
extensions.append('sphinx_material')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Get the them path
html_theme_path = sphinx_material.html_theme_path()
# Register the required helpers for the html context
html_context = sphinx_material.get_html_context()

html_theme_options = {
    "color_primary": "deep-purple",
    "color_accent": "cyan",
    "repo_url": "https://github.com/chanicpanic/reference",
    "repo_name": "Edit on Github",
    "repo_type": "github",
    "master_doc": False,
    "nav_links": [
        {
            "href": "instructions",
            "title": "How to Play",
            "internal": True,
        },
        # {
            # "href": "groups",
            # "title": "Playing in Groups",
            # "internal": True,
        # },
        {
            "href": "abilities",
            "title": "Abilities",
            "internal": True,
        },
        {
            "href": "stack",
            "title": "The Stack",
            "internal": True,
        },
        {
            "href": "presence",
            "title": "Presence",
            "internal": True,
        },
        {
            "href": "ability_reference",
            "title": "Ability Reference",
            "internal": True,
        },
        {
            "href": "by_number",
            "title": "Chanic Panic by Number",
            "internal": True,
        },
        {
            "href": "glossary",
            "title": "Glossary",
            "internal": True,
        },
        {
            "href": "resources",
            "title": "Resources",
            "internal": True,
        },
    ]
}

html_title = 'Chanic Panic™'

html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"

html_copy_source = False

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTex output ------------------------------------------------

latex_engine = "xelatex"

latex_documents = [("instructions", "instructions.pdf", "" , "Nicholas Chan",
                    "manual", False)]

# latex_use_xindy = False
