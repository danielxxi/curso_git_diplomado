# Módulo 6: Proyectos Reales - De la teoría a producción
## Proyectos completos para tu portafolio

---

## 📋 Proyectos en este módulo

Proyectos reales que puedes agregar a tu portafolio.

---

## 🏗️ Proyecto 1: E-Commerce Simple

**Objetivo:** Crear un e-commerce completo con Docker y Kubernetes

### Arquitectura

```
┌─────────────────────────────────────┐
│ Cliente (navegador)                 │
└──────────┬──────────────────────────┘
           │
┌──────────▼──────────────────────────┐
│ Nginx (frontend + reverse proxy)    │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┬──────────┐
    │             │          │
┌───▼──────┐ ┌───▼────┐ ┌──▼────┐
│API Backend│ │Carrito │ │Búsqueda│
│(Python)   │ │(Node)  │ │(ES)    │
└───┬──────┘ └───┬────┘ └──┬────┘
    │            │         │
    └────────────┴─────┬───┘
                       │
                    ┌──▼──────┐
                    │PostgreSQL│
                    └──────────┘
```

### Componentes

1. **Frontend** (React)
2. **API Backend** (FastAPI - Python)
3. **Carrito** (Node.js)
4. **Búsqueda** (Elasticsearch)
5. **Base de datos** (PostgreSQL)
6. **Cache** (Redis)

### Estructura

```
ecommerce/
├── frontend/
│   ├── Dockerfile
│   ├── src/
│   │   └── App.jsx
│   └── package.json
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── cart-service/
│   ├── Dockerfile
│   ├── server.js
│   └── package.json
├── docker-compose.yml
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
└── README.md
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ecommerce
      POSTGRES_DB: ecommerce
    volumes:
      - db-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.0.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    volumes:
      - es-data:/usr/share/elasticsearch/data

  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://postgres:ecommerce@db:5432/ecommerce
      REDIS_URL: redis://redis:6379
    depends_on:
      - db
      - redis

  cart:
    build: ./cart-service
    ports:
      - "5001:5001"
    environment:
      REDIS_URL: redis://redis:6379
    depends_on:
      - redis

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      REACT_APP_API_URL: http://localhost:5000
      REACT_APP_CART_URL: http://localhost:5001

volumes:
  db-data:
  es-data:
```

### Desplegar en K8s

Usar los YAML del módulo 3 y 4 como base, adaptar servicios.

---

## 🚀 Proyecto 2: SaaS - Aplicación de Notas

**Objetivo:** Aplicación SaaS escalable con autenticación

### Features

- Registro de usuarios
- Crear/editar/eliminar notas
- Compartir notas
- API REST

### Stack

- **Frontend:** React
- **Backend:** FastAPI
- **Auth:** JWT
- **BD:** PostgreSQL
- **Caché:** Redis
- **Storage:** S3 (para archivos)

### Estructura

```
saas-notas/
├── frontend/
│   ├── Dockerfile
│   └── src/
│       ├── components/
│       ├── pages/
│       └── App.jsx
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
├── docker-compose.yml
├── kubernetes/
│   └── *.yaml
└── README.md
```

### Archivo main.py (Backend)

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timedelta

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos simulados
notes_db = {}
users_db = {}

# Autenticación con JWT
SECRET_KEY = "tu-clave-super-secreta"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

