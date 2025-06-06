FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    tesseract-ocr \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN  pip install --upgrade pip
RUN  pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . /app/

# Expose port your Flask app uses (usually 8000 or 5000)
EXPOSE 8000

# Run the app with improved Gunicorn settings
CMD ["gunicorn", \
    "--bind", "0.0.0.0:8000", \
    "--workers", "2", \
    "--worker-class", "sync", \
    "--timeout", "60", \
    "--preload", \
    "--log-level", "info", \
    "--access-logfile", "-", \
    "--error-logfile", "-", \
    "ocr_blog:app"]

