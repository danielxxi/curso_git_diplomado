# Módulo 1: Docker Básico - Tu primer contenedor
## Desde la instalación hasta crear y ejecutar tu propia app

---

## 📋 Contenido de este módulo

Todo lo que necesitas para dominar Docker a nivel principiante.

### 📑 Lecciones en este módulo:

1. **Instalación en tu SO** (30-60 min) - Instala Docker en tu máquina
2. **Conceptos Docker** (1 hora) - Imágenes, contenedores, registros
3. **Primer Contenedor** (30 min) - Tu primer "Hola Docker"
4. **Dockerfile** (1-2 horas) - Crea tus propias imágenes
5. **Volumenes** (45 min) - Persistencia de datos
6. **Redes Docker** (45 min) - Comunicación entre contenedores
7. **Docker Compose** (1 hora) - Múltiples contenedores juntos
8. **Ejercicios Prácticos** (2-3 horas) - Refuerza lo aprendido

---

## 🎯 Objetivo

Después de este módulo:
- ✅ Docker instalado en tu máquina
- ✅ Ejecutar contenedores
- ✅ Crear tus propias imágenes
- ✅ Usar volumenes y redes
- ✅ Orquestar múltiples contenedores con Docker Compose

---

## ⏱️ Tiempo total: 8-10 horas

Puedes distribuirlo en 1-2 semanas, haciendo 1 lección por día.

---

## 📚 Instrucciones por Sistema Operativo

### Opción 1: macOS

**Paso 1: Descarga Docker Desktop**

Ve a: https://www.docker.com/products/docker-desktop

Descarga la versión para tu procesador:
- Apple Silicon (M1/M2/M3) → Descargar ARM64
- Intel → Descargar x86_64

**Paso 2: Instala**

1. Abre el archivo .dmg descargado
2. Arrastra "Docker.app" a "Applications"
3. Espera que termine la copia (1-2 minutos)
4. Abre Docker desde Applications
5. Ingresa tu contraseña cuando te lo pida

**Paso 3: Verifica la instalación**

Abre Terminal y ejecuta:

```bash
docker --version
docker run hello-world
```

Deberías ver:
```
Docker version 24.x.x

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

✓ **¡Docker instalado en macOS!**

---

### Opción 2: Linux (Ubuntu/Debian)

**Paso 1: Actualiza paquetes**

```bash
sudo apt update && sudo apt upgrade -y
```

**Paso 2: Instala Docker**

```bash
# Descarga e instala Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

**Paso 3: Agrega tu usuario**

```bash
# Para no usar sudo cada vez
sudo usermod -aG docker $USER

# Aplica los cambios
newgrp docker

# Verifica
docker --version
docker run hello-world
```

✓ **¡Docker instalado en Linux!**

---

### Opción 3: Windows (WSL2)

**Paso 1: Habilita WSL2**

PowerShell como Admin:

```powershell
wsl --install
```

**Paso 2: Descarga Docker Desktop para Windows**

https://www.docker.com/products/docker-desktop

**Paso 3: Instala**

1. Ejecuta el instalador
2. Sigue los pasos
3. Reinicia cuando te lo pida

**Paso 4: Verifica**

PowerShell:

```powershell
docker --version
docker run hello-world
```

✓ **¡Docker instalado en Windows!**

---

## 🚀 Tu Primer Contenedor

Una vez Docker instalado, ejecuta tu primer contenedor:

```bash
# Descarga la imagen nginx y corre un contenedor
docker run -p 8080:80 --name mi-primer-contenedor nginx
```

Explicación:
- `docker run` = Ejecuta un nuevo contenedor
- `-p 8080:80` = Mapea puerto 8080 local → 80 del contenedor
- `--name mi-primer-contenedor` = Nombre del contenedor
- `nginx` = Imagen a usar (se descarga automáticamente)

Abre navegador:
```
http://localhost:8080
```

¡Deberías ver "Welcome to nginx"! 🎉

Para detener:
```bash
# En otra terminal
docker stop mi-primer-contenedor
```

---

## 📚 Contenido Detallado de Lecciones

### Lección 1: ¿Qué es un Dockerfile?

Un Dockerfile es como una receta para construir una imagen.

**Ejemplo simple:**

```dockerfile
# 1. Imagen base (similar a "clonar una VM")
FROM python:3.11-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar archivos de tu máquina
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install -r requirements.txt

# 5. Copiar el código de la app
COPY app.py .

# 6. Puerto que expone
EXPOSE 5000

# 7. Comando a ejecutar cuando inicia el contenedor
CMD ["python", "app.py"]
```

**Paso a paso:**

```
Tú creas:          Docker construye:
┌──────────────┐   ┌──────────────────┐
│ Dockerfile   │   │ Imagen Docker    │
│ requirements │→  │ ┌──────────────┐ │
│ app.py       │   │ │ Python       │ │
└──────────────┘   │ │ Dependencias │ │
                   │ │ Tu app       │ │
                   │ │ Config       │ │
                   │ └──────────────┘ │
                   └──────────────────┘
                            ↓
                   ┌──────────────────┐
                   │ Contenedor       │
                   │ ┌──────────────┐ │
                   │ │ Tu app       │ │
                   │ │ Corriendo... │ │
                   │ └──────────────┘ │
                   └──────────────────┘
```

---

### Lección 2: Construir tu Primera Imagen

**Ejemplo: App "Hola Mundo"**

Crea estos archivos en una carpeta:

**app.py**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return '¡Hola desde Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**requirements.txt**
```
flask==2.3.0
```

