# 🩸 LifeSaver | Blood Donation Management System (BDMS)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Deployment](https://img.shields.io/badge/Deployed-Render/Railway-blue?style=for-the-badge&logo=render&logoColor=white)](https://render.com)

**LifeSaver** is a modern, web-based platform designed to bridge the gap between blood donors and patients. By eliminating intermediaries, it facilitates real-time communication, ensures donor privacy, and fosters a community-driven approach to saving lives.

---

## 🌟 Key Features

### 👤 For Donors
- **Dynamic Profiles**: Manage your personal information, blood group, and contact details.
- **"Ready to Donate" Status**: A single-click toggle to indicate your immediate availability.
- **Privacy First**: Your contact details are only shared with authorized patients.

### 🏥 For Patients
- **Smart Donor Search**: Filter donors by blood group, state, and city.
- **Urgent Blood Requests**: Post public requests with specific requirements (blood type, location, urgency).
- **Real-time Directory**: Access a curated list of active donors in your vicinity.

### 🛠 For Admins
- **Full Control**: Manage users, monitor requests, and ensure data integrity through the Django Admin dashboard.

---

## 🏗 Project Architecture & Pipelines

### 🛠 Tech Stack
- **Backend**: Python 3.10+, Django 3.2
- **Database**: 
  - **Local**: SQLite (Fast development)
  - **Production**: PostgreSQL (Scalable & Persistent)
- **Static Assets**: WhiteNoise (Compressed asset serving)
- **WSGI Server**: Gunicorn

### 🛤 Pipeline & Deployment Structure
The project is built with a **Continuous Integration & Continuous Deployment (CI/CD)** mindset:

1. **Local Development**: Code changes tested with `runserver`.
2. **Version Control**: Git-based workflow with automated tracking of migrations.
3. **Build Pipeline**: 
   - **Environment**: Nixpacks / Buildpacks detection.
   - **Steps**: Dependency installation (`requirements.txt`) -> Database migrations -> Static file collection.
4. **Deployment Strategy**: 
   - **Render/Railway**: Automatic deployments on every `git push`.
   - **Health Checks**: Automated monitoring of the root path `/`.

---

## 📂 Project Structure

```text
blood_donation_management/
├── Code/
│   ├── BloodDonation/      # Main Project Configuration (settings, urls, wsgi)
│   ├── home/               # core App (Models, Views, Templates, Static)
│   ├── templates/          # Global Templates
│   ├── manage.py           # Django Management Script
│   └── requirements.txt    # Backend Dependencies
├── Procfile                # Deployment Process Configuration
├── railway.json            # Infrastructure as Code (Railway)
└── README.md               # You are here!
```

---

## 🚀 Installation & Setup

### 1. Clone & Navigate
```bash
git clone https://github.com/parasmani-dev/blood_donation_management.git
cd blood_donation_management/Code
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
python manage.py migrate
```

### 4. Run Locally
```bash
python manage.py runserver
```
Access the app at `http://127.0.0.1:8000`.

---

## 🌐 Deployment Guide (Production)

To deploy this project to **Render** or **Railway**:

1. **PostgreSQL**: Create a PostgreSQL instance on your host.
2. **Env Vars**: Set the following environment variables in your hosting dashboard:
   - `DATABASE_URL`: Your PostgreSQL connection string.
   - `SECRET_KEY`: A unique, long random string.
   - `DEBUG`: Set to `False`.
   - `ALLOWED_HOSTS`: `your-app.onrender.com` or `your-app.up.railway.app`.

---

## 🤝 Contributors

✨ **Parasmani Kushwaha** - [GitHub](https://github.com/PARASAMANI-DEV) | [Email](mailto:parasmanikushwaha4@gmail.com)  
✨ **Archit Kumar** - [GitHub](https://github.com/karchit11) | [Email](mailto:architkumar2928@gmail.com)  
✨ **Harsh Gupta** - [GitHub](https://github.com/harshbmsit) | [Email](mailto:harshbmsit007@gmail.com)  

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
<p align="center">Made with ❤️ to save lives.</p>
