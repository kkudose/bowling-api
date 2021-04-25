# About

Tech demo. REST API for bowling scoring using Django (and tastypie).

&nbsp;
# Setup

- `poetry install` to install all dependencies (prerequisite: install [Poetry](https://python-poetry.org/docs/))
- if contributing, `poetry run pre-commit install` to install pre-commit git hooks
- `poetry run python manage.py migrate` to run migrations
- `poetry run python manage.py runserver` to run api
- API: http://localhost:8000/api/v1/?format=json
- Admin: http://localhost:8000/admin/

&nbsp;

# Other

Note: aliased `poetry run python manage.py` as `pm`
- `pm test` to run tests
- `pm makemigrations` after any model changes
- `pm migrate` to apply migrations
- `pm shell_plus` for an interactive shell
- `pm reset_db` to reset local db
- `pm createsuperuser` to create admin credentials
