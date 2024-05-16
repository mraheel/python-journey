# Django REST Framework Project Setup

This is a basic guide to setting up a Django project with the Django REST Framework.

## Prerequisites

- Python 3.x installed on your system
- Basic understanding of command line

## Getting Started

1. Clone or download this repository to your local machine.

2. Navigate to the project directory:

    ```
    cd your_project_directory
    ```

3. Create a virtual environment for the project. It's recommended to use virtual environments to isolate your project dependencies:

    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

5. Install Dependencies using requirements.txt file:

    ```
    pip install -r requirements.txt
    ```

6. Run database migrations to create necessary database tables:

    ```
    python manage.py migrate
    ```

7. Start the Django development server:

    ```
    python manage.py runserver
    ```

8. Open your web browser and go to `http://127.0.0.1:8000/` to see your Django project running.

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Python Virtual Environments Documentation](https://docs.python.org/3/library/venv.html)

Happy coding!
