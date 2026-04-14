FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libgomp1 \
    tesseract-ocr \
    libmagic1 \
    libmupdf-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Instalar explícitamente urllib3 y requests primero
RUN pip install --no-cache-dir pip==23.0.1 && \
    pip install --no-cache-dir urllib3==2.0.7 requests==2.32.3 && \
    # Verificar que urllib3 esté disponible
    python -c "import urllib3; import requests; print('urllib3 y requests correctamente instalados')" && \
    # Luego instalar el resto de dependencias
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
