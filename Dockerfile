FROM python:3.8.2

EXPOSE 8501

WORKDIR /app

COPY requirements.txt /opt/app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"