# Endpoints
@app.post("/api/auth/register")
def register(username: str, password: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[username] = {"password": password}
    return {"token": create_access_token({"sub": username})}

@app.get("/api/notes")
def get_notes(token: str):
    user = verify_token(token)
    username = user["sub"]
    return notes_db.get(username, [])

@app.post("/api/notes")
def create_note(title: str, content: str, token: str):
    user = verify_token(token)
    username = user["sub"]
    if username not in notes_db:
        notes_db[username] = []
    note = {"id": len(notes_db[username]) + 1, "title": title, "content": content}
    notes_db[username].append(note)
    return note

@app.delete("/api/notes/{note_id}")
def delete_note(note_id: int, token: str):
    user = verify_token(token)
    username = user["sub"]
    notes_db[username] = [n for n in notes_db[username] if n["id"] != note_id]
    return {"deleted": True}

@app.get("/health")
def health():
    return {"status": "ok"}
```

---

## 📊 Proyecto 3: Dashboard de Monitoreo

**Objetivo:** Recolectar métricas y mostrar dashboard

### Stack

- **Colector:** Prometheus
- **Visualización:** Grafana
- **App:** Flask
- **BD:** InfluxDB

### docker-compose.yml

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      PROMETHEUS_URL: http://prometheus:9090

  prometheus:
    image: prom/prometheus:latest
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prom-data:/prometheus
    ports:
      - "9090:9090"
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-data:/var/lib/grafana
    depends_on:
      - prometheus

volumes:
  prom-data:
  grafana-data:
```

---

## 🎯 Proyecto 4: Pipeline de Datos (ETL)

**Objetivo:** Extraer, transformar y cargar datos

### Componentes

1. **Extractor** (Python) - Lee datos de API
2. **Transformer** (Python) - Limpia y transforma
3. **Loader** (Python) - Carga en BD
4. **Scheduler** (Airflow o Celery)
5. **BD Destino** (PostgreSQL)

### Estructura

```
data-pipeline/
├── extractor/
│   ├── Dockerfile
│   └── extract.py
├── transformer/
│   ├── Dockerfile
│   └── transform.py
├── loader/
│   ├── Dockerfile
│   └── load.py
├── orchestrator/
│   └── airflow/
└── kubernetes/
```

### Ejecutar como Jobs en K8s

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: data-pipeline
spec:
  schedule: "0 2 * * *"  # 2 AM diariamente
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: pipeline
            image: data-pipeline:1.0
            env:
            - name: STEP
              value: "extract,transform,load"
          restartPolicy: OnFailure
```

---

## 🔐 Proyecto 5: Aplicación Segura (HTTPS + Auth)

**Objetivo:** Aprender seguridad en Kubernetes

### Features

- HTTPS con Let's Encrypt
- JWT para autenticación
- RBAC en K8s
- Network Policies
- Secrets para credenciales

### Configuración Ingress con HTTPS

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: app-cert
spec:
  secretName: app-tls
  issuerRef:
    name: letsencrypt-prod
  commonName: mi-app.com
  dnsNames:
  - mi-app.com
  - www.mi-app.com

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - mi-app.com
    secretName: app-tls
  rules:
  - host: mi-app.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
```

---

## 📝 Proyecto 6: Micro-servicios Complejos

**Objetivo:** Arquitectura completa de microservicios

### Servicios

1. **Auth Service** - Autenticación
2. **User Service** - Gestión de usuarios
3. **Product Service** - Catálogo
4. **Order Service** - Órdenes
5. **Payment Service** - Pagos
6. **API Gateway** - Enrutador

### Comunicación entre servicios

```
Cliente → API Gateway
              ↓
           ┌──┼──┬──┬──┐
           ↓  ↓  ↓  ↓  ↓
         Auth User Product Order Payment
           ↓  ↓  ↓
           └─→─┴─→ Shared BD
```

---

## 🎓 Checklist de Proyectos

Después de cada proyecto, verifica:

- [ ] Funciona en Docker Compose
- [ ] Funciona en Kubernetes local
- [ ] Tiene health checks
- [ ] Tiene logging
- [ ] Tiene tests
- [ ] README claro
- [ ] Está en GitHub

---

## 📚 Estructura Recomendada para GitHub

```
proyecto-ecommerce/
├── .github/
│   └── workflows/          # CI/CD
├── frontend/
├── backend/
├── docker-compose.yml
├── kubernetes/
├── docs/
│   └── README.md
├── tests/
├── .gitignore
└── LICENSE
```

---

## 🚀 Desplegar en Producción

Opciones:

1. **AWS EKS** - Managed K8s
2. **Google GKE** - Google Cloud
3. **Azure AKS** - Microsoft Azure
4. **DigitalOcean** - VPS simple
5. **Self-hosted** - Tu propio servidor

---

**Tiempo estimado por proyecto: 20-40 horas cada uno**

¡Elige un proyecto y crea tu portafolio!
