mutation:
	mutmut run --paths-to-mutate kanban_tools

.PHONY: clean install mutation tests

tests:
	pytest --verbose

clean:
	rm --force .mutmut-cache