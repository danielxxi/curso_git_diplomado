# 🐳 Tutorial Docker & Kubernetes ☸️

Tutorial completo paso a paso para aprender Docker y Kubernetes, con ejemplos funcionales y ejercicios interactivos.

## 📋 Contenido

- **PPTX**: Presentación con 25 diapositivas (tema Anthropic/Google)
- **PDF**: Guía paso a paso con comandos exactos a ejecutar
- **Ejemplos funcionales**: Dockerfile, app.py, kubernetes.yaml
- **Helper script**: Comandos simplificados para ejecutar el tutorial

## 🚀 Inicio rápido

### 1. Generar materiales (PPTX + PDF)

```bash
cd /Users/daniel/curso_git_dpl/curso_git_diplomado

# Opción A: Generar todo
bash run_tutorial.sh generate-all

# Opción B: Generar por separado
bash run_tutorial.sh generate-pptx
bash run_tutorial.sh generate-pdf
```

Esto crea:
- `doc/Tutorial_Docker_Kubernetes.pptx` (25 diapositivas)
- `doc/Tutorial_Docker_Kubernetes_Paso_a_Paso.pdf` (12 páginas)

### 2. Ejecutar ejemplo de Docker

```bash
# Construir imagen
bash run_tutorial.sh docker-build

# Ejecutar contenedor
bash run_tutorial.sh docker-run

# En navegador: http://localhost:8080
```

### 3. Ejecutar ejemplo de Kubernetes

```bash
# Desplegar en K8s
bash run_tutorial.sh k8s-deploy

# Port-forward (en otra terminal)
bash run_tutorial.sh k8s-port-forward

# En navegador: http://localhost:8080
```

## 📁 Estructura de archivos

```
src/docker_kubernetes_tutorial/
├── app.py                      # Aplicación Flask (página web)
├── kubernetes.yaml             # Manifiestos de Kubernetes
├── requirements.txt            # Dependencias Python
├── generate_tutorial.py        # Script generador PPTX
└── generate_tutorial_pdf.py    # Script generador PDF

Dockerfile                       # Receta para construir imagen Docker

run_tutorial.sh                 # Helper script con comandos útiles

doc/
├── Tutorial_Docker_Kubernetes.pptx              # Presentación
└── Tutorial_Docker_Kubernetes_Paso_a_Paso.pdf  # Guía paso a paso
```

## 📚 Contenido del tutorial

### PPTX (25 diapositivas)

1. **Introducción**
   - ¿Qué es Docker?
   - ¿Qué es Kubernetes?
   - Conceptos clave

2. **Instalación** (4 diapositivas)
   - macOS (Docker Desktop + Homebrew)
   - Linux (Ubuntu/Debian)
   - Windows (WSL2 + Hyper-V)

3. **Conceptos Docker** (2 diapositivas)
   - Imágenes vs Contenedores
   - Dockerfile
   - Registry

4. **Ejemplo Docker** (4 diapositivas)
   - Construir imagen
   - Ejecutar contenedor
   - Verificar estado
   - Limpiar recursos

5. **Conceptos Kubernetes** (2 diapositivas)
   - Cluster, Nodes, Pods
   - Deployments, Services
   - ConfigMap, Secrets

6. **Ejemplo Kubernetes** (5 diapositivas)
   - Instalar K8s local
   - Desplegar aplicación
   - Verificar pods
   - Acceder a aplicación
   - Escalar y monitoreo

7. **Mejores prácticas** (2 diapositivas)
   - Seguridad
   - Rendimiento
   - Observabilidad

8. **Troubleshooting + Recursos** (2 diapositivas)

### PDF (12 páginas)

Mismos tópicos que PPTX pero con:
- ✅ Comandos **exactos** a ejecutar en macOS
- ✅ Explicación **línea a línea** de cada comando
- ✅ Expected output (qué deberías ver)
- ✅ Troubleshooting detallado

## 🎯 Requisitos

### Mínimos para Docker
- macOS 10.14+ / Linux / Windows 10 Pro+
- 4GB RAM disponible
- Conexión a internet

### Mínimos para Kubernetes
- Docker Desktop con Kubernetes habilitado, O Minikube
- 2GB RAM disponible (además de Docker)

### Software necesario

