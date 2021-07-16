all: check coverage mutants

.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		install \
		lint \
		mutants \
		tests

repo = kanban_tools
codecov_token = eb235d9d-86e8-4c08-a583-70d34f127ff1

define lint
	pylint \
        --disable=bad-continuation \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
        ${1}
endef

check:
	black --check --line-length 100 ${repo}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${repo}
	flake8 --max-line-length 100 tests

clean:
	rm --force --recursive .pytest_cache/
	rm --force --recursive ${repo}.egg-info
	rm --force --recursive ${repo}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: install
	pytest --cov=${repo} --cov-report=xml --verbose && \
	codecov --token=${codecov_token}

format:
	black --line-length 100 ${repo}
	black --line-length 100 tests

install:
	pip install --editable .

linter:
	$(call lint, ${repo})
	$(call lint, tests)

mutants: install
	mutmut run --paths-to-mutate ${repo}

tests: install
	pytest --verbose
