# Используем официальный образ Python
FROM python:3.9

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Запускаем приложение
CMD ["python", "app.py"]
