# AGENTS Instructions

This repository contains a simple Django blog (`personal_blog`).

## Development
- Use Python 3.11+.
- Install dependencies with `pip install -r requirements.txt`.
- Start the server with `python manage.py runserver`.
- When updating models, run:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
  Include new migration files in your commits.

## Quality Checks
- Run the test suite with `python manage.py test`.

## Pull Requests
- Keep commits small and provide clear messages.
- Summaries should mention important changes and reference any related tests.
