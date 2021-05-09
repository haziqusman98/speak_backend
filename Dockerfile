FROM python:3.7-stretch

WORKDIR /speak_backend

# set the environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/speak_backend \
    DJANGO_SETTINGS_MODULE=speak_backend.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

EXPOSE 8000

# Install operating system dependencies
RUN apt-get update -y && \
    apt-get install -y apt-transport-https rsync gettext libgettextpo-dev && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs &&\
    rm -rf /var/lib/apt/lists/*

# Install Gunicorn
RUN pip install "gunicorn>=19.8,<19.9"

# start to install backend-end stuff
WORKDIR /speak_backend

# Install Python requirements.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code.
COPY . .

# Install assets
RUN python manage.py collectstatic --noinput --clear

# Run application
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "speak_backend.wsgi:application"]