from __future__ import annotations

from datetime import date

project = "case-e"
author = "case-e contributors"
copyright = f"{date.today().year}, {author}"
release = "1.0"

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"
master_doc = "index"
language = "en"

html_theme = "furo"
html_title = "case-e documentation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/case-e-logo.png"
html_logo = "_static/case-e-logo.png"
html_theme_options = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "color-brand-primary": "#087f72",
        "color-brand-content": "#087f72",
        "color-admonition-background": "#edf8f5",
    },
    "dark_css_variables": {
        "color-brand-primary": "#67dfca",
        "color-brand-content": "#67dfca",
    },
    "source_repository": "https://github.com/venkateshhs/case-e-docs/",
    "source_branch": "main",
    "source_directory": "docs/",
}

copybutton_prompt_text = r"\$ |>>> |\.\.\. "
copybutton_prompt_is_regexp = True
autosectionlabel_prefix_document = True
todo_include_todos = False

extlinks = {
    "repo": ("https://github.com/venkateshhs/eCRF/%s", "%s"),
}
