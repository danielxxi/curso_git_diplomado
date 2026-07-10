# Módulo 3: Kubernetes Básico - Orquestación de contenedores
## Tu primer clúster y despliegue

---

## 📋 Contenido de este módulo

Todo lo que necesitas para entender y usar Kubernetes a nivel principiante.

### 📑 Lecciones:

1. **Instalación K8s** (45 min) - Configura un clúster local
2. **Conceptos K8s** (1-2 horas) - Pods, Deployments, Services
3. **kubectl Básico** (1 hora) - Comandos esenciales
4. **Tu primer Pod** (30 min) - Crea y ejecuta un pod
5. **Deployments** (1 hora) - Replicación y actualizaciones
6. **Services** (1 hora) - Exponiendo aplicaciones
7. **Labels y Selectors** (45 min) - Organizando recursos
8. **Configuración** (1 hora) - ConfigMaps y Secrets
9. **Persistencia** (1 hora) - Volumenes en K8s
10. **Ejercicios Prácticos** (2-3 horas) - Integración

---

## 🎯 Objetivo

Después de este módulo:
- ✅ Kubernetes instalado en tu máquina
- ✅ Crear y gestionar pods
- ✅ Usar Deployments para replicación
- ✅ Exponer apps con Services
- ✅ Entender Labels y Selectors
- ✅ Configurar aplicaciones con ConfigMaps

---

## ⏱️ Tiempo total: 10-12 horas

Distribúyelo en 1-2 semanas, haciendo 1-2 lecciones por día.

---

## 🚀 Opción 1: Instalar en macOS

### Si tienes Docker Desktop

**Paso 1: Abre Docker Desktop**

Settings → Kubernetes → ✓ Enable Kubernetes

**Paso 2: Espera**

Verás "Kubernetes is starting..." 
Espera 2-5 minutos.

**Paso 3: Verifica**

```bash
kubectl version --client
kubectl get nodes
```

Deberías ver:
```
NAME             STATUS   ROLES           
docker-desktop   Ready    control-plane
```

✓ ¡Kubernetes corriendo!

### Si prefieres Minikube

```bash
# Instalar Minikube
brew install minikube

# Iniciar clúster
minikube start

# Verificar
kubectl get nodes

# Dashboard (opcional, muy útil)
minikube dashboard
```

---

## 🚀 Opción 2: Instalar en Linux

```bash
# Instalar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Instalar Minikube
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Iniciar
minikube start

# Verificar
kubectl get nodes
```

---

## 🚀 Opción 3: Instalar en Windows

**PowerShell (como Admin):**

```powershell
# Instalar chocolatey si no lo tienes
Set-ExecutionPolicy Bypass -Scope Process

# Instalar kubectl
choco install kubernetes-cli

# Instalar Minikube
choco install minikube

# Iniciar
minikube start

# Verificar
kubectl get nodes
```

---

## 📚 Conceptos Fundamentales

### 1. Pod

El **pod** es la unidad más pequeña en Kubernetes.

(Casi siempre = 1 contenedor por pod)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mi-primer-pod
spec:
  containers:
  - name: app
    image: nginx:latest
    ports:
    - containerPort: 80
```

**Crear:**
```bash
kubectl apply -f pod.yaml
```

**Ver:**
```bash
kubectl get pods
kubectl describe pod mi-primer-pod
kubectl logs mi-primer-pod
```

**Acceder:**
```bash
kubectl port-forward pod/mi-primer-pod 8080:80
# Abre http://localhost:8080
```

---

### 2. Deployment

Un **Deployment** es superior a un Pod porque permite:
- Replicación (múltiples copias)
- Actualizaciones sin downtime
- Auto-recuperación

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mi-app
spec:
  replicas: 3  # 3 copias
  selector:
    matchLabels:
      app: mi-app
  template:
    metadata:
      labels:
        app: mi-app
    spec:
      containers:
      - name: app
        image: nginx:latest
        ports:
        - containerPort: 80
```

**Crear:**
```bash
kubectl apply -f deployment.yaml
```

**Ver:**
```bash
kubectl get deployments
kubectl get pods  # Verás 3 pods
```

**Actualizar:**
```bash
# Cambiar imagen
kubectl set image deployment/mi-app app=nginx:1.21
# O editar el archivo y: kubectl apply -f deployment.yaml
```

---

### 3. Service

Un **Service** expone tu aplicación dentro o fuera del clúster.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mi-app-service
spec:
  selector:
    app: mi-app  # Conecta con pods que tengan esta etiqueta
  ports:
  - protocol: TCP
    port: 80        # Puerto del servicio
    targetPort: 80  # Puerto del pod
  type: LoadBalancer  # Expone externamente (localhost)
```

**Tipos de Services:**

```
ClusterIP (default):
├─ Solo accesible dentro del clúster
├─ IP interna única
└─ Para comunicación interna

