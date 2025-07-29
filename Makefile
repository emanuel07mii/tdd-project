run:
	@uvicorn store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k "$(k)" --pdb store ./tests/