**Instalado en tu sistema:**
- Docker / Docker Desktop
- `kubectl` (incluido en Docker Desktop)
- Terminal (macOS: Terminal.app o iTerm2)

**En Python (auto-instalado por scripts):**
- Flask (para app web)
- python-pptx (para PPTX)
- fpdf2 (para PDF)

## 📋 Comandos útiles

### Ver ayuda del script
```bash
bash run_tutorial.sh
```

### Docker
```bash
bash run_tutorial.sh docker-build      # Construir imagen
bash run_tutorial.sh docker-run        # Ejecutar contenedor
bash run_tutorial.sh docker-logs       # Ver logs
bash run_tutorial.sh docker-stop       # Detener contenedor
```

### Kubernetes
```bash
bash run_tutorial.sh k8s-deploy        # Desplegar
bash run_tutorial.sh k8s-status        # Ver estado
bash run_tutorial.sh k8s-port-forward  # Acceso web
bash run_tutorial.sh k8s-scale 5       # Escalar a 5 pods
bash run_tutorial.sh k8s-logs          # Ver logs
bash run_tutorial.sh k8s-delete        # Limpiar todo
```

## 🌐 Aplicación de ejemplo

**Tecnología**: Python + Flask

**Características**:
- Interfaz moderna (HTML/CSS)
- Página de bienvenida con información de estado
- Health checks para K8s
- Responsive design

**Acceso**: http://localhost:8080

**Información mostrada**:
- Estado: "✓ Contenedor ejecutándose correctamente"
- Stack: Docker, Kubernetes, Python, Flask
- Instrucciones para próximos pasos

## 🔍 Verificación paso a paso

### Después de `docker run`:
```
✓ En navegador: http://localhost:8080
✓ Ves página web hermosa
✓ Status: verde "Contenedor ejecutándose"
✓ Presiona Ctrl+C para detener
```

### Después de `k8s-deploy`:
```
✓ 3 pods en estado Running
✓ Service en estado LoadBalancer (local)
✓ HPA listo para auto-escalado
✓ kubectl get pods muestra 3 instancias
```

### Después de `k8s-port-forward`:
```
✓ Output: "Forwarding from 127.0.0.1:8080 -> 8080"
✓ En navegador: http://localhost:8080
✓ MISMA página web que Docker
✓ Pero orquestada en K8s con 3 replicas
```

## 🐛 Solución de problemas

### "docker: command not found"
```bash
# macOS
open /Applications/Docker.app

# Linux
sudo systemctl start docker

# Windows
Abre Docker Desktop desde menú Inicio
```

### "Port 8080 already in use"
```bash
# Cambiar puerto
docker run -p 9000:5000 mi-app-web:latest
```

### "kubectl: command not found"
```bash
# Instalar kubectl (si no lo tienes)
brew install kubectl  # macOS
```

### Pods en estado "Pending"
```bash
# Ver error detallado
kubectl describe pod <pod-name> -n docker-kubernetes-tutorial

# Verificar que imagen existe
docker images | grep mi-app-web
```

## 📖 Próximos pasos

Después de completar este tutorial:

1. **Docker avanzado**
   - Multi-stage builds
   - Docker Compose
   - Registry privado

2. **Kubernetes avanzado**
   - Ingress controllers
   - StatefulSets
   - Operators

3. **Producción**
   - Desplegar en AWS/Azure/GCP
   - Implementar CI/CD
   - Helm charts
   - GitOps

## 📚 Recursos externos

- [Docker Docs](https://docs.docker.com)
- [Kubernetes Docs](https://kubernetes.io/docs)
- [Play with Kubernetes](https://www.play-with-k8s.com)
- [Docker Hub](https://hub.docker.com)

## 🎓 Temas cubiertos

✅ Containerización con Docker  
✅ Orquestación con Kubernetes  
✅ Instalación en múltiples SO  
✅ Ejemplos funcionales  
✅ Escalado automático  
✅ Monitoreo y logs  
✅ Solución de problemas  
✅ Mejores prácticas  
✅ Seguridad  
✅ Rendimiento  

## 📄 Licencia

Tutorial educativo - Libre para uso personal y educativo

---

**Creado**: Julio 2026  
**Tema**: Anthropic/Google (colores modernos, diseño limpio)  
**Formato**: PPTX + PDF + Ejemplos funcionales
