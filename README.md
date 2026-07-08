# Curso Git & GitHub — Diplomado

Material educativo completo para aprender Git y GitHub desde cero. Este es mi repo para aprender git y github en el diplomado.

## 📁 Estructura del Proyecto

```
curso_git_diplomado/
├── README.md                    # Este archivo
├── .gitignore                   # Archivos a ignorar en Git
├── src/
│   └── git_tutorial.ipynb       # Notebook interactivo del tutorial
└── doc/
    └── (documentación adicional futura)
```

## 📚 Contenido del Tutorial

El notebook `src/git_tutorial.ipynb` cubre:

- **¿Qué es Git?** — Conceptos fundamentales y arquitectura
- **Instalación** — macOS, Linux y Windows
- **Configuración** — Identidad, editor, alias productivos
- **Flujo Básico** — `git status`, `git add`, `git commit`
- **Historial** — `git log`, `git diff`, `git show`
- **Ramas** — `git branch`, `git switch`, `git checkout`
- **Fusiones** — Merge, conflictos, resolución
- **Remotos** — `git fetch`, `git pull`, `git push`
- **GitHub** — Fork, Pull Requests, Issues
- **Stash** — `git stash` para trabajo temporal
- **Deshacer Cambios** — `git restore`, `git reset`, `git revert`
- **Comandos Avanzados** — `git rebase`, `git cherry-pick`, `git tag`, `git bisect`, `git blame`, `git reflog`
- **Flujos de Trabajo** — Git Flow, GitHub Flow, Trunk-Based
- **Buenas Prácticas** — Conventional Commits, commits atómicos
- **Cheat Sheet** — Referencia rápida de todos los comandos

## 🚀 Cómo Usar Este Repositorio

### Opción 1: Ejecutar en Google Colab (sin instalar nada)

1. Descarga `src/git_tutorial.ipynb`
2. Ve a [Google Colab](https://colab.research.google.com)
3. Carga el archivo
4. Ejecuta las celdas interactivamente

### Opción 2: Ejecutar localmente con Jupyter

```bash
# Clonar el repositorio
git clone https://github.com/danielxxi/curso_git_diplomado.git
cd curso_git_diplomado

# Instalar Jupyter (si no lo tienes)
pip install jupyter

# Iniciar Jupyter
jupyter notebook src/git_tutorial.ipynb
```

### Opción 3: Leer en GitHub

Simplemente abre `src/git_tutorial.ipynb` directamente en GitHub (previsualiza el notebook).

## 📝 Cambios en esta Rama

En la rama `ajustes_1_diplomado` se agregaron:

- ✅ Directorio `src/` con el notebook del tutorial
- ✅ Directorio `doc/` para documentación futura
- ✅ Archivo `.gitignore` para excluir archivos innecesarios
- ✅ README mejorado con instrucciones claras

## 💻 Requisitos

- Git instalado (v2.28+)
- Python 3.8+ (para ejecutar localmente)
- Jupyter Notebook o Google Colab

## 🔗 Enlaces Útiles

- [Documentación oficial de Git](https://git-scm.com/doc)
- [Guía de GitHub](https://docs.github.com)
- [Learn Git Branching (interactivo)](https://learngitbranching.js.org)
- [Conventional Commits](https://www.conventionalcommits.org)

## 📧 Contacto

Creado como material del diplomado en Git y GitHub.

---

*Última actualización: 2026-07-07*
