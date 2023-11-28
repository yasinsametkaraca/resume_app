# resume_app


See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

## Example

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

More Examples:

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)


How to install packages in docker container
- docker compose run app pip install Pillow 
- docker-compose run app sh -c "pip freeze > requirements.txt" (run with no cache)
- if it doesn't work, try to write Pillow in requirements.txt and run docker-compose build again and run pip freeze > requirements.txt

How to run docker container
- docker-compose up

How to run docker container in background
- docker-compose up -d

How to stop docker container
- docker-compose down

How to run django commands in docker container
- docker-compose run app sh -c "django-admin.py startproject app ."

How to run tests in docker container
- docker-compose run app sh -c "python manage.py test && flake8"

How to create superuser in docker container
- docker-compose run app sh -c "python manage.py createsuperuser"

How to create migrations in docker container
- docker-compose run app sh -c "python manage.py makemigrations"
