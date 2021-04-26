# About

Tech demo. REST API for bowling scoring using Django (and tastypie). Meant to represent 4~6 hrs work.

&nbsp;
# Setup

- `poetry install` to install all dependencies (prerequisite: install [Poetry](https://python-poetry.org/docs/))
- if contributing, `poetry run pre-commit install` to install pre-commit git hooks
- `poetry run python manage.py migrate` to run migrations
- `poetry run python manage.py runserver` to run api
- API: http://localhost:8000/api/v1/?format=json
- Admin: http://localhost:8000/admin/

&nbsp;
# API Use

[HATEOAS](https://restfulapi.net/hateoas/)-supported REST API: http://localhost:8000/api/v1/?format=json

Typical use involves five steps:
1. Create a player
2. Create a game
3. Create a roll
4. Get the updated game (with scores)
5. Repeat steps three and four

`Game.frame_scores` has the running scores for each frame as available, or if individual frame scores aren't needed, `Game.total_score` has just the total score.

&nbsp;
# Other

Note: aliased `poetry run python manage.py` as `pm`
- `pm test` to run tests
- `pm makemigrations` after any model changes
- `pm migrate` to apply migrations
- `pm shell_plus` for an interactive shell
- `pm reset_db` to reset local db
- `pm createsuperuser` to create admin credentials
