# django_tutorial

This is a small Django tutorial project created during setup.

Quick start (PowerShell on Windows):

```powershell
# activate virtualenv (if your venv is named `env` and created at project root):
.\env\Scripts\Activate.ps1
# or if venv named `venv`:
.env\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# run migrations and start server
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser to view the app.

Project layout (key files):
- `manage.py`
- `myproject/` (Django project settings)
- `core/` (tutorial app with `views.py`)
- `templates/` (project templates)
- `static/` (project static assets)

If you want me to move templates into the `core` app or make other changes, tell me which change to make next.
