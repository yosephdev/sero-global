# Sero Global

A mental health platform built with Django, Python and AWS for better access to mental health services.

## Features

- User authentication and profile management
- Therapist discovery and booking system
- Secure video conferencing for remote sessions
- Resource library with mental health educational materials
- Progress tracking and goal setting tools
- Administrative dashboard

## Tech Stack

- Backend: Django, Python, PostgreSQL
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Infrastructure: AWS (EC2, RDS, S3, CloudFront)
- DevOps: Docker, CI/CD with GitHub Actions

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- PostgreSQL 13 or higher
- Redis 6 or higher (for WebSocket support)
- Git

### Local Development Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yosephdev/sero-global.git
   cd sero-global
   ```

2. **Set up a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements/development.txt
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with your local configuration.

5. **Set up the database**

   ```bash
   # Create database in PostgreSQL
   createdb sero_global
   
   # Run migrations
   python manage.py migrate
   
   # Create superuser
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the admin panel**

   - Visit `http://127.0.0.1:8000/admin/`
   - Log in with your superuser credentials

### Running Tests

```bash
pytest
```

### Production Deployment

For production deployment, use the production requirements:

```bash
pip install -r requirements/production.txt
```

Configure your production environment variables and use a production-ready WSGI server like Gunicorn with a reverse proxy like Nginx.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
