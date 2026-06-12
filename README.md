# Сервис заявок

Веб-приложение на Django для приёма и просмотра клиентских заявок. Позволяет создавать заявки через форму, просматривать список с поиском и пагинацией, открывать карточку заявки и менять её статус. Развёртывание — Docker Compose.

## Возможности

- Список заявок с цветными бейджами статусов
- Создание заявки через форму с валидацией и маской телефона
- Карточка заявки с возможностью сменить статус
- Поиск по таблице на стороне браузера (имя, телефон, email)
- Пагинация заявок на странице
- Панель Django Admin с поиском и фильтром по статусу

## Стек

- Python 3.12
- Django 5.1
- django-bootstrap5
- SQLite
- Docker / Docker Compose

## Переменные окружения

Создай файл `.env` в корне проекта (пример — в `.env.example`):

```
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Запуск локально через Docker

```
git clone https://github.com/phentalex/<repo>.git
cd <repo>
docker compose up --build -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Доступно здесь -> http://localhost:8000/requests/

## Локальный запуск без Docker

**Linux/macOS:**

```
git clone https://github.com/phentalex/<repo>.git
cd <repo>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

**Windows:**

```
git clone https://github.com/phentalex/<repo>.git
cd <repo>
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Доступно здесь -> http://localhost:8000/requests/

## Реализованные страницы

| Метод | URL | Описание |
| --- | --- | --- |
| GET | `/requests/` | Список заявок: таблица, бейджи статусов, поиск, пагинация |
| GET / POST | `/requests/create/` | Создание заявки с валидацией |
| GET / POST | `/requests/<id>/` | Карточка заявки и смена статуса |
| GET | `/admin/` | Админка: список, поиск, фильтр по статусу |

## SEO

## SEO

На странице списка заявок добавлены SEO-элементы:

- **title** — название страницы, которое видно во вкладке браузера и в результатах поиска
- **meta description** — короткое описание, которое поисковик показывает под ссылкой на сайт
- **h1** — главный заголовок страницы, по которому понятно, о чём она
- **lang="ru"** — указывает, что страница на русском языке
- правильная структура HTML — страница собрана из подходящих по смыслу тегов

## Что сделано в рамках задания

Основное:

- Модель `Request` со статусами (новая / в работе / выполнена) и датой создания
- Админка: список заявок, поиск по имени, телефону и email, фильтр по статусу, дата только для чтения
- Страница списка заявок на Bootstrap: таблица, цветные бейджи статусов, кнопка «Создать заявку»
- Форма создания заявки на `ModelForm`: серверная валидация, сообщение об успехе, редирект на список
- Маска телефона при вводе (IMask), в базе номер хранится чистыми цифрами через `clean_phone`
- Клиентский JS-поиск по таблице (имя, телефон, email)
- SEO-элементы на странице списка
- Осмысленная история коммитов и README

Дополнительные задания:

- Пагинация списка
- Страница просмотра отдельной заявки с переходом из таблицы
- Смена статуса заявки прямо на её карточке
- Адаптация таблицы под мобильные: горизонтальная прокрутка (`table-responsive`) и скрытие второстепенных колонок на узких экранах
- Вынос настроек в переменные окружения и `.env.example`
- Контейнеризация: Dockerfile, docker-compose

## Админ панель

URL: `/admin/`

Логин и пароль задаются при выполнении `createsuperuser`.

## Автор

**Александр Уваров** — [GitHub](https://github.com/phentalex)
