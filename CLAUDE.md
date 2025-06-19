# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Development Server
```bash
python manage.py runserver
```

### Database Operations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Django Shell
```bash
python manage.py shell
```

### Testing
```bash
python manage.py test
```

## Architecture

This is a Django 5.2.1 blog application with a simple structure:

- **Project**: `personal_blog` - Main Django project configuration
- **App**: `blog` - Single Django app containing all blog functionality
- **Database**: SQLite3 (db.sqlite3) for development
- **Templates**: Uses Django template inheritance with base.html and app-specific templates

### Models (`blog/models.py`)
- `Post`: Blog posts with title, body, timestamps, and categories
- `Category`: Blog categories with many-to-many relationship to posts
- `Comment`: Comments linked to specific posts

### URL Structure
- `/` - Blog index (all posts)
- `/post/<id>/` - Individual post detail with comments
- `/category/<name>/` - Posts filtered by category
- `/admin/` - Django admin interface

### Templates Structure
- `templates/base.html` - Base template with Simple.css framework
- `blog/templates/blog/` - Blog-specific templates (index, detail, category)
- Uses Django template blocks for content extension

### Key Features
- Comment system with forms (`blog/forms.py`)
- Category-based post filtering
- Chronological post ordering (newest first)
- Bootstrap-style form classes for comments