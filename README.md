# Sero Global 🧠

**Sero Global** is a modern mental health platform built with Django and AWS to improve access to therapy, education, and progress tracking. It empowers users and therapists with secure, remote tools for better mental wellness care.

---

## 🌟 Key Features

- ✅ Secure user authentication & profile management
- 🔍 Therapist discovery and appointment booking
- 📹 Encrypted video conferencing for remote sessions
- 📚 Educational resource library on mental health
- 📈 Progress tracking and goal-setting tools
- 🛠️ Admin dashboard for content and user management

---

## 🛠 Tech Stack

**Backend**: Django · Python · PostgreSQL  
**Frontend**: HTML · CSS · Bootstrap · JavaScript  
**Infrastructure**: AWS (EC2, S3, RDS, CloudFront)  
**DevOps**: Docker · GitHub Actions (CI/CD) · Heroku-compatible  

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.10+
- PostgreSQL 13+
- Redis 6+ (for channels/WebSocket support)
- Git & Virtualenv

---

### ⚙️ Local Setup

1. **Clone the repo**

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

### 🧪 Running Tests

```bash
pytest
```

### 📦 Deployment

1. **Install production requirements**

```bash
pip install -r requirements/production.txt
```

2. **Use Gunicorn + Nginx for deployment**

- Ensure environment variables are set securely.

3. **Recommended Hosting**

- **Heroku** - For quick MVP deployment

- **AWS EC2 + S3 + RDS** - For production-scale

## 🤝 Contributing

We welcome contributions from the community!

- Fork the repo

- Create a new branch

- Submit a pull request

Please read CONTRIBUTING.md for our guidelines.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built with care for mental health and human connection. 💙
