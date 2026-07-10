# Módulo 4: Kubernetes Intermedio - Operaciones avanzadas
## Escalado, monitoreo, seguridad y producción

---

## 📋 Contenido de este módulo

Técnicas avanzadas para Kubernetes en producción.

### 📑 Lecciones:

1. **ReplicaSets y DaemonSets** (1 hora) - Otros controladores
2. **StatefulSets** (1-2 horas) - Aplicaciones stateful (BD, etc)
3. **Ingress** (1-2 horas) - HTTP/HTTPS avanzado
4. **HorizontalPodAutoscaler (HPA)** (1 hora) - Auto-escalado
5. **RBAC (Control de Acceso)** (1-2 horas) - Seguridad y permisos
6. **Network Policies** (1 hora) - Firewall de pods
7. **Logging y Monitoreo** (1-2 horas) - Observabilidad
8. **Helm** (1-2 horas) - Gestor de paquetes
9. **Troubleshooting** (1 hora) - Debugging avanzado
10. **Security Best Practices** (1 hora) - Seguridad en producción

---

## 🎯 Objetivo

Después de este módulo:
- ✅ StatefulSets para aplicaciones con estado
- ✅ Ingress para HTTP/HTTPS
- ✅ Auto-escalado automático
- ✅ Control de acceso (RBAC)
- ✅ Monitoreo y observabilidad
- ✅ Helm para gestión

---

## ⏱️ Tiempo total: 10-12 horas

---

## 📚 Lección 1: StatefulSets

### ¿Cuándo usar StatefulSets?

**Deployment** = aplicaciones stateless (sin estado)
```
Pod 1: Mi app ↔ Base de datos externa
Pod 2: Mi app ↔ Base de datos externa
Pod 3: Mi app ↔ Base de datos externa
(cualquiera puede manejar cualquier request)
```

**StatefulSet** = aplicaciones stateful (con estado)
```
Pod 0: mongodb-0 (primer master) - almacena datos
Pod 1: mongodb-1 (secondary) - almacena datos
Pod 2: mongodb-2 (secondary) - almacena datos
(cada uno es único e irreemplazable)
```

### Ejemplo: MongoDB Replicaset

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongodb-config
data:
  mongodb.conf: |
    replication:
      replSetName: rs0

---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
spec:
  serviceName: mongodb  # Importante para StatefulSet
  replicas: 3
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      containers:
      - name: mongodb
        image: mongo:6.0
        ports:
        - containerPort: 27017
        volumeMounts:
        - name: data
          mountPath: /data/db
        - name: config
          mountPath: /etc/mongod.conf
      volumes:
      - name: config
        configMap:
          name: mongodb-config

  # Volumenes persistentes
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Gi

---
apiVersion: v1
kind: Service
metadata:
  name: mongodb
spec:
  clusterIP: None  # Headless service
  selector:
    app: mongodb
  ports:
  - port: 27017
    targetPort: 27017
```

**Características:**

```
- Pods nombrados: mongodb-0, mongodb-1, mongodb-2
- Persistencia: Cada pod tiene su propio PVC
- Identidad estable: Siempre mismo nombre y volumen
- DNS estable: mongodb-0.mongodb.default.svc.cluster.local
- Actualización ordenada: One by one
```

---

## 📚 Lección 2: Ingress

### El Problema

Quieres que usuarios accedan a tu app con un dominio, no puerto.

```
Sin Ingress:
http://mi-server.com:30000  ← Feo, no funciona en navegador

Con Ingress:
http://mi-app.com           ← Bonito, profesional
https://mi-app.com          ← Con SSL
```

### Ejemplo Básico

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mi-app-ingress
spec:
  rules:
  - host: mi-app.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mi-app-service
            port:
              number: 80
```

### Con HTTPS (TLS)

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mi-app-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - mi-app.com
    secretName: mi-app-tls

  rules:
  - host: mi-app.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mi-app-service
            port:
              number: 80
```

### Múltiples servicios

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mi-ingress
spec:
  rules:
  # API
  - host: api.mi-app.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 5000

  # Frontend
  - host: www.mi-app.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend-service
            port:
              number: 3000

  # Admin
  - host: admin.mi-app.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: admin-service
            port:
              number: 8080
```

---

## 📚 Lección 3: HorizontalPodAutoscaler (HPA)

### ¿Qué es?

Añade/quita pods automáticamente según la carga.

```
Carga BAJA        MEDIA        ALTA
  ↓               ↓            ↓
 1 pod      →   3 pods    →  10 pods
 (90% CPU)      (50% CPU)    (60% CPU)
```

### Crear HPA

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: mi-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: mi-app

  minReplicas: 2
  maxReplicas: 10

  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70  # Escala si CPU > 70%

  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80  # Escala si memoria > 80%

  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
```

### Ver HPA

```bash
# Ver estado
kubectl get hpa

# Detalles
kubectl describe hpa mi-app-hpa

# Ver métricas
kubectl get hpa mi-app-hpa --watch
```

---

## 📚 Lección 4: RBAC (Control de Acceso)

### ¿Por qué?

En producción, no todos deben poder hacer todo.

```
Admin:          Puede crear, actualizar, eliminar
Developer:      Puede crear y ver
Viewer:         Solo puede ver (read-only)
```

### Componentes de RBAC

1. **ServiceAccount** - Identidad de un pod/usuario
2. **Role** - Permisos sobre recursos
3. **RoleBinding** - Conecta ServiceAccount con Role
4. **ClusterRole** - Permisos globales del cluster
5. **ClusterRoleBinding** - Para recursos globales

### Ejemplo: Developer con permisos limitados

```yaml
# 1. ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: developer

