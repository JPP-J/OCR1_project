FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["gunicorn", "-b", "0.0.0.0:8000", "ocr_blog:create_app()"]
