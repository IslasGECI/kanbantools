mutation:
	mutmut run --paths-to-mutate kanban_tools

.PHONY: clean install mutation tests

install:
	pip install --editable .

tests: install
	pytest --verbose

clean:
	rm --force .mutmut-cache