FROM python:3.10-slim
WORKDIR /var/www/flash
COPY . .
RUN pip install flask
ENV FLASK_ENV=production FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]