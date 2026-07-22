# case-e documentation

Standalone documentation for [case-e](https://github.com/venkateshhs/eCRF),
built with Sphinx and the Furo theme. The repository supports both local viewing
and automatic GitHub Pages hosting.

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

## Publish on GitHub Pages

1. Create a public GitHub repository named `case-e-docs` and push this directory
   to its `main` branch.
2. Open **Settings → Pages** in that repository.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Open the **Actions** tab and wait for **Deploy documentation to GitHub
   Pages** to complete.

The project site will be:

<https://venkateshhs.github.io/case-e-docs/>

If the repository is instead named `venkateshhs.github.io`, GitHub serves it at
the account root: <https://venkateshhs.github.io/>.

## Optional Read the Docs mirror

The included `.readthedocs.yaml` also supports a Read the Docs project. Import
the GitHub repository in Read the Docs and the service will build `docs/conf.py`
with the pinned dependencies in `requirements.txt`.

## Edit content

Pages are reStructuredText files in `docs/`. Add new pages to a `toctree` in
`docs/index.rst`. Theme colors and components are in
`docs/_static/custom.css`; Sphinx settings are in `docs/conf.py`.
