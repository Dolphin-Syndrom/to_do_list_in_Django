# ToDo List in Django Python Repository

## Overview

The ToDo List in Django repository provides a simple web application built using the Django framework. The application allows users to create and delete tasks in a to-do list.

## Usage

### 1. Clone the Repository

Clone the ToDo List repository to your local machine:

```bash
git clone https://github.com/Dolphin-Syndrom/to_do_list_in_Django.git
```

### 2. Install Dependencies

Navigate to the project directory and create a virtual environment:

```bash
cd to_do_list_in_Django
python -m venv venv
```

Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On Linux/Mac:

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

Run the Django development server:

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your web browser to access the ToDo List application.

### 4. Interact with the ToDo List

- Create a new task: Click on the "Add Task" button, enter the task details, and submit the form.
- Delete a task: Click on the "Delete" button next to a task to remove it from the list.

## Customization

### Database Configuration

By default, the project is configured to use SQLite. You can modify the `DATABASES` settings in `settings.py` to use a different database if needed.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

### Adding Features

Feel free to extend the functionality of the ToDo List application by adding new features. For example, you could implement user authentication, due dates for tasks, or task categories.

### Styling

Customize the appearance of the application by modifying the CSS files in the `static` directory.

## Notes

- This project uses Django, a high-level Python web framework.
- Make sure to run the migrations before starting the application:

```bash
python manage.py migrate
```

- Explore Django's documentation for more advanced features and customization options: [Django Documentation](https://docs.djangoproject.com/).
