# Techdome todos API
> A simple to-do application to demonstrate CRUD operations.

### Setup

The following steps will walk you through installation on a Linux. Mac should be similar.
It's also possible to up and running on a Windows machine.

#### Dependencies
###### Prerequisites

- Python 3.8.10
- PostgreSQL 13.2
- Django 3.2
- Djangorest framework 3.13.1

Create virtualenv in your system then follow the commends:
```` virtualenv venv --python=python3.8 ```` or ````python3 -m venv venv````

After successfully creation of the virtualenv then activate it:
```source venv/bin/activate```

> Then create a `.env` file and paste code from `.env-example` file and update by valid information.

After that please run following commands for up and running in local development server:
```bash
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```



## Table of contents:
- Well organized `CRUD` operations.
- JWT authentication.
- Custom user model
   - User Login
     - endpoint : `http://127.0.0.1:8000/accounts/login/`
   - User Registration : 
     - endpoint :`http://127.0.0.1:8000/accounts/register/`
- Todos app
  - Get all todo list
    - endpoint: `http://127.0.0.1:8000/todos/all/`
  - Get / Update / Delete todo by id
    - endpoint: `http://127.0.0.1:8000/todos/{id}/`

  
#### See live version
You can find live version here hosted on **Heroku** : [Live Here](https://techdome-api.herokuapp.com/)

You can login to admin dashboard by using following credentials:
- Email : `admin@admin.com`
- password : `123456`
