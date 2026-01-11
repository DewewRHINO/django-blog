# Django Blog

A small, Markdown-powered blog site built with Django so that I can learn django :D

## Overview

- **What it is:** A simple blog application using Django with Markdown support for posts and an admin interface for creating posts and uploading images.
- **Key features:**
  - Markdown editing and rendering (`django-markdownx`, `markdownify`) with a generated Table of Contents (ToC) for posts (This took me way too long)
  - Post image uploads via admin (`PostImage` model, inline in the `Post` admin)
  - Responsive static theme and templates under `blog/templates/blog` and `blog/static/blog`

## Tech stack & requirements 🔧

- Python 3 (Check Docker file for specifics)
- Django (see `requirements.txt`)
- `django-markdownx`, `django-markdownify`, `markdown`
- Optional: PostgreSQL (configured in `compose.yml`) or default SQLite
- Optional: https://docs.docker.com/engine/install/ubuntu/ if you want to Deploy via docker

## Quick start — local development (venv) 💡

1. Create & activate a virtual environment:

   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```
   python manage.py migrate
   ```

4. Create a superuser to access Django admin:

   ```
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Visit the site:
   Note: If you want to run as development so static files are rendering you must switch debug to true!
   `DEBUG = bool(os.environ.get("DEBUG", default=1))`

   - Blog index: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Docker / docker-compose usage

A `dockerfile` and `compose.yml` are included for containerized development. So all you have to do is pull an image and start running it.

- Build & run with docker-compose (recommended):

  1. Create a `.env` file (example below).
  2. Run:
     ```bash
     docker compose -f compose.yml up --build
     ```

- Or build the image and run the container directly:

  ```bash
  docker build -t django-blog .
  docker run -p 8000:8000 django-blog
  ```

## Environment variables / `.env` example

compose.yml references the following variables. For local dev with SQLite you only need a few; for Postgres, provide DB details.

Example `.env`:

```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=1
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=postgres
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

Notes:

- If `DATABASE_ENGINE` is not set, the project defaults to SQLite (`db.sqlite3`) as configured in `mysite/settings.py`.
- `MEDIA_ROOT` is set to the `media/` folder; uploaded post images live under `media/post_images/`.

## Admin & content authoring

- Create posts in the Django Admin (`/admin/`) using the `Post` model.
- Fields on `Post` include (see `blog/models.py`):
  - `post_title`, `post_text_field` (Markdown content via `MarkdownxField`), `pub_date`, `post_style`, `post_summary`.
- Upload images via the inline `PostImage` admin (stored in `media/post_images/`).
- The post detail view converts Markdown to HTML and generates a ToC using `markdown` extensions (`extra`, `toc`) in `blog/views.py`.

## How the site is organized

- `manage.py` — Django CLI
- `mysite/` — project settings and URL config (`mysite/settings.py`, `mysite/urls.py`)
- `blog/` — app code (models, views, admin, templates, static assets)
  - Templates: `blog/templates/blog/` (`index.html`, `post.html`, shared partials)
  - Static: `blog/static/blog/assets/` (CSS, JS, images)
  - Models: `Post`, `PostImage` (`blog/models.py`)
  - Views: `IndexView` (list) and `DetailView` (post + ToC)

## Notes & troubleshooting

- In development, Django serves media files because `mysite/urls.py` includes `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`.
- For production, ensure `DEBUG=False`, set proper `ALLOWED_HOSTS`, and serve static/media via a web server or cloud storage.
- If images don't appear after upload, confirm `MEDIA_URL`/`MEDIA_ROOT` and that your server is configured to serve media files.

## Resources

- https://docs.djangoproject.com/en/6.0/intro/tutorial01/
  -- I pretty much went through all of the Django creating a blog tutorial, then decided on how I wanted to deploy my own server. I already had made stuff in notion that I could export as markdown so I wanted to see how I can make it easy for uploading images and stuff with this project.

---

If you'd like, I can also add a `.env.example` file, a `CONTRIBUTING.md`, or a one‑click Docker Compose override for local development—tell me which you'd prefer next.
