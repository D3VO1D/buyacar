# buyacar.com

## How to Run

### Linux

```
1. First terminal tab
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py generate_database --num_rows=100 --num_photos=5

2. Second terminal tab
cd ../frontend
npm i
npm run serve

Frontend will be available on http://localhost:8080
```

### Windows

```
1. First terminal tab
cd backend
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py generate_database --num_rows=100 --num_photos=5

2. Second terminal tab
cd ../frontend
npm i
npm run serve

Frontend will be available on http://localhost:8080
```
