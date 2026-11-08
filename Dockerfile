FROM python:3.14-slim
LABEL org.opencontainers.image.title="Ficha técnica de aplicación móvil" \
      org.opencontainers.image.authors="Alejandro Nuñez, Sebastian Stancu" \
      org.opencontainers.image.source="https://github.com/AlexN124-B/ficha-app-08"
WORKDIR /app
COPY ficha_app.py .
CMD ["python", "ficha_app.py"]