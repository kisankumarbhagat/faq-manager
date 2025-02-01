# FAQ Manager

**faq-manager** is a dynamic and multilingual FAQ management system built with Django and Django Rest Framework (DRF). This project allows you to manage FAQs through an admin interface, display FAQs in different languages, and interact with them via a RESTful API. The app is designed to provide an easy-to-use interface for users while also offering a backend API to integrate with other applications.

## Features
- **Admin Panel**: Allows administrators to manage FAQs through Django's admin interface.
- **Multilingual Support**: FAQs can be displayed in different languages.
- **RESTful API**: Exposes FAQ data through an API using Django Rest Framework.
- **Caching**: FAQ data is cached for better performance and faster access.

## Requirements
- Python 3.10
- Django 4.0 or higher
- Django Rest Framework
- Redis (for caching)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/faq-manager.git
    cd faq-manager
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```

    The app will be available at `http://127.0.0.1:8000/`.

## Usage

- Admin interface: `http://127.0.0.1:8000/admin/`
- View FAQs: `http://127.0.0.1:8000/faqs/`
- API endpoint: `http://127.0.0.1:8000/api/faqs/`
