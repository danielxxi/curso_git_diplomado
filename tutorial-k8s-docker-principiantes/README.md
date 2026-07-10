# Tutorial Completo Docker y Kubernetes para Principiantes
## Aprende desde cero - Paso a paso en Español Latino

¡Bienvenido! Este es un tutorial completo y progresivo para aprender **Docker y Kubernetes** desde cero. No necesitas experiencia previa. 

---

## 📚 Estructura del Tutorial

### **Nivel 0: Conceptos Básicos** 
**Duración estimada: 2-3 horas**

Aprenderás qué son Docker y Kubernetes sin necesidad de instalar nada aún.

```
00_conceptos_basicos/
├── 01_que_es_docker.md           # ¿Qué es Docker? Conceptos fundamentales
├── 02_que_es_kubernetes.md       # ¿Qué es Kubernetes? Introducción
├── 03_diferencias_vm_docker.md   # ¿Por qué Docker es mejor que VMs?
├── 04_casos_uso_reales.md        # Casos de uso en empresas
└── 05_roadmap_completo.md        # Mapa de ruta de aprendizaje
```

---

### **Nivel 1: Docker Básico** 
**Duración estimada: 8-10 horas**

Instalación, conceptos fundamentales y primeros pasos con Docker.

```
01_docker_basico/
├── 01_instalacion_macos.md       # Paso a paso: Docker Desktop en macOS
├── 02_instalacion_linux.md       # Paso a paso: Docker en Linux
├── 03_instalacion_windows.md     # Paso a paso: Docker en Windows
├── 04_conceptos_docker.md        # Imágenes, contenedores, registros
├── 05_primer_contenedor.md       # Tu primer "Hola Docker"
├── 06_dockerfile_basico.md       # Crear tu propia imagen
├── 07_volumenes.md               # Persistencia de datos
├── 08_redes_docker.md            # Comunicación entre contenedores
├── 09_docker_compose_intro.md    # Múltiples contenedores juntos
└── 10_ejercicios_nivel1.md       # Ejercicios prácticos
```

---

### **Nivel 2: Docker Intermedio**
**Duración estimada: 8-10 horas**

Conceptos avanzados, optimización y buenas prácticas.

```
02_docker_intermedio/
├── 01_optimization_imagenes.md   # Reducir tamaño de imágenes
├── 02_multistage_builds.md       # Construcción multi-etapa
├── 03_docker_networking.md       # Redes avanzadas
├── 04_registros_privados.md      # Docker Hub, registros privados
├── 05_seguridad_docker.md        # Mejores prácticas de seguridad
├── 06_docker_compose_avanzado.md # Compose con variables, overlays
├── 07_dockerfile_best_practices.md # Buenas prácticas
├── 08_health_checks.md           # Verificar salud de contenedores
├── 09_logs_debugging.md          # Logging y troubleshooting
└── 10_ejercicios_nivel2.md       # Ejercicios avanzados
```

---

### **Nivel 3: Kubernetes Básico**
**Duración estimada: 10-12 horas**

Primeros pasos en Kubernetes, conceptos fundamentales.

```
03_kubernetes_basico/
├── 01_instalacion_k8s.md         # Instalar Kubernetes local (minikube/Docker Desktop)
├── 02_conceptos_k8s.md           # Pods, Deployments, Services, Namespaces
├── 03_kubectl_basico.md          # Comandos kubectl esenciales
├── 04_pods_basicos.md            # Crear y gestionar pods
├── 05_deployments.md             # Deployments: replicación y actualizaciones
├── 06_services.md                # Exponiendo aplicaciones (ClusterIP, NodePort, LoadBalancer)
├── 07_labels_selectors.md        # Etiquetas y selectores
├── 08_namespaces.md              # Separación lógica de recursos
├── 09_volumenes_k8s.md           # Almacenamiento persistente
├── 10_configmaps_secrets.md      # Configuración y datos sensibles
├── 11_primeros_pasos.md          # Tu primer despliegue en K8s
└── 12_ejercicios_nivel3.md       # Ejercicios prácticos
```

---

### **Nivel 4: Kubernetes Intermedio**
**Duración estimada: 10-12 horas**

Conceptos avanzados, monitoreo, escalado, seguridad.

```
04_kubernetes_intermedio/
├── 01_replicasets_daemonsets.md  # Otros tipos de controladores
├── 02_statefulsets.md            # Aplicaciones stateful
├── 03_ingress.md                 # Enrutamiento HTTP/HTTPS
├── 04_hpa.md                     # Auto-escalado horizontal
├── 05_rbac.md                    # Control de acceso basado en roles
├── 06_network_policies.md        # Políticas de red
├── 07_logging_monitoring.md      # Logs y métricas
├── 08_helm_basics.md             # Gestión de aplicaciones con Helm
├── 09_troubleshooting.md         # Debugging y solución de problemas
├── 10_security_best_practices.md # Seguridad en Kubernetes
└── 11_ejercicios_nivel4.md       # Ejercicios avanzados
```

