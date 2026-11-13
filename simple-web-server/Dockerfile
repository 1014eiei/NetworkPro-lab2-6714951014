FROM python:3.10-slim

WORKDIR /app

# คัดลอกและติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดแอปพลิเคชัน
COPY app.py .

# เปิดพอร์ต 5000 และรัน Flask
EXPOSE 5000
CMD ["python", "app.py"]