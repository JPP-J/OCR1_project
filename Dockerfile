FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . /app/

# Run the app
CMD ["gunicorn", "-b", "0.0.0.0:8000", "ocr_blog:create_app()"]
