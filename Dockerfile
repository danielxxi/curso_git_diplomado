# Usar imagen base oficial de Python (versión ligera)
FROM python:3.11-slim

# Establecer directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY src/docker_kubernetes_tutorial/app.py .
COPY src/docker_kubernetes_tutorial/requirements.txt . 2>/dev/null || echo "requirements.txt no encontrado"

# Instalar dependencias
RUN pip install --no-cache-dir flask

# Exponer puerto 5000
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

# Healthcheck para verificar que el contenedor está vivo
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1
