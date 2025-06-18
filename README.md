# Job Application Tracker API

A RESTful API for tracking job applications, built with Django REST Framework. This API allows users to manage and monitor their job search process efficiently.

## Features

- Add, update, and delete job applications
- Track application status (e.g., applied, interviewing, offered, rejected)
- Store company, position, and contact details
- User authentication (if implemented)
- API endpoints for integration with front-end or other tools

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anilreddysbs/Job-Application-Tracker-API.git
   cd Job-Application-Tracker-API
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install Django and Django REST Framework manually: `pip install django djangorestframework`)*

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **API is available at:**  
   [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  
   *(Adjust the URL based on your API routing.)*

## API Endpoints

- `GET /api/applications/` — List all job applications
- `POST /api/applications/` — Create a new job application
- `GET /api/applications/<id>/` — Retrieve a specific application
- `PUT /api/applications/<id>/` — Update an application
- `DELETE /api/applications/<id>/` — Delete an application

*(Update these endpoints based on your actual API URLs.)*

## Usage

- Use tools like [Postman](https://www.postman.com/) or `curl` to interact with the API.
- Integrate with a front-end or mobile app for a complete job tracking solution.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

---

*Easily track your job applications with this API!*
