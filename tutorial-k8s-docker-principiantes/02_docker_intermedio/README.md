# Módulo 2: Docker Intermedio - Conceptos avanzados
## Optimización, buenas prácticas y técnicas profesionales

---

## 📋 Contenido de este módulo

Aprenderás técnicas avanzadas de Docker para producción.

### 📑 Lecciones:

1. **Optimización de Imágenes** (1 hora) - Reducir tamaño
2. **Construcción Multi-etapa** (1 hora) - Multi-stage builds
3. **Redes Avanzadas** (1 hora) - Configuraciones complejas
4. **Seguridad en Docker** (1-2 horas) - Buenas prácticas
5. **Almacenamientos Avanzados** (1 hora) - Drivers y plugins
6. **Health Checks** (45 min) - Verificar salud de contenedores
7. **Logging y Debugging** (1 hora) - Troubleshoot problemas
8. **Best Practices** (1 hora) - Cómo escribir buenos Dockerfiles
9. **Registro Privado** (1 hora) - Docker registries personalizados
10. **Ejercicios Avanzados** (2-3 horas)

---

## 🎯 Objetivo

Después de este módulo:
- ✅ Optimizar imágenes Docker (reducir 50-90%)
- ✅ Usar multi-stage builds
- ✅ Implementar seguridad
- ✅ Debugging y troubleshooting
- ✅ Mejores prácticas profesionales

---

## ⏱️ Tiempo total: 8-10 horas

---

## 📚 Lección 1: Optimización de Imágenes

### El Problema

Un Dockerfile ingenuo puede crear imágenes de 500MB+.

```dockerfile
FROM ubuntu:22.04  # 77 MB base
RUN apt-get update && apt-get install -y python3 python3-pip  # +200 MB
RUN pip install numpy pandas scipy scikit-learn  # +300 MB
COPY app.py /app/
CMD ["python3", "/app/app.py"]
```

**Resultado:** Imagen de 600+ MB

### Solución 1: Usar imágenes base más ligeras

```dockerfile
# ❌ Pesada (77 MB)
FROM ubuntu:22.04

# ✓ Normal (140 MB)
FROM python:3.11

# ✓✓ Ligera (40 MB)
FROM python:3.11-slim

# ✓✓✓ Muy ligera (12 MB)
FROM python:3.11-alpine
```

### Solución 2: Reducir capas

```dockerfile
# ❌ Muchas capas
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y vim

# ✓ Una sola capa
RUN apt-get update && apt-get install -y curl git vim
```

