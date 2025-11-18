FROM python:3.11-slim

WORKDIR /application
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy==2.3.5
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "application.py"]
