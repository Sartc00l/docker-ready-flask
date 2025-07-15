# Используем официальный образ Python с Alpine (легковесный)
FROM python:3.9-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект (кроме файлов из .dockerignore)
COPY . .

# Переменные окружения для Flask
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

# Открываем порт, который использует Flask (по умолчанию 5000)
EXPOSE 5000

# Запускаем приложение
CMD ["flask", "run", "--host=0.0.0.0"]