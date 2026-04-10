
FROM python:3.12-slim

# Ustawiam folder roboczy wewnątrz kontenera
WORKDIR /app

# Kopiuję listę bibliotek i instaluję
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiuję resztę kodu 
COPY . .

# Komenda, która odpali skrypt po starcie kontenera
CMD ["python", "main.py"]