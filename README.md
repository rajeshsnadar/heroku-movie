# Heroku-Movie

API request examples:

base API - https://rajeshkumar-movies.herokuapp.com/api/movies

filter by name (full text search) - https://rajeshkumar-movies.herokuapp.com/api/movies?name=wizard

filter by movie name and director name - https://rajeshkumar-movies.herokuapp.com/api/movies?name=wizard&director=victor

filter by genre name - https://rajeshkumar-movies.herokuapp.com/api/movies?genre=family

Admin-panel - https://rajeshkumar-movies.herokuapp.com/admin

# Setting up project and initializing data

create a virtualenv 

virtualenv env

cd env

./Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

python manage.py populate_movies