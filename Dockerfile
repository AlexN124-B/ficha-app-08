FROM python:3.14-slim
LABEL org.opencontainers.image.title="Ficha técnica de aplicación móvil" \
      org.opencontainers.image.authors="Nombre Apellido · Nombre Apellido" \
      org.opencontainers.image.source="https://github.com/usuario/ficha-app-08"
WORKDIR /app
COPY ficha_app.py .
CMD ["python", "ficha_app.py"]
