# Dockerfile

FROM python:3.10

# Установить рабочую директорию
WORKDIR /code

# Скопировать requirements.txt в контейнер
COPY requirements.txt /code/

# Установить зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать проект в контейнер
COPY . /code/

# Запустить сервер Gunicorn
CMD ["gunicorn", "app_store.wsgi:application", "--bind", "0.0.0.0:8000"]


