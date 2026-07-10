# Módulo 0.5: Instalación Completa - Tu Primer Setup
## Guía detallada para cada sistema operativo

---

## 🎯 Objetivo de este módulo

Instalar Docker, Kubernetes y todas las herramientas necesarias para completar el tutorial, sin que nada se quede sin funcionar.

---

## 📋 Herramientas a instalar

| Herramienta | Necesidad | Uso |
|------------|----------|-----|
| Docker | OBLIGATORIO | Crear y ejecutar contenedores |
| Docker Compose | Incluido en Docker | Múltiples contenedores |
| kubectl | OBLIGATORIO para K8s | Gestionar Kubernetes |
| Minikube | OPCIONAL (alternativa) | K8s local alternativo |
| git | Recomendado | Clonar el tutorial |
| Navegador | OBLIGATORIO | Probar aplicaciones |

---

## 🍎 Instalación en macOS

### Opción A: Docker Desktop (RECOMENDADO - Más fácil)

**Paso 1: Descarga Docker Desktop**

1. Ve a: https://www.docker.com/products/docker-desktop
2. Haz clic en "Download for Mac"
3. Elige tu procesador:
   - **Apple Silicon (M1, M2, M3)**: Descargar "Apple Silicon"
   - **Intel**: Descargar "Intel Chip"

**Paso 2: Instala**

1. Abre el archivo `.dmg` que descargaste
2. Arrastra el icono "Docker.app" a la carpeta "Applications"
3. Espera (1-2 minutos)
4. Ve a Applications
5. Doble-clic en "Docker.app"
6. Ingresa tu contraseña macOS cuando te lo pida
7. Espera a que Docker inicie (verás el icono en la barra superior)

**Paso 3: Verifica la instalación**

Abre Terminal y ejecuta:

```bash
docker --version
docker run hello-world
```

**Deberías ver:**
```
Docker version 24.0.x, build xxxxx

Hello from Docker!
This message shows that your installation appears to be working correctly.
```

✓ **¡Docker instalado en macOS!**

**Bonus: Habilitar Kubernetes (en Docker Desktop)**

1. Docker Desktop → Settings (icono de rueda)
2. Busca "Kubernetes" en el menú izquierdo
3. Marca el checkbox "Enable Kubernetes"
4. Haz clic en "Apply & Restart"
5. Espera 2-5 minutos

**Verifica:**
```bash
kubectl version --client
kubectl get nodes
```

Deberías ver:
```
NAME             STATUS   ROLES           
docker-desktop   Ready    control-plane
```

✓ **¡Kubernetes habilitado!**

---

### Opción B: Instalación manual (Más control)

**Solo si prefieres no usar Docker Desktop**

```bash
# Instalar Docker con Homebrew
brew install docker

# Instalar Docker Compose
brew install docker-compose

# Instalar kubectl
brew install kubectl

# Instalar Minikube
brew install minikube

# Iniciar Minikube
minikube start

# Verificar
docker --version
kubectl version --client
```

---

## 🐧 Instalación en Linux (Ubuntu/Debian)

### Paso 1: Actualizar paquetes

```bash
sudo apt update
sudo apt upgrade -y
```

### Paso 2: Instalar Docker

```bash
# Descargar script de instalación
curl -fsSL https://get.docker.com -o get-docker.sh

# Ejecutar instalación
sudo sh get-docker.sh

# Verificar
docker --version
```

### Paso 3: Usar Docker sin sudo

```bash
# Agregar tu usuario al grupo docker
sudo usermod -aG docker $USER

# Aplicar cambios (elige UNA opción):

# Opción A: Reiniciar sesión
# Cierra sesión y abre terminal nuevamente

# Opción B: Comando rápido
newgrp docker

# Opción C: Reiniciar
sudo reboot

# Verificar que funciona sin sudo
docker run hello-world
```

### Paso 4: Instalar Docker Compose

```bash
# Descargar última versión
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Hacer ejecutable
sudo chmod +x /usr/local/bin/docker-compose

# Verificar
docker-compose --version
```

