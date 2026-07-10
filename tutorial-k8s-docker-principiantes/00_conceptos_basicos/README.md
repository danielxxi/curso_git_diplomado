# Módulo 0: Conceptos Básicos - Docker y Kubernetes
## Para entender antes de instalar nada

---

## 📖 Contenido de este módulo

Este módulo te enseñará todo lo que necesitas entender ANTES de empezar a instalar Docker y Kubernetes. No necesitas instalar nada aún, solo aprender conceptos.

### 📑 Lecciones

1. **¿Qué es Docker?** (30 min) - Aprenderás qué es Docker y por qué lo necesitas
2. **¿Qué es Kubernetes?** (30 min) - Introducción a Kubernetes y cuándo lo usas
3. **Docker vs Máquinas Virtuales** (30 min) - Por qué Docker es superior
4. **Conceptos Fundamentales** (1 hora) - Imágenes, contenedores, registros
5. **Casos de Uso Reales** (30 min) - Dónde se usa en empresas
6. **Roadmap de Aprendizaje** (20 min) - Tu camino personalizado

---

## 🎯 Objetivo

Después de este módulo:
- ✅ Entenderás qué es Docker y Kubernetes
- ✅ Sabrás cuándo usar cada uno
- ✅ Comprenderás los conceptos fundamentales
- ✅ Estarás listo para instalar y aprender

---

## ⏱️ Tiempo total: 2-3 horas

Puedes completarlo en una mañana o distribuirlo en 2-3 días.

---

## 📚 Lecciones Detalladas

### Lección 1: ¿Qué es Docker? (30 minutos)

**¿Por qué existe Docker?**

Imagina que escribes una aplicación en tu macOS. Funciona perfectamente en tu máquina. Pero cuando la envías a producción (un servidor Linux en la nube), algo no funciona. ¿Por qué? Porque hay diferencias:

- Sistema operativo diferente
- Versiones de librerías diferentes
- Configuraciones diferentes
- Variables de entorno diferentes

**"Pero en mi máquina funciona perfectamente"** - La frase más común de los programadores 😅

**Docker resuelve esto con contenedores:**

Un **contenedor** es como un "portapaquete" que incluye:
- Tu código
- Todas las dependencias
- La configuración exacta
- El sistema operativo mínimo necesario

Cuando envías este portapaquete a otro servidor, **funciona exactamente igual** porque todo está dentro.

**Analogía real:**

```
Antes (sin Docker):
┌─────────────────────────────┐
│  Mi máquina (macOS)         │
│  └─ Mi App + Dependencias   │  ✓ Funciona
└─────────────────────────────┘

         ↓ Envío a producción ↓

┌─────────────────────────────┐
│  Servidor (Linux)           │
│  └─ Mi App + Dependencias   │  ✗ ¡No funciona!
└─────────────────────────────┘
                              (Versiones diferentes!)


Con Docker:
┌─────────────────────────────┐
│ 🐳 Contenedor Docker        │
│ ├─ Mi App                   │
│ ├─ Dependencias             │
│ ├─ Librerías                │
│ └─ Linux Mínimo             │
└─────────────────────────────┘
         ↓ El mismo contenedor ↓
┌─────────────────────────────┐     ┌─────────────────────────────┐
│  macOS                      │     │  Servidor Linux             │
│  └─ 🐳 Contenedor           │  →  │  └─ 🐳 Mismo contenedor     │
└─────────────────────────────┘     └─────────────────────────────┘
    ✓ Funciona                           ✓ Funciona igual
```

**Ventajas de Docker:**

1. **Consistencia**: Funciona igual en tu máquina, en testing y en producción
2. **Aislamiento**: Cada contenedor es independiente
3. **Ligero**: Usa menos recursos que máquinas virtuales
4. **Rápido**: Inicia en milisegundos
5. **Portabilidad**: Corre en cualquier máquina con Docker
6. **Reproducible**: Todos ejecutan exactamente lo mismo

---

### Lección 2: ¿Qué es Kubernetes? (30 minutos)

**Primero, ¿cuándo necesitas Kubernetes?**

Imagina que tienes 1 contenedor Docker. Es fácil manejarlo:

```bash
docker run mi-app
```

Pero ¿qué pasa cuando:
- Necesitas 10 copias de tu app (para que aguante más usuarios)
- Una copia falla, quieres que reinicie automáticamente
- Quieres actualizar tu app sin que los usuarios noten
- Necesitas balancear la carga entre las 10 copias
- Necesitas monitoreo, logs, métricas

**Kubernetes es un orquestador de contenedores.**

"Orquestador" = Dirige múltiples contenedores como un director de orquesta.

