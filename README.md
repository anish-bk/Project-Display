# Single Image 3D Reconstruction (SI3DR) - Project Showcase Website

A Django-based promotional website showcasing the SI3DR final year project from IOE Pulchowk Campus.

## 🎯 Project Overview

This website presents the Single Image 3D Reconstruction project, which combines multi-view diffusion models, neural radiance representations, and vision-language understanding to generate and edit 3D assets from single images.

## 🚀 Features

- **Responsive Design**: Mobile-first approach using Bootstrap 5
- **Dynamic Content**: Database-driven content management
- **Admin Dashboard**: Full Django admin for content management
- **Contact Form**: Store inquiries in database
- **SEO Optimized**: Semantic HTML structure
- **Animations**: Smooth scroll animations with AOS library

## 📁 Project Structure

```
si3dr_website/
├── manage.py
├── si3dr_website/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── project_showcase/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── fixtures/
│       └── initial_data.json
├── templates/
│   ├── base.html
│   └── project_showcase/
│       ├── home.html
│       ├── about.html
│       ├── technology.html
│       ├── architecture.html
│       ├── features.html
│       ├── screenshots.html
│       ├── results.html
│       ├── future_scope.html
│       ├── contact.html
│       └── team.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
        ├── hero.svg
        ├── team-placeholder.svg
        └── screenshot-placeholder.svg
```

## 🛠️ Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to project directory**:
   ```bash
   cd si3dr_website
   ```

2. **Create virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Django**:
   ```bash
   pip install django
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load sample data**:
   ```bash
   python manage.py loaddata initial_data.json
   ```

6. **Create superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `admin123` (change in production!)

7. **Collect static files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

9. **Access the website**:
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📄 Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Hero section, features overview, stats |
| About | `/about/` | Project details, objectives, team |
| Technology | `/technology/` | Tech stack, frameworks, ML models |
| Architecture | `/architecture/` | System pipeline, methodology |
| Features | `/features/` | Detailed feature breakdown |
| Screenshots | `/screenshots/` | Gallery with filtering |
| Results | `/results/` | Performance metrics, benchmarks |
| Future Scope | `/future/` | Planned enhancements |
| Contact | `/contact/` | Contact form, information |
| Team | `/team/` | Team members, supervisors |

## 🔧 Admin Dashboard

Access the Django admin at `/admin/` to manage:

- **Project Info**: Main project details
- **Team Members**: Add/edit team profiles
- **Supervisors**: Faculty information
- **Technologies**: Tech stack items
- **Features**: Project capabilities
- **Screenshots**: Gallery images
- **Results**: Performance metrics
- **Contact Submissions**: View form submissions

## 🎨 Customization

### Adding Screenshots

1. Go to Admin → Screenshots → Add Screenshot
2. Upload image and fill details
3. Assign category for filtering

### Updating Content

1. All content is editable via Django admin
2. Fallback content exists in templates if database is empty
3. Update static files for custom styling

### Changing Colors

Edit CSS variables in `static/css/style.css`:

```css
:root {
    --primary: #667eea;
    --secondary: #764ba2;
    /* ... other variables */
}
```

## 📱 Responsive Breakpoints

- Desktop: 1200px+
- Laptop: 992px - 1199px
- Tablet: 768px - 991px
- Mobile: < 768px

## 🔒 Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use environment variables for `SECRET_KEY`
4. Set up proper database (PostgreSQL recommended)
5. Configure static file serving (whitenoise/nginx)
6. Enable HTTPS

## 👥 Project Team

- **Anish Bishwakarma** (PUL078BCT011)
- **Ankit Belbase** (PUL078BCT013)
- **Dipan Bartaula** (PUL078BCT040)

### Supervisor
- **Assoc. Prof. Dr. Jyoti Tandukar**

## 📄 License

This project is part of the final year requirements at IOE Pulchowk Campus.

## 🙏 Acknowledgments

- Department of Electronics and Computer Engineering, Pulchowk Campus
- Project Management Team
- All faculty members who provided guidance

---

**Tribhuvan University | Institute of Engineering | Pulchowk Campus**

*December 2025*