### Paso 5: Instalar kubectl

```bash
# Descargar kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Hacer ejecutable
chmod +x kubectl

# Instalar
sudo mv kubectl /usr/local/bin/

# Verificar
kubectl version --client
```

### Paso 6: Instalar Minikube

```bash
# Descargar
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64

# Instalar
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Iniciar
minikube start

# Verificar
kubectl get nodes
```

✓ **¡Todo instalado en Linux!**

---

## 🪟 Instalación en Windows

### Requisitos previos

Windows 10/11 Pro, Enterprise o Education (NO Home)

### Opción A: Docker Desktop (RECOMENDADO)

**Paso 1: Habilitar WSL2 (Windows Subsystem for Linux)**

Abre PowerShell **como Administrador** y ejecuta:

```powershell
# Habilitar WSL
wsl --install

# Esto instalará Ubuntu también
```

**Paso 2: Reiniciar**

Windows te pedirá que reinicies. **Reinicia ahora.**

**Paso 3: Descargar Docker Desktop**

1. Ve a: https://www.docker.com/products/docker-desktop
2. Descarga "Docker Desktop for Windows"
3. Ejecuta el instalador
4. Sigue los pasos (déjalo con opciones por defecto)
5. Marca "Use WSL 2 instead of Hyper-V"
6. Reinicia cuando te lo pida

**Paso 4: Abre PowerShell y verifica**

```powershell
docker --version
docker run hello-world
```

**Deberías ver:**
```
Docker version 24.0.x, build xxxxx

Hello from Docker!
```

✓ **¡Docker instalado en Windows!**

**Paso 5: Habilitar Kubernetes**

1. Docker Desktop → Settings (icono de rueda)
2. Kubernetes → Enable Kubernetes
3. Apply & Restart

Espera 5-10 minutos.

```powershell
kubectl version --client
kubectl get nodes
```

✓ **¡Kubernetes habilitado!**

---

### Opción B: Instalación manual con Chocolatey

```powershell
# Si no tienes Chocolatey, instálalo primero
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Reinicia PowerShell

# Instalar Docker
choco install docker-desktop

# Instalar kubectl
choco install kubernetes-cli

# Instalar Minikube
choco install minikube

# Verificar
docker --version
kubectl version --client
```

---

## ✅ Checklist de Verificación Post-Instalación

Ejecuta estos comandos para verificar que TODO funciona:

### Verificar Docker

```bash
# En cualquier SO

# 1. Versión
docker --version

# 2. Ejecutar contenedor de prueba
docker run --rm alpine echo "Docker funciona!"

# 3. Ver información
docker info

# 4. Ver imágenes
docker images

# 5. Ver contenedores
docker ps
```

**Resultado esperado:**
```
✓ Docker version 24.x.x
✓ Docker funciona!
✓ Sin errores
✓ Lista de imágenes
✓ Sin contenedores corriendo (normal si es nuevo)
```

### Verificar Kubernetes

```bash
# 1. Versión del cliente
kubectl version --client

# 2. Ver nodos del clúster
kubectl get nodes

# 3. Ver pods del sistema
kubectl get pods -n kube-system

# 4. Ver servicios
kubectl get services
```

**Resultado esperado:**
```
✓ kubectl version 1.x.x
✓ docker-desktop (o minikube) en estado Ready
✓ Varios pods del sistema corriendo
✓ kubernetes service visible
```

### Verificar Docker Compose

```bash
docker-compose --version
```

**Resultado esperado:**
```
Docker Compose version 2.x.x
```

---

## 🐛 Troubleshooting de Instalación

### "docker: command not found"

**Causa:** Docker no está en el PATH

**Soluciones:**

macOS:
```bash
# Reinicia Docker Desktop
# O reinstala
```

Linux:
```bash
# Verifica que está instalado
which docker
# Si no sale nada, reinstala: sudo sh get-docker.sh
```

Windows:
```powershell
# Abre PowerShell NUEVA (después de instalar Docker)
# O reinicia la máquina
```