### Solución 3: Limpiar después

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean && \  # Limpia caché de apt
    rm -rf /var/lib/apt/lists/*  # Elimina listas de paquetes

COPY app.py /app/
CMD ["python3", "/app/app.py"]
```

### Solución 4: Multi-stage (Ver Lección 2)

**Comparación de tamaños:**

```
Imagen original (ingenua):      600 MB
Con alpine:                     150 MB
Con slim + limpieza:           100 MB
Multi-stage:                     40 MB
```

---

## 📚 Lección 2: Construcción Multi-etapa (Multi-stage)

### ¿Qué es?

Construyes en varias etapas y solo copias lo que necesitas.

### Ejemplo Real: App Python

**Dockerfile ingenuo (sin multi-stage):**

```dockerfile
FROM python:3.11

WORKDIR /app

# Instalar build tools (200+ MB)
RUN apt-get update && \
    apt-get install -y build-essential gcc

# Copiar código
COPY requirements.txt .

# Instalar dependencias (compila paquetes C)
RUN pip install -r requirements.txt

# Copiar app
COPY app.py .

# Ejecutar
CMD ["python", "app.py"]

# RESULTADO: 500+ MB (contiene build tools innecesarios)
```

**Dockerfile con multi-stage:**

```dockerfile
# ETAPA 1: Compilar
FROM python:3.11 AS builder

WORKDIR /app

# Instalar solo lo necesario para compilar
RUN apt-get update && \
    apt-get install -y build-essential gcc && \
    apt-get clean

COPY requirements.txt .

# Instalar dependencias en /opt
RUN pip install --target=/opt/python-packages -r requirements.txt

---

# ETAPA 2: Runtime (imagen final)
FROM python:3.11-slim

WORKDIR /app

# Copiar SOLO los paquetes compilados de etapa 1
COPY --from=builder /opt/python-packages /opt/python-packages

# Copiar app
COPY app.py .

# Configurar Python path
ENV PYTHONPATH=/opt/python-packages

CMD ["python", "app.py"]

# RESULTADO: 150 MB (sin build tools)
```

### Ventajas

```
Ingenuo:        500 MB + tiempo de build
Multi-stage:    150 MB + tiempo de build

Ahorras:        70% de espacio + descargas más rápidas
```

### Ejemplo: Frontend React

```dockerfile
# ETAPA 1: Build
FROM node:18 AS builder

WORKDIR /build
COPY package.json package-lock.json .
RUN npm ci && npm run build

# ETAPA 2: Servir
FROM nginx:alpine

COPY --from=builder /build/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

# Resultado: 150 MB (sin node instalado en imagen final)
```

---

## 📚 Lección 3: Redes Avanzadas

### Tipos de redes en Docker

```bash
# 1. BRIDGE (default)
docker network create mi-red --driver bridge

# 2. HOST (usa red del host)
docker run --network host mi-app

# 3. OVERLAY (para Swarm)
docker network create -d overlay mi-red-overlay

# 4. NONE (sin red)
docker run --network none mi-app
```

### Ejemplo: Aplicación Multi-tier

```bash
# Crear red
docker network create mi-app-net

# Base de datos (solo acceso interno)
docker run \
  --network mi-app-net \
  --name db \
  -e POSTGRES_PASSWORD=pass \
  postgres:15

# Backend (acceso interno y externo)
docker run \
  --network mi-app-net \
  --name backend \
  -p 5000:5000 \
  mi-api:1.0

# Frontend (solo externo)
docker run \
  --network mi-app-net \
  --name frontend \
  -p 3000:3000 \
  mi-frontend:1.0
```

**Configuración en docker-compose:**

```yaml
version: '3.8'

networks:
  app-network:
    driver: bridge

services:
  db:
    image: postgres:15
    networks:
      - app-network
    environment:
      POSTGRES_PASSWORD: password

  backend:
    build: .
    networks:
      - app-network
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://postgres:password@db:5432/myapp
    depends_on:
      - db

  frontend:
    build: ./frontend
    networks:
      - app-network
    ports:
      - "3000:3000"
```

---

## 📚 Lección 4: Seguridad en Docker

### 1. No ejecutar como root

```dockerfile
# ❌ Inseguro - corre como root
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3
COPY app.py /app/
CMD ["python3", "/app/app.py"]

# ✓ Seguro - corre como usuario
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3
RUN useradd -m -u 1000 appuser
USER appuser
COPY --chown=appuser:appuser app.py /app/
CMD ["python3", "/app/app.py"]
```

### 2. Usar imágenes de registros de confianza

```dockerfile
# ✓ Oficial
FROM python:3.11

# ✗ Desconocido
FROM random-user/python-image:latest
```

### 3. Analizar vulnerabilidades

```bash
# Instalar Trivy
brew install trivy

# Escanear imagen
trivy image python:3.11

# Escanear Dockerfile
trivy config Dockerfile
```

### 4. Limitar recursos

```bash
# Limitar CPU y memoria
docker run \
  --cpus=1 \
  --memory=512m \
  mi-app:1.0
```

### 5. Usar secrets para credenciales

```bash
# Crear secret
docker secret create db_password -

# Usar en Swarm
docker service create \
  --secret db_password \
  mi-app:1.0
```

---

## 📚 Lección 5: Health Checks

### ¿Por qué?

Docker necesita saber si tu app está realmente funcionando.

### Sintaxis

```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1
```

### Opciones

- `--interval`: Cada cuánto revisar (default 30s)
- `--timeout`: Timeout de cada check (default 30s)
- `--start-period`: Esperar antes de empezar checks (default 0s)
- `--retries`: Intentos antes de declarar unhealthy (default 3)

### Ejemplo completo

```dockerfile
FROM python:3.11-slim

WORKDIR /app
RUN pip install flask requests
COPY app.py .

EXPOSE 5000

# Health check
HEALTHCHECK --interval=10s --timeout=3s --start-period=20s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')"

CMD ["python", "app.py"]
```

### Ver estado

```bash
docker ps
# HEALTH: healthy, unhealthy, starting

docker inspect --format='{{.State.Health.Status}}' container-name
```

---

## 📚 Lección 6: Logging y Debugging

### Ver logs

```bash
# Logs de contenedor
docker logs container-name

# Seguir logs en tiempo real
docker logs -f container-name

# Últimas 100 líneas
docker logs --tail=100 container-name

# Con timestamps
docker logs -t container-name
```

### Acceder a la shell del contenedor

```bash
# Bash
docker exec -it container-name bash

# Ash (para Alpine)
docker exec -it container-name ash

# Verifica archivos
docker exec container-name ls -la /app
```

### Copiar archivos

```bash
# Desde contenedor
docker cp container-name:/app/logs.txt ./logs.txt

# Hacia contenedor
docker cp ./config.json container-name:/app/
```

### Inspeccionar contenedor

```bash
# Información completa
docker inspect container-name

# Solo configuración
docker inspect -f '{{json .Config}}' container-name
```

---

## 📚 Lección 7: Best Practices en Dockerfiles

### Checklist de un buen Dockerfile

```dockerfile
# 1. Usar imagen base específica (no latest)
FROM python:3.11-slim

# 2. Metadatos
LABEL maintainer="tu@email.com"
LABEL version="1.0"

# 3. Directorio de trabajo
WORKDIR /app

# 4. Copiar solo lo necesario
COPY requirements.txt .

# 5. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar código
COPY --chown=appuser:appuser . .

# 7. Crear usuario no-root
RUN useradd -m -u 1000 appuser
USER appuser

# 8. Exponer puerto
EXPOSE 5000

# 9. Health check
HEALTHCHECK --interval=30s CMD curl -f http://localhost:5000/health || exit 1

# 10. Comando final
CMD ["python", "app.py"]
```

### Antip patterns

```dockerfile
# ❌ NO hacer esto

# 1. Usar latest
FROM python:latest

# 2. Root user
USER root

# 3. Instalar build tools en imagen final
RUN apt-get install -y build-essential gcc

# 4. Copiar archivos innecesarios
COPY . .

# 5. Procesos que no terminan
CMD service nginx start

# 6. Enviroment variables hardcodeadas
ENV DATABASE_PASSWORD=password123
```

---

## 📚 Lección 8: Docker Compose Avanzado

### Variables de entorno

```yaml
version: '3.8'

services:
  app:
    build: .
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - DEBUG=${DEBUG:-false}
    ports:
      - "${APP_PORT}:5000"
```

**Archivo .env:**
```
DATABASE_URL=postgresql://user:pass@db:5432/mydb
APP_PORT=8000
DEBUG=true
```

**Usar:**
```bash
docker-compose up  # Automáticamente carga .env
```

### Override de configuración

```yaml
# docker-compose.override.yml
version: '3.8'

services:
  app:
    volumes:
      - .:/app  # Mount local para desarrollo
```

Automáticamente se merging con el docker-compose.yml.

---

## ✅ Checklist de Dominio

- [ ] Entiendes multi-stage builds
- [ ] Puedes optimizar tamaño de imágenes
- [ ] Implementas health checks
- [ ] Debugueas contenedores
- [ ] Usas redes Docker correctamente
- [ ] Implementas seguridad básica
- [ ] Escribes Dockerfiles profesionales

---

## 🚀 Próximo Paso

Ahora estás listo para:

**Opción A: Kubernetes Intermedio**
→ Ve a [`04_kubernetes_intermedio`](../04_kubernetes_intermedio)

**Opción B: Ejercicios avanzados**
→ Ve a [`05_ejercicios_practicos`](../05_ejercicios_practicos)

---

**Tiempo estimado: 8-10 horas**

¡Felicidades, ahora eres un experto en Docker!
