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
├── README.md                 # Toda la teoría en una lección
```

---

### **Nivel 0.5: Instalación Completa** 
**Duración estimada: 45-60 minutos**

Instala Docker, Kubernetes y todas las herramientas en tu sistema operativo.

```
0.5_instalacion_completa/
├── README.md                 # Instalación paso a paso para macOS, Linux, Windows
```

---

### **Nivel 1: Docker Básico** 
**Duración estimada: 8-10 horas**

Instalación, conceptos fundamentales y primeros pasos con Docker.

```
01_docker_basico/
├── README.md                 # Paso a paso desde cero
```

---

### **Nivel 2: Docker Intermedio**
**Duración estimada: 8-10 horas**

Conceptos avanzados, optimización y buenas prácticas.

```
02_docker_intermedio/
├── README.md                 # Multi-stage, optimización, seguridad, best practices
```

---

### **Nivel 3: Kubernetes Básico**
**Duración estimada: 10-12 horas**

Primeros pasos en Kubernetes, conceptos fundamentales.

```
03_kubernetes_basico/
├── README.md                 # Instalación K8s, Pods, Deployments, Services
```

---

### **Nivel 4: Kubernetes Intermedio**
**Duración estimada: 10-12 horas**

Conceptos avanzados, monitoreo, escalado, seguridad.

```
04_kubernetes_intermedio/
├── README.md                 # StatefulSets, Ingress, HPA, RBAC, Monitoring, Helm
```

---

### **Nivel 5: Ejercicios Prácticos**
**Duración variable según ejercicio**

Proyectos integrados aplicando todo lo aprendido.

```
05_ejercicios_practicos/
├── README.md                 # 12 ejercicios progresivos (desde TODO app hasta Helm)
```

---

### **Nivel 6: Proyectos Reales**
**Duración variable según proyecto**

Proyectos para producción y portafolio.

```
06_proyectos_reales/
├── README.md                 # E-commerce, SaaS, Pipeline de datos, Microservicios
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

| Nivel | Tema | Duración | Horas |
|-------|------|----------|-------|
| 0 | Conceptos Básicos | 2-3 horas | 2-3 |
| 0.5 | Instalación Completa | 45-60 min | 1 |
| 1 | Docker Básico | 1-2 semanas | 8-10 |
| 2 | Docker Intermedio | 1-2 semanas | 8-10 |
| 3 | Kubernetes Básico | 1-2 semanas | 10-12 |
| 4 | Kubernetes Intermedio | 1-2 semanas | 10-12 |
| 5 | Ejercicios Prácticos | 2-3 semanas | 20+ |
| 6 | Proyectos Reales | 4-8 semanas | 40+ |
| **TOTAL LEARNING** | **Todos los módulos** | **10-16 semanas** | **60-80** |
| **+ Proyectos** | **Con proyectos** | **12-20 semanas** | **100-120** |

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

**Si eres TOTAL PRINCIPIANTE:**
→ Inicia con [`00_conceptos_basicos/README.md`](./00_conceptos_basicos/README.md)

**Si entiendes conceptos pero necesitas instalar:**
→ Inicia con [`0.5_instalacion_completa/README.md`](./0.5_instalacion_completa/README.md)

**Si tienes Docker pero no Kubernetes:**
→ Inicia con [`03_kubernetes_basico/README.md`](./03_kubernetes_basico/README.md)

**Si tienes experiencia y quieres profundizar:**
→ Inicia con [`02_docker_intermedio/README.md`](./02_docker_intermedio/README.md) o [`04_kubernetes_intermedio/README.md`](./04_kubernetes_intermedio/README.md)

---

**Última actualización**: Julio 2026
**Versión**: 1.0
**Estado**: ✅ Completo y actualizado
