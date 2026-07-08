# Curso Git & GitHub + Computer Vision — Diplomado

🎓 Material educativo completo y profesional para aprender **Git, GitHub y Visión por Computadora** desde cero. Proyecto desarrollado como material del diplomado con recursos interactivos, documentación en PDF y notebooks Jupyter.

## ✨ Características

- ✅ Tutoriales interactivos en Jupyter Notebook (compatibles con Google Colab)
- ✅ Documentación completa en PDF en español latino
- ✅ Presentación PowerPoint con diseño minimalist
- ✅ Ejercicios prácticos y desafíos
- ✅ Bien documentado en español para estudiantes latinoamericanos

---

## 📁 Estructura del Proyecto

```
curso_git_diplomado/
├── README.md                                    # Este archivo
├── .gitignore                                   # Archivos a ignorar en Git
├── src/
│   ├── git_tutorial.ipynb                      # Tutorial interactivo de Git (90 celdas)
│   └── vision_por_computadora_principiantes.ipynb  # Intro a Computer Vision (31 celdas)
└── doc/
    └── Manual_Git_Completo_ES.pdf              # Manual PDF completo en español (30 páginas)
```

---

## 📚 Módulos Disponibles

### 1️⃣ Git & GitHub Tutorial (`src/git_tutorial.ipynb`)

**90 celdas interactivas** que cubren:

- **Conceptos Fundamentales** — ¿Qué es Git? Arquitectura distribuida
- **Instalación Completa** — macOS, Linux y Windows (con 5 opciones en Windows)
- **Configuración Inicial** — Identidad, editor, alias productivos
- **Flujo Básico** — `git status`, `git add`, `git commit`, `git diff`
- **Historial y Análisis** — `git log`, `git diff`, `git show`, `git blame`
- **Ramas** — `git branch`, `git switch`, `git checkout`, eliminar ramas
- **Fusiones (Merge)** — Fast-forward vs merge commit, resolución de conflictos
- **Operaciones Remotas** — `git fetch`, `git pull`, `git push`
- **GitHub Workflow** — Fork, Pull Requests, Issues, colaboración
- **Stash** — Guardado temporal de cambios
- **Deshacer Cambios** — `git restore`, `git reset`, `git revert`, `git reflog`
- **Comandos Avanzados** — `git rebase`, `git cherry-pick`, `git tag`, `git bisect`
- **Flujos de Trabajo** — Git Flow, GitHub Flow, Trunk-Based Development
- **Buenas Prácticas** — Conventional Commits, commits atómicos, mensajes claros
- **Cheat Sheet** — Referencia rápida y descareable

### 2️⃣ Visión por Computadora (`src/vision_por_computadora_principiantes.ipynb`)

**31 celdas interactivas** con enfoque en principiantes:

- **Introducción** — ¿Qué es Computer Vision? Aplicaciones reales (reconocimiento facial, conducción autónoma, OCR)
- **Conceptos Fundamentales** — Píxeles, canales (RGB, escala de grises), resolución
- **Setup** — Instalación de OpenCV, NumPy, Matplotlib, PIL, Scikit-image
- **Cargar y Visualizar** — Desde archivo, URL o crear imágenes nuevas
- **Operaciones Básicas** — Redimensionamiento, conversión de color, rotación
- **Filtros** — Blur (desenfoque), detección de bordes Canny
- **Características** — Detección de esquinas con Harris Corner
- **Histogramas** — Análisis de distribución de píxeles
- **Umbralizacion** — Conversión a imagen binaria
- **Pipeline Completo** — Ejercicio práctico: ruido → procesamiento → análisis
- **Desafío Final** — Experimenta con tus propias transformaciones

### 3️⃣ Manual PDF Completo (`doc/Manual_Git_Completo_ES.pdf`)

**30 páginas** de documentación profesional en español latino:

- Tabla de contenidos
- 13 secciones temáticas
- Instalación detallada (macOS, Linux, Windows)
- Conceptos con diagramas
- Cheat sheet para referencia rápida
- Troubleshooting de errores comunes
- Recursos útiles y enlaces

---

## 🚀 Cómo Usar Este Repositorio

### 📌 Opción 1: Google Colab (Recomendado - Sin Instalación)