---
# 2. Role (permisos)
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer-role
rules:
# Puede ver deployments
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch"]

# Puede ver pods
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list", "watch", "logs"]

# Puede crear deployments (no eliminar)
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["create", "update", "patch"]

---
# 3. RoleBinding (conectar ServiceAccount + Role)
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developer-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: developer-role
subjects:
- kind: ServiceAccount
  name: developer
  namespace: default
```

### Ver permisos

```bash
# Ver roles
kubectl get roles

# Ver bindings
kubectl get rolebindings

# Ver que puede hacer un serviceaccount
kubectl auth can-i get pods --as=system:serviceaccount:default:developer
```

---

## 📚 Lección 5: Network Policies

### ¿Qué es?

Un "firewall" para el tráfico entre pods.

```
Por defecto: TODO pod puede hablar con TODO pod

Con Network Policy:
- Pod A ↔ Pod B (permitido)
- Pod A ↔ Pod C (bloqueado)
- Pod B ↔ C (bloqueado)
```

### Ejemplo: Aislamiento básico

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}  # Aplica a todos los pods
  policyTypes:
  - Ingress
  - Egress
```

Esto **bloquea todo tráfico** (muy restrictivo).

### Ejemplo: Permitir tráfico específico

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: mi-app-policy
spec:
  podSelector:
    matchLabels:
      app: mi-app

  policyTypes:
  - Ingress
  - Egress

  ingress:
  # Permitir desde frontend
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 5000

  egress:
  # Permitir hacia BD
  - to:
    - podSelector:
        matchLabels:
          app: db
    ports:
    - protocol: TCP
      port: 5432

  # Permitir DNS
  - to:
    - namespaceSelector: {}
    ports:
    - protocol: UDP
      port: 53
```

---

## 📚 Lección 6: Logging y Monitoreo

### Acceder a logs

```bash
# Logs de un pod
kubectl logs pod-name

# Logs de contenedor específico
kubectl logs pod-name -c container-name

# Últimas 100 líneas
kubectl logs pod-name --tail=100

# Seguir logs
kubectl logs -f pod-name

# Con timestamps
kubectl logs -t pod-name

# Todos los pods de un deployment
kubectl logs -l app=mi-app
```

### Eventos del cluster

```bash
# Ver eventos
kubectl get events

# Ver eventos de un namespace
kubectl get events -n kube-system

# Ver eventos detalladamente
kubectl describe node node-name
```

### Métricas

```bash
# Necesita metrics-server instalado
kubectl top nodes
kubectl top pods
kubectl top pods -n kube-system

# Ver consumo de pod específico
kubectl top pod pod-name
```

### Instalar stack de monitoreo

```yaml
# Prometheus + Grafana (opcional, avanzado)
# Requiere más configuración
# Documentación: https://prometheus.io/docs/prometheus/latest/installation/
```

---

## 📚 Lección 7: Helm

### ¿Qué es?

"npm" o "pip" pero para Kubernetes.

Instala paquetes complejos con un comando.

```bash
# Sin Helm: escribir 50 YAML files
# Con Helm:
helm install my-release bitnami/mysql
```

### Instalar Helm

```bash
# macOS
brew install helm

# Linux
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Verificar
helm version
```

### Usar un Chart

```bash
# Buscar charts
helm search repo mysql

# Ver detalles
helm show values bitnami/mysql

# Instalar
helm install my-mysql bitnami/mysql \
  --set auth.rootPassword=password \
  --set auth.database=mydb

# Ver instalados
helm list

# Actualizar
helm upgrade my-mysql bitnami/mysql \
  --set primary.persistence.size=20Gi

# Desinstalar
helm uninstall my-mysql
```

---

## 📚 Lección 8: Troubleshooting Avanzado

### Pod en estado "Pending"

```bash
kubectl describe pod pod-name

# Ver:
# - Recursos insuficientes (memory, CPU)
# - Imagen no encontrada
# - PVC sin disponible

# Soluciones:
kubectl delete pod pod-name  # Reintentar
kubectl logs -p pod-name    # Ver logs previos
```

### Pod en "CrashLoopBackOff"

```bash
# App se reinicia infinitamente

# Ver último log
kubectl logs pod-name --previous

# Ejecutar comando debug
kubectl run -it --image=busybox debug -- sh
```

### Node "NotReady"

```bash
# Node offline o con problemas

# Ver estado
kubectl describe node node-name

# Ver logs del kubelet
kubectl logs -n kube-system kubelet

# En el nodo:
systemctl status kubelet
```

---

## ✅ Checklist de Dominio

- [ ] Entiendes StatefulSets vs Deployments
- [ ] Puedes configurar Ingress
- [ ] Implementas auto-escalado (HPA)
- [ ] Usas RBAC para seguridad
- [ ] Entiendes Network Policies
- [ ] Accedes a logs y métricas
- [ ] Debugueas problemas avanzados

---

## 🚀 Próximo Paso

Ahora estás listo para:

**Opción A: Proyectos reales**
→ Ve a [`06_proyectos_reales`](../06_proyectos_reales)

**Opción B: Más ejercicios**
→ Ve a [`05_ejercicios_practicos`](../05_ejercicios_practicos)

---

**Tiempo estimado: 10-12 horas**

¡Ahora eres un experto en Kubernetes!
