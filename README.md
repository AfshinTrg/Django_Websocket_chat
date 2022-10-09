```
source venv/bin/activate
pip install -r requirements.txt
cd wschat/
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
url : http://127.0.0.1:8000/chat/<UserName>/
```
