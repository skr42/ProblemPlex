# ProblemPlex
Made an application like StackOverflow type  Application where developer can ask thier question and Others can gave the Answer
# ProblemPlex 🧠💬  
*A Stack Overflow-style Q&A platform for developers and learners.*

ProblemPlex is a collaborative Q&A web application where users can ask coding questions, post answers, and engage with the developer community. Built with the Django framework, ProblemPlex allows user authentication, posting questions and answers, and browsing topics — making it an ideal platform for learners and tech enthusiasts.

---

## 🚀 Features

- 📝 Ask and answer programming-related questions
- 🔐 User authentication (Sign up, Login, Logout)
- 🧵 Threaded Q&A format
- 🏷️ Tagging support (WIP or upcoming)
- 📅 View question history and activity

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Version Control**: Git & GitHub

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Steps

```bash
# Clone the repo
git clone https://github.com/<your-username>/ProblemPlex.git
cd ProblemPlex

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional for admin access)
python manage.py createsuperuser

# Start the development server
python manage.py runserver

