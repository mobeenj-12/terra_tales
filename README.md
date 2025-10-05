// ...existing code...
# Terra Tales

Terra Tales is a small Flask web app that visualizes 25 years of Earth observations (satellite-derived visuals and short guided pages). It serves interactive pages and media from the `templates/` and `static/` folders.

Quick links:
- App entry: [main.py](main.py) — Flask app instance: [`main.app`](main.py)
- Routes: [`main.home_page`](main.py), [`main.about_page`](main.py), [`main.melt_page`](main.py), [`main.air_page`](main.py), [`main.air2_page`](main.py), [`main.cropland_page`](main.py), [`main.cropland2_page`](main.py), [`main.why_page`](main.py)
- Templates: [templates/home.html](templates/home.html), [templates/melting.html](templates/melting.html), [templates/melting2.html](templates/melting2.html), [templates/air.html](templates/air.html), [templates/air2.html](templates/air2.html), [templates/cropland.html](templates/cropland.html), [templates/cropland2.html](templates/cropland2.html), [templates/why.html](templates/why.html)
- Static assets: [static/image](static/image) and [static/video](static/video)

Prerequisites
- Python 3.8+
- pip

Setup

1. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies
```bash
pip install flask
```

(Optionally create requirements.txt)
```bash
pip freeze > requirements.txt
```

Running the app

- Run directly:
```bash
python main.py
```
Open http://127.0.0.1:5000/ in your browser.

- Or use flask CLI:
```bash
# Linux / macOS
export FLASK_APP=main.py
export FLASK_ENV=development
flask run

# Windows (PowerShell)
$env:FLASK_APP = "main.py"
$env:FLASK_ENV = "development"
flask run
```

Routes
- Home: `/` — served by [`main.home_page`](main.py) -> [templates/home.html](templates/home.html)
- Melting overview: `/melting` -> [`main.about_page`](main.py) -> [templates/melting.html](templates/melting.html)
- Melting compare: `/melting2` -> [`main.melt_page`](main.py) -> [templates/melting2.html](templates/melting2.html)
- Atmosphere overview: `/air` -> [`main.air_page`](main.py) -> [templates/air.html](templates/air.html)
- Atmosphere compare: `/air2` -> [`main.air2_page`](main.py) -> [templates/air2.html](templates/air2.html)
- Cropland overview: `/cropland` -> [`main.cropland_page`](main.py) -> [templates/cropland.html](templates/cropland.html)
- Cropland compare: `/cropland2` -> [`main.cropland2_page`](main.py) -> [templates/cropland2.html](templates/cropland2.html)
- About / Why: `/why` -> [`main.why_page`](main.py) -> [templates/why.html](templates/why.html)

Notes & tips
- Media files are served from `static/`. Example images: [static/image/arcticseaice2000.jpg](static/image/arcticseaice2000.jpg), [static/image/arctic.jpg](static/image/arctic.jpg). Example videos: [static/video/arctic.mp4](static/video/arctic.mp4).
- The app currently runs with `debug=True` in [main.py](main.py). Disable in production.
- If you want to deploy, consider using a production WSGI server (gunicorn/uvicorn) and configuring static file serving via the web server.

Contributing
- Update templates under [templates/](templates/) and media under [static/](static/).
- Keep route names in [main.py](main.py) consistent with template names.

License
- Add a license file if you plan to share the project publicly.

Contact
- For help editing templates or adding new pages, open [main.py](main.py) and add a new route returning render_template with your new template.
