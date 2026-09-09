# case-e documentation

Standalone documentation for [case-e](https://github.com/venkateshhs/eCRF),
built with Sphinx and the Read the Docs theme. The repository supports both local viewing
and automatic Read the Docs hosting.

- **Published documentation:** <https://case-e.readthedocs.io/en/latest/>
- **Documentation author and maintainer:** [Venkatesh Hariharapura Shivashankar](https://github.com/venkateshhs)
- **Hosted case-e:** <https://ecrf.inm7.de/login>
- **Collaboration contact:** Prof. Jürgen Dukart, <j.dukart@fz-juelich.de>

## AI-generation disclosure

This documentation site was generated entirely by ChatGPT. This statement is
provided expressly for transparency and legal attribution. ChatGPT and OpenAI
are not the author, maintainer, publisher, operator, or legal guarantor of
case-e. The named human maintainer reviews, accepts, publishes, corrects, and
versions the documentation. See `docs/support.rst` for the complete legal
notice and limitations.

## Build locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make html
python3 -m http.server 8080 --directory docs/_build/html
```

Open <http://127.0.0.1:8080/>. Run `make clean html` after structural changes.
The same strict build runs in GitHub Actions, so warnings fail before deployment.

## Publish on Read the Docs

1. Push this repository to its `main` branch.
2. Import `case-e-docs` in Read the Docs.
3. Keep `.readthedocs.yaml` as the project configuration file.
4. Wait for the `latest` build to complete.

The canonical documentation site is:

<https://case-e.readthedocs.io/en/latest/>

Read the Docs builds `docs/conf.py` using the pinned dependencies in
`requirements.txt`.

## Edit content

Pages are reStructuredText files in `docs/`. Add new pages to a `toctree` in
`docs/index.rst`. Theme colors and components are in
`docs/_static/custom.css`; Sphinx settings are in `docs/conf.py`.

The generated footer credits
[Sphinx](https://www.sphinx-doc.org/), the
[Read the Docs theme](https://github.com/readthedocs/sphinx_rtd_theme), and
[Read the Docs](https://readthedocs.org/).
