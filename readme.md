
Мінісистема каталогізації курсів на Django (`Course`, адмінпанель, HTML-список опублікованих курсів та JSON API).

## Встановлення та запуск
1. Перейдіть у папку проєкту та створіть віртуальне середовище:
   python -m venv .venv


2. Активуйте віртуальне середовище:
   * **Windows (PowerShell):**
     .venv\Scripts\Activate.ps1
     
   * **macOS / Linux:**
     source .venv/bin/activate
     

3. Встановіть залежності:
   python -m pip install -r requirements.txt
   

4. Застосуйте міграції та виконайте перевірку проєкту:
   python manage.py migrate
   python manage.py check


5. Створіть суперкористувача та запустіть сервер:
   python manage.py createsuperuser
   python manage.py runserver
   

Маршрути:
* `/admin/` — адмінпанель Django (керування моделлю `Course`)
* `/courses/` — HTML-сторінка зі списком опублікованих (`published`) курсів
* `/api/courses/` — JSON-ендпоінт з назвами та місткістю опублікованих (`published`) курсів

Тести та перевірки:
python manage.py test
python manage.py check
python manage.py makemigrations --check --dry-run