# About

Tech demo. REST API for bowling scoring.

&nbsp;
# Setup

- `poetry install` to install all dependencies (prerequisite: install [Poetry](https://python-poetry.org/docs/))
- if contributing, `poetry run pre-commit install` to install pre-commit git hooks
- `cp .env.example .env` to create `.env` file
- `poetry run python manage.py runserver` to run

&nbsp;

# Other

Note: aliased `poetry run python manage.py` as `pm`
- `pm test` to run tests
- `pm makemigrations` after any model changes
- `pm migrate` to apply migrations
- `pm shell_plus` for an interactive shell
- `pm reset_db` to reset local db