NodePort:
├─ Expone en puerto del nodo
├─ Puerto 30000-32767
└─ Acceso externo básico

LoadBalancer:
├─ Expone con balanceador
├─ IP externa (en la nube)
└─ Recomendado para producción
```

**Crear:**
```bash
kubectl apply -f service.yaml
```

**Ver:**
```bash
kubectl get services
kubectl describe service mi-app-service
```

**Acceder:**
```bash
kubectl port-forward service/mi-app-service 8080:80
# Abre http://localhost:8080
```

---

### 4. Labels y Selectors

**Labels** = Etiquetas para identificar recursos

```yaml
metadata:
  labels:
    app: mi-app
    environment: production
    version: 1.0
```

**Selectors** = Criterios para seleccionar recursos

```yaml
selector:
  app: mi-app  # Selecciona pods con label app=mi-app
```

**Comandos:**

```bash
# Ver todos los pods con etiqueta
kubectl get pods -l app=mi-app

# Ver todos en producción
kubectl get pods -l environment=production

# Múltiples etiquetas
kubectl get pods -l app=mi-app,environment=production
```

---

### 5. Namespaces

**Namespace** = Separación lógica de recursos

```bash
# Ver namespaces
kubectl get namespaces

# Crear namespace
kubectl create namespace mi-proyecto

# Usar namespace
kubectl apply -f deployment.yaml -n mi-proyecto

# Ver recursos en namespace
kubectl get pods -n mi-proyecto
```

---

## 🎯 Tu Primer Despliegue

Vamos a desplegar Nginx (un servidor web) con 3 replicas.

**deployment.yaml:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
```

**service.yaml:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

**Desplegar:**

```bash
# Aplicar deployment
kubectl apply -f deployment.yaml

# Aplicar service
kubectl apply -f service.yaml

# Ver estado
kubectl get deployments
kubectl get pods
kubectl get services

# Port-forward
kubectl port-forward service/nginx-service 8080:80

# Abre navegador: http://localhost:8080
```

---

## 📚 Comandos Esenciales

```bash
# Ver recursos
kubectl get pods
kubectl get deployments
kubectl get services
kubectl get nodes

# Describir
kubectl describe pod <pod-name>
kubectl describe deployment <deployment-name>

# Logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>  # Seguir logs

# Acceso
kubectl exec -it <pod-name> -- bash  # Bash dentro del pod
kubectl port-forward pod/<pod-name> 8080:80

# Editar
kubectl edit deployment <deployment-name>

# Eliminar
kubectl delete pod <pod-name>
kubectl delete deployment <deployment-name>
kubectl delete service <service-name>

# Escalar
kubectl scale deployment <deployment-name> --replicas=5

# Rollout
kubectl rollout status deployment/<deployment-name>
kubectl rollout history deployment/<deployment-name>
kubectl rollout undo deployment/<deployment-name>
```

---

## 🎓 ConfigMaps y Secrets

### ConfigMap (configuración)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mi-config
data:
  DATABASE_HOST: localhost
  DATABASE_PORT: "5432"
  APP_MODE: production
```

**Usar en Deployment:**

```yaml
spec:
  containers:
  - name: app
    image: mi-app:1.0
    envFrom:
    - configMapRef:
        name: mi-config
```

### Secret (datos sensibles)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mi-secret
type: Opaque
data:
  DATABASE_PASSWORD: cGFzc3dvcmQx  # base64 encoded
  API_KEY: bXlhcGlrZXk=
```

```bash
# Crear desde línea de comandos
kubectl create secret generic mi-secret \
  --from-literal=DATABASE_PASSWORD=password123 \
  --from-literal=API_KEY=myapikey
```

---

## ✅ Checklist de Dominio

- [ ] Kubernetes instalado en tu máquina
- [ ] kubectl funcionando
- [ ] Entiendes qué es un Pod
- [ ] Entiendes qué es un Deployment
- [ ] Entiendes qué es un Service
- [ ] Creaste tu primer Deployment
- [ ] Exponiste un servicio
- [ ] Escalaste un Deployment
- [ ] Usaste Labels
- [ ] Creaste un ConfigMap
- [ ] Puedes explicar la diferencia entre Pod y Deployment

---

## 🚀 Próximo Paso

**Opción A: Aprofundiza en Kubernetes**
→ Ve a [`04_kubernetes_intermedio`](../04_kubernetes_intermedio)

**Opción B: Haz ejercicios prácticos**
→ Ve a [`05_ejercicios_practicos`](../05_ejercicios_practicos)

---

## 📚 Recursos

- **Documentación oficial**: https://kubernetes.io/docs
- **kubectl Cheat Sheet**: https://kubernetes.io/docs/reference/kubectl/cheatsheet
- **Play with Kubernetes**: https://www.play-with-k8s.com
- **Minikube Docs**: https://minikube.sigs.k8s.io

---

**Tiempo estimado: 10-12 horas**

¡Enhorabuena, ahora entiendes Kubernetes!
