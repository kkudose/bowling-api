# About

Tech demo (and an excuse to check out [Tastypie](http://tastypieapi.org/)). [Django](https://www.djangoproject.com/) project for a bowling scoring REST API. Meant to represent 4~6 hrs work.

&nbsp;
# Setup

- `poetry install` to install all dependencies (prerequisite: install [Poetry](https://python-poetry.org/docs/))
- For contributing: `poetry run pre-commit install` to install pre-commit git hooks
- `poetry run python manage.py migrate` to run migrations

&nbsp;
# Use

- `poetry run python manage.py runserver` to run api
- `poetry run python manage.py test` to run tests

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
- `pm shell_plus` for an interactive shell
- `pm reset_db` to reset local db
- `pm createsuperuser` to create admin credentials