```
Sin Kubernetes:
Tú tienes que hacer:
├─ Iniciar contenedores
├─ Reiniciar los que fallan
├─ Balancear la carga
├─ Actualizar versiones
├─ Recolectar logs
└─ Monitorear salud
            ↓
        👶 Trabajo de bebé


Con Kubernetes:
Kubernetes hace:
├─ Inicia contenedores
├─ Reinicia automáticamente
├─ Balancea carga
├─ Actualiza sin downtime
├─ Recolecta logs
└─ Monitorea salud
            ↓
        🤖 Automatizado
```

**¿Qué es un clúster Kubernetes?**

Un clúster es un grupo de máquinas que Kubernetes gestiona:

```
┌──────────────────────────────────────────┐
│        Clúster Kubernetes                │
│  ┌────────────────────────────────────┐  │
│  │   Nodo 1 (máquina física)          │  │
│  │  ┌──────────────────────────────┐  │  │
│  │  │ 🐳 Contenedor 1              │  │  │
│  │  │ 🐳 Contenedor 2              │  │  │
│  │  └──────────────────────────────┘  │  │
│  └────────────────────────────────────┘  │
│  ┌────────────────────────────────────┐  │
│  │   Nodo 2 (máquina física)          │  │
│  │  ┌──────────────────────────────┐  │  │
│  │  │ 🐳 Contenedor 3              │  │  │
│  │  │ 🐳 Contenedor 4              │  │  │
│  │  └──────────────────────────────┘  │  │
│  └────────────────────────────────────┘  │
│  ┌────────────────────────────────────┐  │
│  │   Nodo 3 (máquina física)          │  │
│  │  ┌──────────────────────────────┐  │  │
│  │  │ 🐳 Contenedor 5              │  │  │
│  │  │ 🐳 Contenedor 6              │  │  │
│  │  └──────────────────────────────┘  │  │
│  └────────────────────────────────────┘  │
│                                          │
│  Control Plane (el director)             │
│  ├─ API Server                           │
│  ├─ Scheduler                            │
│  └─ Controller Manager                   │
└──────────────────────────────────────────┘
```

**Casos donde necesitas Kubernetes:**

- ✓ App con miles de usuarios
- ✓ Necesitas alta disponibilidad
- ✓ Actualizaciones frecuentes
- ✓ Múltiples servicios trabajando juntos
- ✓ Infraestructura en la nube

**Casos donde NO necesitas Kubernetes:**

- ✗ Startup pequeña con pocos usuarios
- ✗ Aplicación simple de una máquina
- ✗ Prototipo
- ✗ Estás empezando con Docker

---

### Lección 3: Docker vs Máquinas Virtuales (30 minutos)

**¿Son lo mismo?**

No. Aunque parecen similares, son muy diferentes.

**Máquina Virtual (VM):**

```
┌─────────────────────────────────────┐
│ Tu Computadora (macOS)              │
│ ┌──────────────────────────────┐   │
│ │ Hypervisor (VirtualBox)      │   │
│ │  ┌────────────────────────┐  │   │
│ │  │ SO: Windows            │  │   │
│ │  │ RAM: 4 GB              │  │   │
│ │  │ Disco: 30 GB           │  │   │
│ │  │ LibreOffice            │  │   │
│ │  └────────────────────────┘  │   │
│ │  ┌────────────────────────┐  │   │
│ │  │ SO: Linux              │  │   │
│ │  │ RAM: 2 GB              │  │   │
│ │  │ Disco: 20 GB           │  │   │
│ │  │ PostgreSQL             │  │   │
│ │  └────────────────────────┘  │   │
│ └──────────────────────────────┘   │
└─────────────────────────────────────┘

Desventajas:
- Pesadas (GBs de espacio)
- Lentas (segundos para iniciar)
- Consumen mucha RAM
- Cada VM necesita SO completo
```

**Contenedor Docker:**

```
┌──────────────────────────────────────┐
│ Tu Computadora (macOS)               │
│ ┌────────────────────────────────┐  │
│ │ Docker Engine                  │  │
│ │  ┌─────────────────────────┐   │  │
│ │  │ 🐳 Contenedor 1         │   │  │
│ │  │ - Mi App                │   │  │
│ │  │ - Dependencias          │   │  │
│ │  │ - 50 MB                 │   │  │
│ │  └─────────────────────────┘   │  │
│ │  ┌─────────────────────────┐   │  │
│ │  │ 🐳 Contenedor 2         │   │  │
│ │  │ - PostgreSQL            │   │  │
│ │  │ - Configuración         │   │  │
│ │  │ - 200 MB                │   │  │
│ │  └─────────────────────────┘   │  │
│ │  ┌─────────────────────────┐   │  │
│ │  │ 🐳 Contenedor 3         │   │  │
│ │  │ - Nginx                 │   │  │
│ │  │ - Config                │   │  │
│ │  │ - 100 MB                │   │  │
│ │  └─────────────────────────┘   │  │
│ └────────────────────────────────┘  │
└──────────────────────────────────────┘

Ventajas:
- Ligeros (MBs)
- Rápidos (milisegundos)
- Comparten kernel
- Aislados pero eficientes
```

