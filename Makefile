.PHONY: html clean serve

html:
	sphinx-build --fail-on-warning -b html docs docs/_build/html

clean:
	sphinx-build -M clean docs docs/_build

serve: html
	python3 -m http.server 8080 --directory docs/_build/html
