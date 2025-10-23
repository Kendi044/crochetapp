Starting the creation of my app.   CROCHETAPP API DJANGO PROJECT

A RECIPE MANAGEMENT API, that helps creators to share their creation to crocheters who would like to get the skill or educate people interested with crocheting.
   
FEATURES:   1. User-authentication via Django REST Framework
            2. CRUD API for crochet patterns
            3. Endpoints for listing, retrieving, updating, and deleting patterns
            4. Example HTTP requests in test.http for quick testing

      Project Structure
crochetapp/
├── crochet/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/crochet
│   │   │   └── styles.css
│   │   │   └── scripts.js
│   │   |   └── yarn.jpg
│   ├── templates/crochet
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── pattern_detail.html
│   │   ├── pattern_list.html
│   │   └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── crochetapp/
|   >__pycache__ 
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
|  |__ db.sqlite3 
│  ├── manage.py
│  └── test.http
├── README.md
└── .gitignore

    Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/crochetapp.git
cd crochetapp

2. Install dependencies
pip install djoser

3. Apply database migrations
python manage.py makemigrations
python manage.py migrate

4. Create a superuser
python manage.py createsuperuser

5. Run the server
python manage.py runserver

6. Open http://127.0.0.1:8000
 
7. API Testing with test.http
    
    register,login and logout
POST http://127.0.0.1:8000/api/register/
Content-Type: application/json

{
  "username": "Maya",
  "email": "md@gmail.com",
  "password": "Dancing10"
}

POST http://127.0.0.1:8000/api/login/
Content-Type: application/json

{
  "username": "rose",
  "password": "Dancing10"
}

POST http://127.0.0.1:8000/api/logout/
Content-Type: application/json
Authorization: Token 0e72bfe6571186ac8f5532376632882790a572b9
   
    pattern_list.html
POST http://127.0.0.1:8000/api/patterns/
Content-Type: application/json
Authorization: Token 0e72bfe6571186ac8f5532376632882790a572b9

{
  "title": "Single crochet",
  "description": "A simple beginner pattern.",
  "difficulty_level": "EASY",
  "instructions": "Start with a chain of 20 stitches and single crochet across each row."
}

GET http://127.0.0.1:8000/api/patterns/
Authorization: Token 0e72bfe6571186ac8f5532376632882790a572b9
Accept: application/json

PUT http://127.0.0.1:8000/api/patterns/1/
Content-Type: application/json
Authorization: Token 0e72bfe6571186ac8f5532376632882790a572b9

{
  "title": "Updated Single Crochet Scarf",
  "description": "An improved version of the original beginner scarf pattern with more details.",
  "instructions": "Use a 5mm hook and soft yarn. Chain 30, then single crochet each row until desired length.",
  "difficulty_level": "EASY"
}

DELETE http://127.0.0.1:8000/api/patterns/1/
Authorization: Token 0e72bfe6571186ac8f5532376632882790a572b9

API:
GET	/api/patterns/	List all patterns
POST	/api/patterns/	Create a new pattern
GET	/api/patterns/<id>/	Retrieve a single pattern
PUT	/api/patterns/<id>/	Update a pattern
PATCH	/api/patterns/<id>/	Partial update
DELETE	/api/patterns/<id>/	Delete a pattern
🧵 Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (default)

Auth: Token Authentication

Testing: test.http, Django’s test client


GITHUB: 1. Fork the repository
        2. Add the respective files and update them
        3. Commit your changes
        4. Open a Pull Request

 Author= Rose Ngaamba