---

### **Nivel 5: Ejercicios Prácticos**
**Duración variable según ejercicio**

Proyectos integrados aplicando todo lo aprendido.

```
05_ejercicios_practicos/
├── 01_todo_app/                  # App Todo simple en Docker y K8s
├── 02_blog_wordpress/            # WordPress con base de datos
├── 03_api_rest_python/           # API REST con FastAPI
├── 04_microservicios/            # Arquitectura de microservicios
├── 05_ci_cd_basics/              # Pipeline CI/CD básico
└── EJERCICIOS_RESUELTOS.md       # Soluciones
```

---

### **Nivel 6: Proyectos Reales**
**Duración variable según proyecto**

Proyectos para producción y portafolio.

```
06_proyectos_reales/
├── 01_ecommerce/                 # E-commerce completo
├── 02_saas_app/                  # Aplicación SaaS
├── 03_data_pipeline/             # Pipeline de datos
├── 04_monitoreo_produccion/      # Monitoreo y alertas
└── PROYECTOS_COMPLETOS.md        # Descripción completa
```

---

## 🚀 Cómo usar este Tutorial

### **Opción 1: Aprendizaje Secuencial (Recomendado para principiantes)**

```bash
# Semana 1-2: Conceptos básicos
Leer: 00_conceptos_basicos/

# Semana 3-4: Docker desde cero
Aprender: 01_docker_basico/
Hacer: Ejercicios de nivel 1

# Semana 5-6: Docker avanzado
Aprender: 02_docker_intermedio/
Hacer: Ejercicios de nivel 2

# Semana 7-9: Kubernetes básico
Aprender: 03_kubernetes_basico/
Hacer: Ejercicios de nivel 3

# Semana 10-11: Kubernetes avanzado
Aprender: 04_kubernetes_intermedio/
Hacer: Ejercicios de nivel 4

# Semana 12+: Proyectos reales
Ejecutar: 05_ejercicios_practicos/ y 06_proyectos_reales/
```

### **Opción 2: Aprendizaje Acelerado (3-4 semanas)**

```bash
# Día 1-2: Docker conceptos + instalación
00_conceptos_basicos/ + 01_docker_basico/01-03

# Día 3-4: Docker práctico
01_docker_basico/04-10 + ejercicios

# Día 5-6: Kubernetes conceptos
03_kubernetes_basico/01-03

# Día 7-10: Kubernetes práctico
03_kubernetes_basico/04-12 + ejercicios

# Día 11-14: Ejercicios integrados
05_ejercicios_practicos/
```

### **Opción 3: Profundidad selectiva**

Elige el tema que necesitas y profundiza:
- Solo Docker → 00 + 01 + 02
- Solo Kubernetes → 00 + 03 + 04
- Full Stack → 00 + 01 + 02 + 03 + 04

---

## 📋 Requisitos Previos

### Conocimientos
- Conceptos básicos de terminal/línea de comandos
- Noción de cómo funcionan los servidores
- Curiosidad y ganas de aprender 😊

### Software
- **macOS**: Docker Desktop o instalación manual
- **Linux**: Docker + kubectl
- **Windows**: Docker Desktop (WSL2) o Hyper-V

### Tiempo estimado total
- **Nivel principiante** → 40-50 horas
- **Nivel intermedio** → 80-100 horas
- **Proyectos reales** → 20+ horas

---

## 💡 Metodología

### Cada lección incluye:

1. **Conceptos teóricos** - Explicación clara y simple
2. **Ejemplos prácticos** - Código listo para copiar/pegar
3. **Paso a paso** - Instrucciones detalladas
4. **Ejercicios** - Refuerza lo aprendido
5. **Soluciones** - Verificar tu trabajo
6. **Troubleshooting** - Solución de problemas comunes

### Material incluido:

- 📝 Documentos Markdown con explicaciones
- 🐳 Dockerfiles listos para usar
- ☸️ Manifiestos Kubernetes
- 🐍 Scripts de ejemplo
- 📊 Notebooks Jupyter interactivos
- 🎯 Ejercicios con soluciones
- 📚 Referencias y recursos

---

## 🎯 Objetivos de Aprendizaje

### Después del Nivel 1 (Docker Básico)
- ✅ Entender qué es Docker y por qué es importante
- ✅ Instalar Docker en tu máquina
- ✅ Crear y ejecutar contenedores
- ✅ Crear tus propias imágenes con Dockerfile
- ✅ Entender volumenes y redes en Docker

