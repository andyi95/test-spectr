FROM python:3.10

# RUN apt-get update && apt-get install -y gettext

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