---

### "Permission denied while trying to connect to Docker daemon"

**Causa:** No tienes permiso para usar Docker

**Solución Linux:**
```bash
# Agregar usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker

# Verifica
docker run hello-world
```

**Solución macOS/Windows:**
```bash
# Abre Docker Desktop
# Espera a que inicie completamente
# Intenta nuevamente
```

---

### "Kubernetes not available"

**Causa:** K8s no está habilitado

**Solución:**

macOS (Docker Desktop):
1. Settings → Kubernetes
2. Marca "Enable Kubernetes"
3. Espera 5 minutos

Linux/Windows (Minikube):
```bash
minikube start
```

---

### "WSL2 installation is incomplete" (Windows)

**Causa:** WSL2 no está completamente instalado

**Solución:**
```powershell
# Abre PowerShell como Admin
wsl --install
# Reinicia

# Si sigue sin funcionar:
wsl --update
wsl --set-default-version 2
```

---

## 🎓 Verificar que puedes seguir el tutorial

Ejecuta esto para estar 100% seguro:

```bash
# Test Docker
docker run -p 8080:80 --name test-nginx nginx

# En otra terminal, verifica que funciona
curl http://localhost:8080

# Deberías ver HTML de Nginx
# Presiona Ctrl+C en la primera terminal
docker rm test-nginx
```

```bash
# Test Kubernetes
kubectl create deployment test-app --image=nginx
kubectl expose deployment test-app --port=80 --target-port=80 --type=LoadBalancer
kubectl get services

# Port-forward
kubectl port-forward service/test-app 8080:80

# En otra terminal
curl http://localhost:8080

# Limpia
kubectl delete deployment test-app
kubectl delete service test-app
```

✓ **Si todo esto funciona, estás listo para empezar el tutorial**

---

## 📚 Próximo Paso

Ahora que tienes todo instalado:

1. **Lee el Módulo 0:** Conceptos básicos
2. **Empieza Módulo 1:** Docker Básico

```bash
cd tutorial-k8s-docker-principiantes
cat README.md                          # Para el índice
cat 00_conceptos_basicos/README.md     # Para conceptos
cat 01_docker_basico/README.md         # Para empezar
```

---

## 🆘 Si algo no funciona

**Antes de rendirte, intenta esto:**

1. **Reinicia Docker**
   - macOS: Docker → Quit
   - Linux: `sudo systemctl restart docker`
   - Windows: Reinicia el sistema

2. **Reinicia tu máquina**
   - A veces es lo único que funciona

3. **Busca el error en Google**
   - Copia el error exacto
   - Busca "docker error xyz"

4. **Consulta la documentación oficial**
   - Docker: https://docs.docker.com
   - Kubernetes: https://kubernetes.io/docs
   - Stack Overflow: https://stackoverflow.com

---

## ✨ Tips útiles

**Para macOS:**
```bash
# Abre Docker Desktop automáticamente
open -a Docker

# Ver logs de Docker
log stream --predicate 'eventMessage contains "Docker"' --level debug
```

**Para Linux:**
```bash
# Ver logs del daemon de Docker
sudo journalctl -u docker -f

# Ver información del sistema de Docker
docker system info

# Limpiar espacio
docker system prune
```

**Para Windows:**
```powershell
# Abrir WSL
wsl

# Ver versión de WSL
wsl --version

# Listar distribuciones de Linux disponibles
wsl --list --verbose
```

---

## ✅ Resumen de instalación

| SO | Docker | K8s | Comando clave |
|----|--------|-----|--------------|
| macOS | Docker Desktop | Incluido | `brew install docker` |
| Linux | APT/curl | Minikube | `curl -fsSL https://get.docker.com` |
| Windows | Docker Desktop | Incluido | PowerShell como Admin |

---

**Tiempo estimado:** 30-60 minutos (esperas incluidas)

**Cuando termines, estarás listo para aprender Docker y Kubernetes** 🚀

¿Necesitas ayuda con tu instalación específica?