### Después del Nivel 2 (Docker Intermedio)
- ✅ Optimizar imágenes Docker
- ✅ Usar Docker Compose para múltiples servicios
- ✅ Implementar seguridad en contenedores
- ✅ Subir imágenes a registros

### Después del Nivel 3 (Kubernetes Básico)
- ✅ Instalar Kubernetes local
- ✅ Crear y gestionar pods
- ✅ Usar Deployments para replicación
- ✅ Exponer aplicaciones con Services
- ✅ Usar ConfigMaps y Secrets

### Después del Nivel 4 (Kubernetes Intermedio)
- ✅ Implementar auto-escalado
- ✅ Configurar control de acceso (RBAC)
- ✅ Monitorear aplicaciones
- ✅ Usar Helm para gestionar apps
- ✅ Troubleshooting avanzado

### Después de Ejercicios (Nivel 5)
- ✅ Construir aplicaciones multi-contenedor
- ✅ Desplegar en Kubernetes
- ✅ Implementar pipelines CI/CD
- ✅ Entender arquitecturas de microservicios

---

## 📖 Cómo Leer el Contenido

### Formato de archivos

**Markdown (.md)**: Explicaciones y teoría
```
# Título principal (concepto)
## Subtítulo (detalles)

Explicación en párrafos...

### Código ejemplo
```bash
# Comando a ejecutar
```

✓ Explicación de qué hace
```

**Dockerfiles**: Ejemplos prácticos
```dockerfile
FROM image:version
# Explicación de cada línea
...
```

**YAML (Kubernetes)**: Manifiestos
```yaml
# Explicación de cada sección
apiVersion: v1
...
```

---

## 🛠️ Herramientas Necesarias

| Herramienta | Instalación | Uso |
|-------------|------------|-----|
| Docker | 01_docker_basico/instalacion_*.md | Crear/ejecutar contenedores |
| kubectl | 03_kubernetes_basico/instalacion_k8s.md | Gestionar Kubernetes |
| Minikube (opcional) | 03_kubernetes_basico/instalacion_k8s.md | K8s local alternativo |
| Docker Compose | Incluido en Docker Desktop | Múltiples contenedores |
| git | Tu OS | Control de versiones |

---

## 🤝 Contribuir

¿Encontraste un error? ¿Tienes una sugerencia?

```bash
# Crear rama
git checkout -b mejora/mi-sugerencia

# Hacer cambios
# Commit
git add .
git commit -m "docs: mejorar explicación de X"

# Push y PR
git push origin mejora/mi-sugerencia
```

---

## 📞 Soporte

Si tienes dudas:

1. **Revisa Troubleshooting** en cada sección
2. **Busca tu error** en Google/ChatGPT
3. **Documentación oficial**:
   - Docker: https://docs.docker.com
   - Kubernetes: https://kubernetes.io/docs
   - Stack Overflow: https://stackoverflow.com/questions/tagged/docker+kubernetes

---

## 📅 Estimación de Tiempo

| Nivel | Duración | Horas |
|-------|----------|-------|
| Conceptos Básicos | 2-3 horas | 2-3 |
| Docker Básico | 1-2 semanas | 8-10 |
| Docker Intermedio | 1-2 semanas | 8-10 |
| Kubernetes Básico | 1-2 semanas | 10-12 |
| Kubernetes Intermedio | 1-2 semanas | 10-12 |
| **Total aprendizaje** | **5-9 semanas** | **40-50** |
| Ejercicios prácticos | Variable | 20+ |
| Proyectos reales | Variable | 30+ |

---

## ✨ Características Especiales

🌍 **Español Latino** - Todo en español claro y accesible
👶 **Principiantes** - Explicaciones simples, sin tecnicismos
🔄 **Progresivo** - De lo fácil a lo difícil
🎯 **Práctico** - Aprende haciendo
🐛 **Troubleshooting** - Soluciones a problemas comunes
📚 **Exhaustivo** - Desde instalación hasta producción
🎓 **Certificable** - Puedes armarte un portafolio

---

## 🎓 Licencia

Este tutorial es libre para uso personal y educativo.

---

## 🚀 ¡Empecemos!

### Siguiente paso según tu nivel:

**Si eres total principiante:**
→ Inicia con [`00_conceptos_basicos/README.md`](./00_conceptos_basicos/README.md)

**Si entiendes conceptos básicos:**
→ Inicia con [`01_docker_basico/01_instalacion_macos.md`](./01_docker_basico/01_instalacion_macos.md)

**Si tienes experiencia con Docker:**
→ Inicia con [`03_kubernetes_basico/01_instalacion_k8s.md`](./03_kubernetes_basico/01_instalacion_k8s.md)

---

**Última actualización**: Julio 2026
**Versión**: 1.0
**Estado**: ✅ Completo y actualizado