**Para Git Tutorial:**
1. Abre [Google Colab](https://colab.research.google.com)
2. Menú → `Archivo` → `Abrir notebook`
3. Busca: `https://github.com/danielxxi/curso_git_diplomado/blob/main/src/git_tutorial.ipynb`
4. Ejecuta las celdas interactivamente

**Para Computer Vision:**
1. Mismo proceso con: `https://github.com/danielxxi/curso_git_diplomado/blob/main/src/vision_por_computadora_principiantes.ipynb`

### 💻 Opción 2: Ejecutar Localmente

```bash
# Clonar el repositorio
git clone https://github.com/danielxxi/curso_git_diplomado.git
cd curso_git_diplomado

# Crear entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install jupyter notebook opencv-python numpy matplotlib pillow scikit-image

# Iniciar Jupyter
jupyter notebook

# Luego abre src/git_tutorial.ipynb o src/vision_por_computadora_principiantes.ipynb
```

### 📖 Opción 3: Leer en GitHub

- Abre los archivos `.ipynb` directamente en GitHub
- Vista previa interactiva (solo lectura)
- Perfecto para una rápida revisión

### 📄 Opción 4: Descargar PDF

- Descarga `doc/Manual_Git_Completo_ES.pdf`
- Lectura offline
- Referencia rápida

---

## 🔄 Ramas y Cambios Recientes

### `main` (Rama Principal)
✅ Último estado estable del proyecto
- Tutorial de Git completo
- Manual PDF incluido
- Estructura de proyecto finalizada

### `ajustes_2_diplomado`
📄 Manual PDF en formato descargable agregado

### `ajustes_3_diplomado`
🖼️ **Nuevo módulo de Computer Vision agregado**
- Notebook completo para principiantes
- 31 celdas con teoría y práctica
- Ejercicios interactivos

---

## 📝 Cambios en Cada Rama

### Rama: `ajustes_1_diplomado` ✅ MERGEADA A MAIN
```
✅ Directorio src/ con el notebook del tutorial
✅ Directorio doc/ para documentación futura
✅ Archivo .gitignore configurado
✅ README con instrucciones claras
```

### Rama: `ajustes_2_diplomado` ✅ MERGEADA A MAIN
```
✅ Manual_Git_Completo_ES.pdf (30 páginas)
  - Tabla de contenidos
  - 13 secciones temáticas
  - Instalación detallada (macOS, Linux, Windows)
  - Troubleshooting
  - Cheat sheet imprimible
```

### Rama: `ajustes_3_diplomado` 🆕 EN DESARROLLO
```
🆕 vision_por_computadora_principiantes.ipynb
  - 31 celdas interactivas
  - Introducción a Computer Vision
  - OpenCV, filtros, detección de características
  - Ejercicios prácticos para principiantes
```

---

## 💻 Requisitos Técnicos

### Para Google Colab
- ✅ Navegador web actualizado
- ✅ Conexión a internet
- ✅ Cuenta de Google (gratis)
- ✅ Sin instalación adicional

### Para Ejecución Local
- Python 3.8 o superior
- pip (gestor de paquetes)
- Librerías: jupyter, opencv-python, numpy, matplotlib, pillow, scikit-image

### Para Git & GitHub
- Git 2.28+ instalado
- Cuenta de GitHub (gratis)
- Terminal/CMD conocimientos básicos

---

## 🎯 Objetivo de Aprendizaje

Después de completar este material, podrás:

### Git & GitHub
- ✅ Inicializar y clonar repositorios
- ✅ Hacer commits con mensajes descriptivos
- ✅ Crear y mergear ramas
- ✅ Resolver conflictos de merge
- ✅ Colaborar en GitHub con Pull Requests
- ✅ Usar comandos avanzados (rebase, cherry-pick, stash)
- ✅ Seguir flujos de trabajo profesionales (GitHub Flow, Git Flow)
- ✅ Entender buenas prácticas en versionamiento

### Computer Vision
- ✅ Entender la estructura de imágenes digitales
- ✅ Cargar y manipular imágenes con OpenCV
- ✅ Aplicar filtros y transformaciones básicas
- ✅ Detectar características (bordes, esquinas)
- ✅ Analizar histogramas y umbralizacion
- ✅ Implementar pipelines de procesamiento

---

## 🔗 Enlaces Útiles

### Documentación Oficial
- [Git Documentation](https://git-scm.com/doc) — Guía oficial completa
- [GitHub Docs](https://docs.github.com) — Ayuda de GitHub
- [OpenCV Docs](https://docs.opencv.org/) — Referencia de OpenCV
- [Python Docs](https://docs.python.org/3/) — Referencia de Python

### Recursos Interactivos
- [Learn Git Branching](https://learngitbranching.js.org/) — Visualizador interactivo de ramas
- [Conventional Commits](https://www.conventionalcommits.org/) — Estándar de mensajes
- [Oh Shit, Git!?!](https://ohshitgit.com/) — Solución de problemas frecuentes

### Comunidades
- [Stack Overflow - Git](https://stackoverflow.com/questions/tagged/git)
- [GitHub Discussions](https://github.com/danielxxi/curso_git_diplomado/discussions)
- [Reddit r/learnprogramming](https://reddit.com/r/learnprogramming)

---

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Notebooks Jupyter | 2 |
| Total de celdas | 121 |
| Páginas PDF | 30 |
| Ejercicios prácticos | 15+ |
| Idioma | Español Latino |
| Público objetivo | Principiantes |
| Tiempo estimado | 8-12 horas |

---

## 👨‍💻 Sobre Este Proyecto

Este material fue desarrollado como parte del diplomado en Git y GitHub, con énfasis en:
- 📚 Educación accesible para principiantes
- 🌐 Recursos en español latino
- 💡 Enfoque práctico con ejercicios
- 🎓 Contenido profesional y actualizado
- 🤝 Colaboración y buenas prácticas

---

## 📧 Contacto y Soporte

### Preguntas sobre el contenido
- Abre un [Issue en GitHub](https://github.com/danielxxi/curso_git_diplomado/issues)
- Participa en [Discussions](https://github.com/danielxxi/curso_git_diplomado/discussions)

### Sugerencias y mejoras
- Haz un Fork del proyecto
- Crea una rama con tus cambios
- Abre un Pull Request

---

## 📜 Licencia

Este proyecto está disponible bajo licencia **MIT** — eres libre de usar, modificar y distribuir este material educativo.

---

## 🙏 Agradecimientos

Agradezco a la comunidad de educación tecnológica y a todos los recursos open-source que hacen posible material como este.

---

**Última actualización:** 2026-07-07  
**Versión:** 2.0 (Con Computer Vision)  
**Estado:** En desarrollo activo ✨
