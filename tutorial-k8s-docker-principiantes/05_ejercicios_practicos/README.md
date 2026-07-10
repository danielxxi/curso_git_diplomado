# Módulo 5: Ejercicios Prácticos
## Proyectos integrados para practicar

---

## 📋 Ejercicios en este módulo

Aquí encontrarás ejercicios que integran Docker y Kubernetes.

---

## 📝 Ejercicio 1: App TODO simple

**Objetivo:** Crear una app TODO en Flask, containerizarla y desplegarla en K8s

### Parte 1: Crear la aplicación

**app.py:**

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
todos = []

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    todo = request.json
    todo['id'] = len(todos) + 1
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return '', 204

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

**requirements.txt:**

```
Flask==2.3.0
gunicorn==20.1.0
```

**Dockerfile:**

```dockerfile
FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
```

### Parte 2: Construir imagen

```bash
cd ejercicio-1-todo
docker build -t mi-todo:1.0 .
docker run -p 5000:5000 mi-todo:1.0
```

**Probar:**

```bash
# Agregar TODO
curl -X POST http://localhost:5000/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"Aprender Docker","done":false}'

# Obtener TODOs
curl http://localhost:5000/api/todos
```

### Parte 3: Desplegar en Kubernetes

**deployment.yaml:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todo-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: todo
  template:
    metadata:
      labels:
        app: todo
    spec:
      containers:
      - name: todo
        image: mi-todo:1.0
        ports:
        - containerPort: 5000
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 10
          periodSeconds: 10
```

**service.yaml:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: todo-service
spec:
  selector:
    app: todo
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
  type: LoadBalancer
```

**Desplegar:**

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl port-forward service/todo-service 5000:5000
```

---

## 📝 Ejercicio 2: WordPress + MySQL

**Objetivo:** Orquestar WordPress y MySQL con Docker Compose

**docker-compose.yml:**

```yaml
version: '3.8'

services:
  wordpress:
    image: wordpress:6.0
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress123
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress-data:/var/www/html
    depends_on:
      - db

  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root123
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress123
    volumes:
      - mysql-data:/var/lib/mysql
    ports:
      - "3306:3306"

volumes:
  wordpress-data:
  mysql-data:
```

**Ejecutar:**

```bash
docker-compose up
```

Accede a: `http://localhost:8080`

---

## 📝 Ejercicio 3: Microservicios con Kubernetes

**Objetivo:** Crear 3 servicios comunicándose entre sí

### Servicios:

1. **API Gateway** (Puerto 5000)
2. **Servicio de Usuarios** (Puerto 5001)
3. **Servicio de Productos** (Puerto 5002)

**usuarios-service.py:**

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/usuarios')
def get_usuarios():
    return jsonify([
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "María"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

**productos-service.py:**

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/productos')
def get_productos():
    return jsonify([
        {"id": 1, "nombre": "Laptop", "precio": 1000},
        {"id": 2, "nombre": "Mouse", "precio": 20}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
```

**gateway-service.py:**

```python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/datos')
def get_datos():
    try:
        usuarios = requests.get('http://usuarios-service:5001/usuarios').json()
        productos = requests.get('http://productos-service:5002/productos').json()
        return jsonify({
            "usuarios": usuarios,
            "productos": productos
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**deployment.yaml:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: usuarios
spec:
  replicas: 1
  selector:
    matchLabels:
      app: usuarios
  template:
    metadata:
      labels:
        app: usuarios
    spec:
      containers:
      - name: usuarios
        image: usuarios-service:1.0
        ports:
        - containerPort: 5001
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: productos
spec:
  replicas: 1
  selector:
    matchLabels:
      app: productos
  template:
    metadata:
      labels:
        app: productos
    spec:
      containers:
      - name: productos
        image: productos-service:1.0
        ports:
        - containerPort: 5002
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gateway
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gateway
  template:
    metadata:
      labels:
        app: gateway
    spec:
      containers:
      - name: gateway
        image: gateway-service:1.0
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: usuarios-service
spec:
  selector:
    app: usuarios
  ports:
  - port: 5001
    targetPort: 5001
  type: ClusterIP
---
apiVersion: v1
kind: Service
metadata:
  name: productos-service
spec:
  selector:
    app: productos
  ports:
  - port: 5002
    targetPort: 5002
  type: ClusterIP
---
apiVersion: v1
kind: Service
metadata:
  name: gateway-service
spec:
  selector:
    app: gateway
  ports:
  - port: 5000
    targetPort: 5000
  type: LoadBalancer
```

**Desplegar:**

```bash
# Construir imágenes
docker build -t usuarios-service:1.0 -f usuarios/Dockerfile usuarios/
docker build -t productos-service:1.0 -f productos/Dockerfile productos/
docker build -t gateway-service:1.0 -f gateway/Dockerfile gateway/

# Desplegar
kubectl apply -f deployment.yaml

# Port-forward
kubectl port-forward service/gateway-service 5000:5000

# Probar
curl http://localhost:5000/datos
```

---

## 📝 Ejercicio 4: Escalar y actualizar

**Objetivo:** Practicar escalado y actualizaciones

```bash
# Ver deployments
kubectl get deployments

# Escalar a 5 replicas
kubectl scale deployment/mi-app --replicas=5

# Ver los 5 pods
kubectl get pods

# Actualizar imagen
kubectl set image deployment/mi-app app=mi-app:2.0

# Ver progreso
kubectl rollout status deployment/mi-app

# Deshacer si algo sale mal
kubectl rollout undo deployment/mi-app

# Ver historial
kubectl rollout history deployment/mi-app
```

---

## 📝 Ejercicio 5: Monitoreo

**Objetivo:** Ver logs y métricas

```bash
# Ver logs de un pod
kubectl logs pod-nombre

# Seguir logs
kubectl logs -f pod-nombre

# Ver eventos del clúster
kubectl get events

# Ver consumo de recursos
kubectl top nodes
kubectl top pods

# Describir pod
kubectl describe pod pod-nombre
```

---

## ✅ Soluciones

Las soluciones de los ejercicios están en la carpeta `soluciones/`

```bash
ls soluciones/
├── 01-todo-app/
├── 02-wordpress/
├── 03-microservicios/
├── 04-scaling/
└── 05-monitoreo/
```

---

## 🎯 Checkpoint

Después de estos ejercicios deberías poder:

- [ ] Crear un Dockerfile desde cero
- [ ] Construir una imagen personalizada
- [ ] Orquestar múltiples servicios con Docker Compose
- [ ] Desplegar en Kubernetes
- [ ] Escalar aplicaciones
- [ ] Ver logs y depurar
- [ ] Usar Services para comunicación

---

**¡Felicidades! Ya dominas Docker y Kubernetes a nivel principiante.**
