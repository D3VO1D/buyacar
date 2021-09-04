# buyacar.com

## Как запустить

### Linux

```
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py runserver
```

### Windows

```
python -m venv venv
venv\Scripts\activate.bat
pip install -r backend/requirements.txt
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py runserver
```
