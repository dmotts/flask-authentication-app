
# Flask Authentication App

This is a Flask-based authentication app that allows users to sign up, log in, and log out. The app is built using Flask, Flask-SQLAlchemy for database management, and includes secure password handling using Werkzeug.

## Project Overview

This project serves as a template for building user authentication in Flask applications. It includes:
- User registration
- User login and session management
- Secure password storage using hashing
- Simple user greeting upon login

## Features

- **User Registration**: New users can sign up with their email and password.
- **User Login**: Registered users can log in with their credentials.
- **Session Management**: The app uses Flask sessions to manage user authentication states.
- **Database**: SQLite is used as the database backend for storing user information.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)
- A virtual environment tool (recommended)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/dmotts/flask-authentication-app.git
cd flask-authentication-app
```

### 2. Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Initialize the SQLite database by running the following command:

```bash
flask shell
```

Inside the Flask shell, run:

```python
from app import db
db.create_all()
exit()
```

This will create a `users.db` file in the `instance` folder.

### 5. Run the Application
Start the Flask development server:

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to access the app.

## Contributions

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes tests where appropriate.

## Follow Me

If you find this project useful, please consider following me on GitHub:
- [Daley Mottley (dmotts)](https://github.com/dmotts)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
