# Что посмотреть?

Учебный Flask-проект для работы с мнениями о фильмах. Приложение показывает случайное мнение о фильме, позволяет добавлять новые мнения через форму и открывать отдельную страницу конкретного мнения по ссылке.

Проект был переработан в рамках задания по рефакторингу: код приложения разделён на модули по принципу разделения ответственности.

## Возможности

- отображение случайного мнения о фильме на главной странице;
- добавление нового мнения через веб-форму;
- просмотр отдельного мнения по его ID;
- хранение данных в SQLite;
- загрузка мнений из CSV-файла через пользовательскую Flask-команду;
- обработка ошибок `404` и `500`;
- использование шаблонов Jinja2 и статических файлов;
- поддержка миграций через Flask-Migrate.

## Технологии

- Python 3.12
- Flask 3.0.2
- Flask-SQLAlchemy 3.1.1
- Flask-WTF 1.2.1
- Flask-Migrate 4.0.7
- SQLite
- Jinja2
- Bootstrap

## Структура проекта

```text
what_to_watch/
├── instance/
│   └── db.sqlite3
├── migrations/
│   ├── versions/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── opinions_app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── cli_commands.py
│   ├── error_handlers.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
├── .env
├── .gitignore
├── opinions_app.py
├── opinions.csv
├── README.md
├── requirements.txt
└── settings.py
```

## Назначение основных файлов

| Файл | Назначение |
|---|---|
| `opinions_app.py` | Точка входа в приложение |
| `settings.py` | Настройки проекта |
| `opinions_app/__init__.py` | Создание Flask-приложения, подключение базы данных и миграций |
| `opinions_app/models.py` | Модели базы данных |
| `opinions_app/forms.py` | Flask-WTF формы |
| `opinions_app/views.py` | View-функции и маршруты |
| `opinions_app/error_handlers.py` | Обработчики ошибок |
| `opinions_app/cli_commands.py` | Пользовательские команды Flask CLI |
| `opinions.csv` | Данные для загрузки мнений в базу |

## Установка и запуск

Клонируйте репозиторий:

```bash
git clone https://github.com/FilonovGrigoriy/what_to_watch.git
```

Перейдите в директорию проекта:

```bash
cd what_to_watch
```

Создайте виртуальное окружение:

```bash
python -m venv venv
```

Активируйте виртуальное окружение.

Для Git Bash на Windows:

```bash
source venv/Scripts/activate
```

Для Linux/macOS:

```bash
source venv/bin/activate
```

Обновите `pip`:

```bash
python -m pip install --upgrade pip
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Переменные окружения

Создайте файл `.env` в корне проекта и добавьте в него:

```env
FLASK_APP=opinions_app
FLASK_DEBUG=1
```

## Настройки приложения

Файл `settings.py` содержит базовые настройки проекта:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SECRET_KEY = 'super-secret-key-123'
```

Для учебного проекта этого достаточно. В реальном проекте `SECRET_KEY` не должен храниться прямо в коде, его обычно выносят в переменные окружения.

## Подготовка базы данных

Если файл базы данных уже есть в директории `instance/`, этот шаг можно пропустить.

Если база данных отсутствует, создайте таблицы через Flask shell:

```bash
flask shell
```

В интерактивной консоли выполните:

```python
from opinions_app import db
db.create_all()
exit()
```

После этого можно загрузить стартовые данные из файла `opinions.csv`:

```bash
flask load_opinions
```

Команда прочитает CSV-файл и добавит мнения о фильмах в базу данных.

## Запуск проекта

Запустите сервер разработки:

```bash
flask run
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:5000
```

## Основные маршруты

| Маршрут | Описание |
|---|---|
| `/` | Главная страница со случайным мнением о фильме |
| `/add` | Страница добавления нового мнения |
| `/opinions/<id>` | Страница конкретного мнения |

## Работа с миграциями

В проекте подключён Flask-Migrate.

Создать новую миграцию после изменения модели:

```bash
flask db migrate -m "Migration description"
```

Применить миграции:

```bash
flask db upgrade
```

Откатить последнюю миграцию:

```bash
flask db downgrade
```

## Принцип разделения ответственности

В ходе рефакторинга код был разделён на отдельные модули:

- модели базы данных вынесены в `models.py`;
- формы вынесены в `forms.py`;
- маршруты и view-функции вынесены в `views.py`;
- обработчики ошибок вынесены в `error_handlers.py`;
- пользовательские CLI-команды вынесены в `cli_commands.py`;
- создание приложения и подключение расширений выполняется в `__init__.py`.

Такой подход упрощает поддержку проекта и делает структуру приложения понятнее по мере его роста.

## Автор

FilonovGrigoriy