**Comparación Detallada:**

| Aspecto | VM | Contenedor |
|---------|----|-----------:|
| **Tamaño** | GBs | MBs |
| **Inicio** | Segundos | Milisegundos |
| **RAM** | 2-4 GB c/u | 50-500 MB |
| **SO** | SO completo c/u | Kernel compartido |
| **Aislamiento** | Muy fuerte | Fuerte |
| **Performance** | 90-95% nativo | 95-99% nativo |
| **Gestión** | Compleja | Simple |

**¿Cuándo usar cada uno?**

Usa **Máquinas Virtuales** si:
- Necesitas SO diferentes (Windows + Linux)
- Máxima seguridad de aislamiento
- Software que no corre en contenedores

Usa **Contenedores** si:
- Quieres aplicaciones ligeras
- Necesitas iniciar rápido
- Quieres escalabilidad
- Desarrollas en equipo

---

### Lección 4: Conceptos Fundamentales

**Imagen Docker**

Una imagen es como una "receta" o "plantilla". Define todo lo que necesita tu aplicación:

```dockerfile
# Imagen base
FROM python:3.11

# Instalar dependencias del sistema
RUN apt-get install -y libpq-dev

# Copiar código
COPY app.py /app/

# Instalar dependencias Python
RUN pip install flask

# Puerto que expone
EXPOSE 5000

# Comando a ejecutar
CMD ["python", "app.py"]
```

**Contenedor**

Un contenedor es una instancia en ejecución de una imagen. Es como la diferencia entre:
- Imagen = Clase (en programación)
- Contenedor = Instancia de la clase

**Registro (Registry)**

Un registro es un almacén de imágenes. El más popular es Docker Hub (como GitHub pero para imágenes).

```
Tu máquina              Docker Hub (internet)
┌──────────────┐        ┌──────────────────┐
│ 🐳 Imagen    │   →    │ 📦 Imagen        │
│ mi-app:1.0   │        │ usuario/mi-app   │
└──────────────┘        └──────────────────┘
              (docker push)
```

---

### Lección 5: Casos de Uso Reales

**¿Dónde se usa Docker y Kubernetes?**

- **Netflix** - Kubernetes para servir millones de usuarios
- **Spotify** - Microservicios en contenedores
- **Uber** - Arquitectura de microservicios
- **Airbnb** - Deployment continuo
- **Dropbox** - Escalado automático

**Ejemplo Real: Startup de Delivery de Comida**

```
┌─────────────────────────────────────┐
│  Mi Startup de Delivery             │
├─────────────────────────────────────┤
│ API Backend (Python)                │
│  └─ 🐳 Contenedor 1                 │
│  └─ 🐳 Contenedor 2                 │
│  └─ 🐳 Contenedor 3 (auto-escalado) │
├─────────────────────────────────────┤
│ Base de Datos (PostgreSQL)          │
│  └─ 🐳 Contenedor DB                │
├─────────────────────────────────────┤
│ Frontend (React)                    │
│  └─ 🐳 Contenedor Frontend          │
├─────────────────────────────────────┤
│ Cache (Redis)                       │
│  └─ 🐳 Contenedor Cache             │
└─────────────────────────────────────┘

Con Docker:
✓ Inicio rápido
✓ Deploy en minutos
✓ Cada dev tiene mismo ambiente
✓ Escala fácilmente

Con Kubernetes (cuando crece):
✓ Auto-escalado en horas pico
✓ Actualizaciones sin downtime
✓ Auto-recuperación
✓ Manejo de miles de usuarios
```

---

## 🎓 Próximo Paso

Cuando termines este módulo, estás listo para:

**Opción A: Aprender Docker primero**
→ Ve a [`01_docker_basico`](../01_docker_basico)

**Opción B: Saltar a Kubernetes**
→ Ve a [`03_kubernetes_basico`](../03_kubernetes_basico)
(No recomendado si es tu primer vez)

---

## ✅ Checklist de Entendimiento

Antes de pasar al siguiente módulo, asegúrate de entender:

- [ ] ¿Qué es Docker y por qué existe?
- [ ] Diferencia entre máquina virtual y contenedor
- [ ] Ventajas de Docker
- [ ] ¿Qué es Kubernetes?
- [ ] ¿Cuándo necesitas Kubernetes?
- [ ] Diferencia entre imagen y contenedor
- [ ] ¿Qué es un registro (registry)?
- [ ] Puedes explicar a alguien por qué Docker es mejor que VMs

Si tienes dudas en cualquiera de estos, **vuelve a leer** esa sección. Es importante tener los conceptos claros.

---

**Tiempo estimado de este módulo: 2-3 horas**

¿Listo para empezar con Docker?
