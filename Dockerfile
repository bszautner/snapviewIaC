FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc nginx && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/media /app/staticfiles && \
    chmod -R 775 /app && \
    chown -R 1000:0 /app /var/lib/nginx /var/log/nginx /etc/nginx && \
    chmod -R g+rwX /app /var/lib/nginx /var/log/nginx

COPY nginx.conf /etc/nginx/nginx.conf

USER 1000

EXPOSE 8000

CMD nginx && gunicorn snapview.wsgi:application --bind 0.0.0.0:8000 --workers 2