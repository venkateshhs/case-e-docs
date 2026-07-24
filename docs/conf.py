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

html_theme = "sphinx_rtd_theme"
html_title = "case-e documentation"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/case-e-logo.png"
html_logo = "_static/case-e-logo.png"
html_theme_options = {
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}
html_context = {
    "display_github": True,
    "github_user": "venkateshhs",
    "github_repo": "case-e-docs",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

copybutton_prompt_text = r"\$ |>>> |\.\.\. "
copybutton_prompt_is_regexp = True
autosectionlabel_prefix_document = True
todo_include_todos = False

extlinks = {
    "repo": ("https://github.com/venkateshhs/eCRF/%s", "%s"),
}
