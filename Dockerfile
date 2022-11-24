# Pull base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system

# Copy project
COPY . /code/

EXPOSE 8000 

CMD python manage.py runserver 0.0.0.0:8000