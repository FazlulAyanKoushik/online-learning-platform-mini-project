# Online Learning Platform Backend

This project is the backend system for an online learning platform built using Django Rest Framework. Database used is PostgresSQL.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

1. Clone the public repository:

```bash
git clone git@github.com:FazlulAyanKoushik/online-learning-platform-mini-project.git
```


Navigate to the project directory
```bash
cd online-learning-platform-mini-project
```

2. Create a virtual environment and activate it:

For Windows:
```bash
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```
For Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Run the Django migrations:

Navigate to Project root directory and run the following command:
```bash
cd learning_platform
```

```bash
python manage.py migrate
```

### Create a superuser:

```bash
python manage.py createsuperuser
```

### Run the Django development server:

```bash
python manage.py runserver
```

## How to operate this project and API description

### API Endpoints
- http://localhost:8000/api/v1/auth/users/register/ (POST)
  - `Registration`: Register a new user.
    - `Request Body`: 
        ```json
        {
          "username": "kalam",
          "password": "123456",
          "confirm_password": "123456",
          "first_name": "Md Abdul",
          "last_name": "kalam",
          "email": ""
        }
        ```
- http://localhost:8000/api/v1/token (POST)
    - `Login`: Obtain a token for a user.
        - `Request Body`: 
            ```json
            {
            "username": "kalam",
            "password": "123456"
            }
            ```



