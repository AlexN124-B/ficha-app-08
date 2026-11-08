# Ficha técnica de una aplicación móvil

Programa en Python que muestra la ficha técnica de una aplicación móvil
antes de publicarla en la tienda: identificación, tamaño del APK, ingresos,
versionCode, permisos, color del icono, tipos de datos, redondeo de la
valoración y un resumen de todo.

Aplicación descrita: **APP-08 · Turnos de Farmacia**
(paquete `es.salud.turnosfarmacia`, versión 3.3.1).

Autores: [Nombre Apellido] · [Nombre Apellido]

## Ejecutar con Docker (sin descargar el código)

```
docker run --rm --pull always [usuario]/ficha-app-08:1.0.0
```

Imagen publicada en Docker Hub:
https://hub.docker.com/r/[usuario]/ficha-app-08

La imagen está construida para `linux/amd64` y `linux/arm64`.

## Ejecutar en local

Requisitos: Python 3.14 o superior.

```
python3 ficha_app.py
```

En Windows puede hacer falta usar `py ficha_app.py`.

## Construir la imagen

Requisitos: Docker, con Buildx para construcción multiplataforma.

```
docker build -t ficha-app-08 .
docker run --rm ficha-app-08
```

Para publicar una imagen multiarquitectura:

```
docker buildx build --platform linux/amd64,linux/arm64 \
  -t [usuario]/ficha-app-08:1.0.0 -t [usuario]/ficha-app-08:latest --push .
```

## Estructura del repositorio

- `ficha_app.py`: el programa.
- `Dockerfile`: receta de la imagen.
- `.dockerignore`: archivos que no entran en la imagen.
- `.gitignore`: archivos que no se suben al repositorio (`.venv`, `__pycache__`).
- `requirements.txt`: dependencias (vacío, el programa usa solo la biblioteca estándar).

## Pipeline de CI/CD

[Si hacéis la pipeline, explicad aquí qué hace: la etapa Comprobar se ejecuta
en cada push a main y compila el programa, comprueba PEP 8 y lo ejecuta; la
etapa Publicar se ejecuta al subir una etiqueta v* y publica la imagen en
Docker Hub. Si no la hacéis, borrad este apartado.]

## Versión

Etiqueta de entrega: `v1.0.0`. Imagen: `[usuario]/ficha-app-08:1.0.0`.