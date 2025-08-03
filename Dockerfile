FROM python:3.11-slim
WORKDIR /app

# 1. Install deps first (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 2. Copy source code
COPY fastapi_shop_api fastapi_shop_api

# 3. Run the service
CMD ["uvicorn", "fastapi_shop_api.main:app", "--host", "0.0.0.0", "--port", "80"]
