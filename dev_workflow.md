# Development Workflow

## After Model Changes
1. Create a new migration: `flask db migrate -m "Description of changes"`
2. Apply the migration: `flask db upgrade`
3. Test your changes

## Regular Maintenance
1. Update requirements: `pip freeze > requirements.txt`
2. Git commands:
   - `git status`
   - `git add .`
   - `git commit -m "Descriptive message"`
   - `git push`
3. Run tests (if applicable): `python -m pytest`
4. Check for outdated packages: `pip list --outdated`
5. Lint code: `flake8 .`
6. Format code: `black .`

Remember to activate your virtual environment before running these commands!