**Dockerfile**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Construir imagen:**

```bash
# En la carpeta con los 3 archivos
docker build -t mi-app:1.0 .

# -t = nombre:versión
# . = Dockerfile en carpeta actual
```

Verás output:
```
Sending build context...
Step 1/7 : FROM python:3.11-slim
Step 2/7 : WORKDIR /app
...
Successfully built abc123def456
Successfully tagged mi-app:1.0
```

**Ejecutar:**

```bash
docker run -p 5000:5000 mi-app:1.0
```

Abre:
```
http://localhost:5000
```

¡Tu app en un contenedor! 🎉

---

### Lección 3: Volumenes (Persistencia de datos)

**Problema:** Cuando borras un contenedor, se pierden los datos.

**Solución:** Volumenes - permiten persistir datos.

**Tipos de volumenes:**

```
1. Volume Docker:
   docker run -v mi-volumen:/data imagen
   └─ Docker gestiona el almacenamiento

2. Bind Mount (carpeta local):
   docker run -v /ruta/local:/ruta/contenedor imagen
   └─ Mapea carpeta de tu máquina

3. tmpfs mount:
   docker run --tmpfs /data imagen
   └─ Almacenamiento en RAM (temporal)
```

**Ejemplo: PostgreSQL con persistencia**

```bash
# Crear volumen nombrado
docker volume create mi-data-db

# Ejecutar PostgreSQL con volumen
docker run \
  -v mi-data-db:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=micontraseña \
  -p 5432:5432 \
  postgres:15
```

Ahora:
- Los datos persisten después de borrar el contenedor
- Puedes recrear el contenedor y tendrás los datos

---

### Lección 4: Redes Docker

**Problema:** ¿Cómo se comunican dos contenedores?

**Solución:** Redes - permiten comunicación entre contenedores.

**Ejemplo: Frontend + Backend**

```bash
# Crear red
docker network create mi-red

# Backend
docker run \
  --network mi-red \
  --name backend \
  -p 5000:5000 \
  mi-app:1.0

# Frontend
docker run \
  --network mi-red \
  --name frontend \
  -p 3000:3000 \
  mi-frontend:1.0
```

Dentro del frontend, conectar al backend:
```javascript
// frontend/app.js
fetch('http://backend:5000/datos')  // ¡Usa el nombre del contenedor!
```

Docker resuelve automáticamente `backend` → IP del contenedor backend.

---

### Lección 5: Docker Compose

**Problema:** Escribir comandos largos es tedioso.

**Solución:** Docker Compose - define múltiples servicios en un archivo YAML.

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./app:/app
    environment:
      - DATABASE_URL=postgresql://user:pass@db/myapp
    depends_on:
      - db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=mypassword
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

**Usar:**

```bash
# Inicia todo
docker-compose up

# Ver estado
docker-compose ps

# Ver logs
docker-compose logs -f backend

# Detener todo
docker-compose down
```

---

## 🎯 Ejercicios Prácticos

### Ejercicio 1: Tu primera imagen

**Objetivo:** Crear una imagen con tu nombre

**app.py:**
```python
print("¡Hola! Soy [TU NOMBRE]")
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim
COPY app.py /app/
CMD ["python", "/app/app.py"]
```

**Comandos:**
```bash
docker build -t mi-nombre:1.0 .
docker run mi-nombre:1.0
```

✓ Deberías ver tu nombre impreso.

---

### Ejercicio 2: App web interactiva

**Objetivo:** App que responda HTTP

**app.py:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>¡Hola Mundo desde Docker!</h1>'

@app.route('/nombre/<name>')
def nombre(name):
    return f'<h1>Hola, {name}!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Dockerfile:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install flask
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

**Ejecutar:**
```bash
docker build -t mi-web:1.0 .
docker run -p 8000:5000 mi-web:1.0
```

**Prueba:**
- http://localhost:8000/ 
- http://localhost:8000/nombre/Juan

---

### Ejercicio 3: Docker Compose con BD

**Objetivo:** App + PostgreSQL orquestados

**docker-compose.yml:**
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/miapp
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=miapp
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

**Ejecutar:**
```bash
docker-compose up
```

---

## ✅ Checklist de Dominio

Cuando termines este módulo, deberías poder:

- [ ] Instalar Docker en tu SO
- [ ] Ejecutar un contenedor existente
- [ ] Entender qué es un Dockerfile
- [ ] Crear tu primera imagen Docker
- [ ] Ejecutar tu imagen como contenedor
- [ ] Mapear puertos correctamente
- [ ] Usar volumenes para persistencia
- [ ] Comunicar contenedores con redes
- [ ] Escribir un docker-compose.yml básico
- [ ] Explicar a alguien qué es un contenedor

---

## 🚀 Próximo Paso

Una vez domines Docker Básico:

**Opción A: Aprofundiza en Docker**
→ Ve a [`02_docker_intermedio`](../02_docker_intermedio)

**Opción B: Salta a Kubernetes**
→ Ve a [`03_kubernetes_basico`](../03_kubernetes_basico)

---

## 📚 Recursos Útiles

- **Documentación Docker**: https://docs.docker.com
- **Docker Hub**: https://hub.docker.com
- **Docker Compose**: https://docs.docker.com/compose
- **Best Practices**: https://docs.docker.com/develop/develop-images/dockerfile_best-practices

---

**Tiempo estimado: 8-10 horas**

¡Felicidades, pronto estarás creando tus propias imágenes Docker!
