# Gunakan Python 3.11 sebagai base image
FROM python:3.11-slim

# Set metadata
LABEL maintainer="yuhanidz2325@gmail.com"
LABEL description="Linear Regression Project with Custom Matrix Operations"

# Set working directory di dalam container
WORKDIR /app

# Copy requirements.txt terlebih dahulu (untuk Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh project ke container
COPY . .

# Generate hasil regresi saat build (opsional, bisa juga saat runtime)
# RUN python regression/save_regression_results.py

# Expose port yang digunakan Flask (sesuaikan dengan app.py kamu: port 8000)
EXPOSE 8000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Health check - cek apakah container masih hidup
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Command untuk menjalankan aplikasi
CMD ["python", "app.py"]