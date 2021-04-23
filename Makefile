all: mutants

.PHONY: all clean format install lint mutants tests

repo = kanban_tools
codecov_token = eb235d9d-86e8-4c08-a583-70d34f127ff1

clean:
	rm --force .mutmut-cache
	rm --recursive --force ${repo}.egg-info
	rm --recursive --force ${repo}/__pycache__
	rm --recursive --force tests/__pycache__

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests

format:
	black --line-length 100 ${repo}
	black --line-length 100 tests

install:
	pip install --editable .

lint:
	pylint ${repo}
	pylint tests

mutants:
	mutmut run --paths-to-mutate ${repo}

coverage: install
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

tests: install
	pytest --verbose
