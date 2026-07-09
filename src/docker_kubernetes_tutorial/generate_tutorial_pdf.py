#!/usr/bin/env python3
"""
Generador de PDF: Tutorial Docker y Kubernetes paso a paso
Incluye comandos exactos a ejecutar y explicaciones
"""

from fpdf import FPDF
from datetime import datetime

class TutorialPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        self.set_auto_page_break(auto=True, margin=15)
    
    def header(self):
        """Encabezado de cada página"""
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(26, 115, 232)  # Google Blue
        self.cell(0, 10, "Tutorial Docker & Kubernetes - Paso a Paso", 0, 1, "C")
        self.set_draw_color(15, 150, 110)  # Google Green
        self.line(15, 20, self.WIDTH - 15, 20)
        self.ln(10)
    
    def footer(self):
        """Pie de página"""
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"Página {self.page_no()}", 0, 0, "C")
    
    def section_title(self, title):
        """Título de sección"""
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(26, 115, 232)
        self.cell(0, 10, title, 0, 1, "L")
        self.set_draw_color(15, 150, 110)
        self.line(15, self.get_y(), self.WIDTH - 15, self.get_y())
        self.ln(5)
    
    def subsection_title(self, title):
        """Subtítulo"""
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(118, 75, 162)  # Anthropic Purple
        self.cell(0, 8, title, 0, 1, "L")
        self.ln(2)
    
    def body_text(self, text):
        """Texto normal"""
        self.set_font("Helvetica", "", 10)
        self.set_text_color(60, 64, 67)  # Dark gray
        self.multi_cell(0, 5, text)
        self.ln(2)
    
    def code_block(self, code):
        """Bloque de código"""
        self.set_font("Courier", "", 9)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(60, 64, 67)  # Dark gray background
        
        # Fondo gris oscuro
        x = self.get_x()
        y = self.get_y()
        
        lines = code.split('\n')
        for line in lines:
            self.cell(0, 5, line, 0, 1, "L", fill=True)
        
        self.ln(2)
        self.set_text_color(60, 64, 67)  # Volver a texto normal
    
    def example_box(self, title, content):
        """Caja con ejemplo"""
        self.set_draw_color(15, 150, 110)
        self.set_fill_color(240, 244, 255)  # Light blue
        self.set_x(18)
        self.multi_cell(0, 25, "", border=1, fill=True)
        
        # Título
        self.set_y(self.get_y() - 24)
        self.set_x(20)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(26, 115, 232)
        self.cell(0, 5, f"[*] {title}", 0, 1)
        
        # Contenido
        self.set_x(20)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(60, 64, 67)
        self.multi_cell(160, 4, content)

def main():
    pdf = TutorialPDF()
    pdf.set_title("Tutorial Docker & Kubernetes")
    pdf.add_page()
    
    # ===== PORTADA =====
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 36)
    pdf.set_text_color(26, 115, 232)
    pdf.cell(0, 15, "Docker & Kubernetes", 0, 1, "C")
    
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(118, 75, 162)
    pdf.cell(0, 10, "Tutorial Completo Paso a Paso", 0, 1, "C")
    
    pdf.ln(20)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(60, 64, 67)
    pdf.multi_cell(0, 6, "Aprende a containerizar aplicaciones con Docker\ny orquestarlas en producción con Kubernetes\n\n"
                          "Tutorial interactivo con ejemplos funcionales\npara macOS, Linux y Windows")
    
    pdf.ln(20)
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 5, f"Generado: {datetime.now().strftime('%d de %B de %Y')}", 0, 1, "C")
    
    # ===== TABLA DE CONTENIDOS =====
    pdf.add_page()
    pdf.section_title("Tabla de Contenidos")
    
    contents = [
        ("1", "Introducción: Conceptos de Docker y Kubernetes", 3),
        ("2", "Instalación en macOS", 4),
        ("3", "Instalación en Linux", 4),
        ("4", "Instalación en Windows", 5),
        ("5", "Ejemplo 1: Docker - Construir y ejecutar contenedor", 6),
        ("6", "Ejemplo 2: Kubernetes - Desplegar aplicación", 7),
        ("7", "Operaciones comunes (logs, escalar, monitoreo)", 8),
        ("8", "Compartir en GitHub", 9),
    ]
    
    for num, title, page in contents:
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 64, 67)
        pdf.cell(10, 6, num, 0, 0, "L")
        pdf.cell(145, 6, title, 0, 0, "L")
        pdf.set_text_color(100, 100, 100)
        pdf.cell(20, 6, str(page), 0, 1, "R")
    
    # ===== SECCIÓN 1: INTRODUCCIÓN =====
    pdf.add_page()
    pdf.section_title("1. Introducción: Docker y Kubernetes")
    
    pdf.subsection_title("¿Qué es Docker?")
    pdf.body_text("Docker es una plataforma que permite empaquetar tu aplicación, "
                  "dependencias y configuración en una unidad llamada 'contenedor'. "
                  "Un contenedor es como una máquina virtual pero mucho más ligera.")
    
    pdf.body_text("Ventajas:\n"
                  "- Consistencia: Funciona igual en tu máquina, en testing y en producción\n"
                  "- Eficiencia: Usa menos recursos que VMs tradicionales\n"
                  "- Portabilidad: Puedes correr en cualquier máquina con Docker instalado\n"
                  "- Aislamiento: Cada contenedor está aislado de otros")
    
    pdf.subsection_title("¿Qué es Kubernetes?")
    pdf.body_text("Kubernetes (K8s) es un orquestador de contenedores. "
                  "Gestiona automáticamente múltiples contenedores, distribuyendo carga, "
                  "escalando, reiniciando en caso de fallo, etc.")
    
    pdf.body_text("Características principales:\n"
                  "- Auto-escalado: Aumenta/disminuye pods automáticamente\n"
                  "- Auto-recuperación: Reinicia contenedores que fallan\n"
                  "- Actualizaciones sin downtime: Rolling updates\n"
                  "- Balanceo de carga: Distribuye tráfico automáticamente")
    
    # ===== SECCIÓN 2: INSTALACIÓN MACOS =====
    pdf.add_page()
    pdf.section_title("2. Instalación en macOS")
    
    pdf.subsection_title("Opción A: Docker Desktop (Recomendado)")
    pdf.body_text("1. Descarga Docker Desktop desde:")
    pdf.code_block("https://www.docker.com/products/docker-desktop")
    pdf.body_text("2. Ejecuta el instalador (.dmg) y sigue las instrucciones")
    pdf.body_text("3. Docker Desktop incluye: Docker Engine, Docker CLI, Docker Compose")
    pdf.body_text("4. También puedes activar Kubernetes desde Settings -> Kubernetes")
    
    pdf.subsection_title("Opción B: Homebrew")
    pdf.body_text("Si prefieres instalar por línea de comandos:")
    pdf.code_block("brew install docker docker-compose")
    
    pdf.subsection_title("Verificar instalación")
    pdf.body_text("Abre Terminal y ejecuta:")
    pdf.code_block("docker --version\ndocker run hello-world")
    pdf.body_text("Si ves el mensaje 'Hello from Docker!', está correctamente instalado.")
    
    # ===== SECCIÓN 3: INSTALACIÓN LINUX =====
    pdf.add_page()
    pdf.section_title("3. Instalación en Linux")
    
    pdf.subsection_title("Ubuntu/Debian")
    pdf.body_text("Paso 1: Actualizar paquetes del sistema")
    pdf.code_block("sudo apt update\nsudo apt upgrade -y")
    
    pdf.body_text("Paso 2: Instalar Docker desde repositorio oficial")
    pdf.code_block("curl -fsSL https://get.docker.com -o get-docker.sh\nsudo sh get-docker.sh")
    
    pdf.body_text("Paso 3: Agregar tu usuario al grupo docker (para no usar sudo)")
    pdf.code_block("sudo usermod -aG docker $USER\nnewgrp docker")
    
    pdf.body_text("Paso 4: Verificar instalación")
    pdf.code_block("docker --version\ndocker run hello-world")
    
    # ===== SECCIÓN 4: INSTALACIÓN WINDOWS =====
    pdf.add_page()
    pdf.section_title("4. Instalación en Windows")
    
    pdf.subsection_title("Requisitos previos")
    pdf.body_text("- Windows 10 Pro, Enterprise o Education (No Home)\n"
                  "- Procesador compatible con virtualización\n"
                  "- Al menos 4 GB RAM disponible\n"
                  "- Hyper-V debe estar habilitado")
    
    pdf.subsection_title("Paso 1: Habilitar Hyper-V")
    pdf.body_text("Abre PowerShell como Administrador y ejecuta:")
    pdf.code_block("Enable-WindowsOptionalFeature -FeatureName Hyper-V -All")
    pdf.body_text("Reinicia la computadora cuando se pida")
    
    pdf.subsection_title("Paso 2: Instalar Docker Desktop")
    pdf.body_text("1. Descarga desde: https://www.docker.com/products/docker-desktop")
    pdf.body_text("2. Ejecuta el instalador")
    pdf.body_text("3. Marca 'Install required Windows components for WSL 2'")
    pdf.body_text("4. Reinicia al terminar")
    
    pdf.subsection_title("Paso 3: Verificar")
    pdf.body_text("Abre PowerShell o CMD y ejecuta:")
    pdf.code_block("docker --version\ndocker run hello-world")
    
    # ===== SECCIÓN 5: EJEMPLO 1 - DOCKER =====
    pdf.add_page()
    pdf.section_title("5. Ejemplo 1: Docker - Contenedor funcional")
    
    pdf.subsection_title("¿Qué haremos?")
    pdf.body_text("Construiremos una imagen Docker de una aplicación web con Flask, "
                  "la ejecutaremos en un contenedor, y la veremos funcionar en el navegador.")
    
    pdf.subsection_title("Paso 1: Crear estructura de archivos")
    pdf.body_text("En terminal macOS (dentro del proyecto):")
    pdf.code_block("cd /Users/daniel/curso_git_dpl/curso_git_diplomado\n"
                   "mkdir -p src/docker_kubernetes_tutorial")
    
    pdf.subsection_title("Paso 2: Crear archivos necesarios")
    pdf.body_text("Archivo 1: Dockerfile (plantilla para imagen)")
    pdf.code_block("# Ver archivo: Dockerfile\n"
                   "# Contiene instrucciones para construir la imagen")
    
    pdf.body_text("Archivo 2: app.py (aplicación web)")
    pdf.code_block("# Ver archivo: src/docker_kubernetes_tutorial/app.py\n"
                   "# Aplicación Flask que muestra página HTML")
    
    # ===== SECCIÓN 6: DOCKER - CONSTRUIR Y EJECUTAR =====
    pdf.add_page()
    pdf.section_title("5 (cont). Construir y ejecutar contenedor Docker")
    
    pdf.subsection_title("Paso 3: Construir la imagen Docker")
    pdf.body_text("En terminal, desde la raíz del proyecto:")
    pdf.code_block("cd /Users/daniel/curso_git_dpl/curso_git_diplomado\n"
                   "docker build -t mi-app-web:latest .")
    
    pdf.body_text("Explicación del comando:\n"
                  "- docker build: Construye una imagen\n"
                  "- -t mi-app-web:latest: Tag (nombre:versión)\n"
                  "- .: Busca Dockerfile en directorio actual\n\n"
                  "Esto puede tardar 1-2 minutos la primera vez.")
    
    pdf.subsection_title("Paso 4: Ejecutar el contenedor")
    pdf.body_text("Una vez construida la imagen:")
    pdf.code_block("docker run -p 8080:5000 mi-app-web:latest")
    
    pdf.body_text("Explicación:\n"
                  "- docker run: Ejecuta un contenedor\n"
                  "- -p 8080:5000: Mapea puerto 8080 (local) -> 5000 (contenedor)\n"
                  "- mi-app-web:latest: Imagen a usar\n\n"
                  "Deberías ver en terminal:\n"
                  "  'Running on http://0.0.0.0:5000'")
    
    pdf.subsection_title("Paso 5: Prueba en navegador")
    pdf.body_text("Abre tu navegador y ve a:")
    pdf.code_block("http://localhost:8080")
    
    pdf.body_text("Deberías ver una página web hermosa con:")
    pdf.body_text("- Título: 'Docker & Kubernetes Tutorial'\n"
                  "- Estado: '[OK] Contenedor ejecutándose correctamente'\n"
                  "- Stack tecnológico: Docker, Kubernetes, Python, Flask\n\n"
                  "¡Felicidades! Tu primer contenedor está funcionando.")
    
    # ===== SECCIÓN 7: VERIFICAR Y DETENER =====
    pdf.add_page()
    pdf.section_title("5 (cont). Verificar y detener contenedor")
    
    pdf.subsection_title("Paso 6: Inspeccionar el contenedor")
    pdf.body_text("En otra ventana de terminal (sin cerrar la anterior):")
    pdf.body_text("Ver contenedores ejecutándose:")
    pdf.code_block("docker ps")
    
    pdf.body_text("Deberías ver algo como:\n"
                  "CONTAINER ID  IMAGE          STATUS           PORTS\n"
                  "abc123def456  mi-app-web...  Up 2 minutes    0.0.0.0:8080->5000/tcp")
    
    pdf.subsection_title("Paso 7: Ver logs")
    pdf.code_block("docker logs <container-id>")
    
    pdf.body_text("O si quieres ver logs en tiempo real mientras usas la app:")
    pdf.code_block("docker logs -f <container-id>")
    
    pdf.subsection_title("Paso 8: Detener el contenedor")
    pdf.body_text("Cuando termines, presiona Ctrl+C en la terminal donde corre Docker")
    pdf.body_text("O desde otra terminal:")
    pdf.code_block("docker stop <container-id>")
    
    # ===== SECCIÓN 8: KUBERNETES =====
    pdf.add_page()
    pdf.section_title("6. Ejemplo 2: Kubernetes - Orquestar contenedores")
    
    pdf.subsection_title("¿Qué haremos?")
    pdf.body_text("Usaremos la misma imagen Docker anterior, pero ahora la "
                  "desplegaremos en Kubernetes. K8s creará automáticamente 3 "
                  "copias (replicas) de la aplicación, con balanceo de carga.")
    
    pdf.subsection_title("Paso 1: Habilitar Kubernetes en Docker Desktop")
    pdf.body_text("Opción A (Docker Desktop con K8s):\n"
                  "  1. Abre Docker Desktop\n"
                  "  2. Ve a Settings -> Kubernetes\n"
                  "  3. Marca 'Enable Kubernetes'\n"
                  "  4. Espera 2-3 minutos a que inicie\n\n"
                  "Opción B (Minikube):\n"
                  "  brew install minikube\n"
                  "  minikube start")
    
    pdf.subsection_title("Paso 2: Verificar K8s está corriendo")
    pdf.code_block("kubectl version --client\nkubectl get nodes")
    
    pdf.body_text("Deberías ver tu node (máquina local) en estado 'Ready'")
    
    # ===== SECCIÓN 9: DESPLEGAR EN K8S =====
    pdf.add_page()
    pdf.section_title("6 (cont). Desplegar en Kubernetes")
    
    pdf.subsection_title("Paso 3: Preparar manifiestos de Kubernetes")
    pdf.body_text("Archivo: src/docker_kubernetes_tutorial/kubernetes.yaml")
    pdf.body_text("Este archivo define:\n"
                  "- Namespace: Separación lógica de recursos\n"
                  "- Deployment: 3 replicas de la aplicación\n"
                  "- Service: Expone la app en la red (puerto 8080)\n"
                  "- HPA: Auto-escalado basado en CPU")
    
    pdf.subsection_title("Paso 4: Aplicar manifiestos")
    pdf.code_block("kubectl apply -f src/docker_kubernetes_tutorial/kubernetes.yaml")
    
    pdf.body_text("Deberías ver:\n"
                  "  namespace/docker-kubernetes-tutorial created\n"
                  "  deployment.apps/mi-app-web created\n"
                  "  service/mi-app-web created\n"
                  "  horizontalpodautoscaler.autoscaling/mi-app-web-hpa created")
    
    pdf.subsection_title("Paso 5: Verificar que está corriendo")
    pdf.body_text("Ver deployments:")
    pdf.code_block("kubectl get deployments -n docker-kubernetes-tutorial")
    
    pdf.body_text("Ver pods (instancias de la aplicación):")
    pdf.code_block("kubectl get pods -n docker-kubernetes-tutorial")
    
    pdf.body_text("Deberías ver 3 pods en estado 'Running'")
    
    # ===== SECCIÓN 10: ACCEDER A K8S =====
    pdf.add_page()
    pdf.section_title("6 (cont). Acceder a la aplicación en Kubernetes")
    
    pdf.subsection_title("Paso 6: Port-forward (acceso local)")
    pdf.body_text("Para acceder a la aplicación desde tu navegador:")
    pdf.code_block("kubectl port-forward -n docker-kubernetes-tutorial \\\n"
                   "  service/mi-app-web 8080:8080")
    
    pdf.body_text("Verás: 'Forwarding from 127.0.0.1:8080 -> 8080'")
    
    pdf.subsection_title("Paso 7: Acceder en navegador")
    pdf.code_block("http://localhost:8080")
    
    pdf.body_text("¡Verás la MISMA página web que en Docker!\n\n"
                  "Pero ahora está ejecutándose en Kubernetes, con:\n"
                  "- 3 replicas de la aplicación\n"
                  "- Balanceo de carga automático\n"
                  "- Auto-recuperación si un pod falla\n"
                  "- Auto-escalado si aumenta la demanda")
    
    # ===== SECCIÓN 11: OPERACIONES COMUNES =====
    pdf.add_page()
    pdf.section_title("7. Operaciones comunes en Kubernetes")
    
    pdf.subsection_title("Ver logs de un pod")
    pdf.code_block("kubectl logs <pod-name> \\\n"
                   "  -n docker-kubernetes-tutorial")
    
    pdf.subsection_title("Seguir logs en tiempo real")
    pdf.code_block("kubectl logs -f <pod-name> \\\n"
                   "  -n docker-kubernetes-tutorial")
    
    pdf.subsection_title("Describir pod (información detallada)")
    pdf.code_block("kubectl describe pod <pod-name> \\\n"
                   "  -n docker-kubernetes-tutorial")
    
    pdf.subsection_title("Escalar manualmente (cambiar replicas)")
    pdf.code_block("kubectl scale deployment/mi-app-web \\\n"
                   "  --replicas=5 \\\n"
                   "  -n docker-kubernetes-tutorial")
    
    pdf.subsection_title("Ver recursos de un pod")
    pdf.code_block("kubectl top pods -n docker-kubernetes-tutorial")
    
    # ===== SECCIÓN 12: COMPARTIR EN GITHUB =====
    pdf.add_page()
    pdf.section_title("8. Compartir en GitHub (paso a paso)")
    
    pdf.subsection_title("Paso 1: Ver cambios realizados")
    pdf.body_text("En terminal, verifica qué archivos cambiaron:")
    pdf.code_block("cd /Users/daniel/curso_git_dpl/curso_git_diplomado\ngit status")
    
    pdf.body_text("Deberías ver archivos nuevos (Dockerfile, app.py, etc.)")
    
    pdf.subsection_title("Paso 2: Agregar archivos al staging")
    pdf.body_text("Agrega todos los cambios del tutorial Docker/Kubernetes:")
    pdf.code_block("git add src/docker_kubernetes_tutorial/\ngit add Dockerfile\ngit add run_tutorial.sh\ngit add doc/Tutorial_Docker_Kubernetes.pptx\ngit add doc/Tutorial_Docker_Kubernetes_Paso_a_Paso.pdf")
    
    pdf.body_text("O más simple: agrega todo")
    pdf.code_block("git add -A")
    
    pdf.subsection_title("Paso 3: Verificar cambios a commit")
    pdf.code_block("git status")
    
    pdf.body_text("Deberías ver los archivos en verde (listos para commit)")
    
    pdf.subsection_title("Paso 4: Hacer commit")
    pdf.body_text("Crea un commit con un mensaje descriptivo:")
    pdf.code_block("git commit -m \"feat: agregar tutorial completo de Docker y Kubernetes\"")
    
    pdf.body_text("Mensaje incluye:\n"
                  "  feat: = feature (nueva funcionalidad)\n"
                  "  Descripción clara de qué se agregó")
    
    pdf.subsection_title("Paso 5: Enviar a GitHub")
    pdf.code_block("git push origin main")
    
    pdf.body_text("Verás:\n"
                  "  Total X objects written\n"
                  "  main -> main\n\n"
                  "Esto significa que los cambios están en GitHub")
    
    pdf.subsection_title("Paso 6: Verificar en GitHub")
    pdf.body_text("1. Abre navegador: https://github.com/danielxxi/curso_git_diplomado")
    pdf.body_text("2. Deberías ver los archivos nuevos")
    pdf.body_text("3. Los PDFs y PPTX se ven en la interfaz web")
    
    # ===== PÁGINA FINAL =====
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(26, 115, 232)
    pdf.ln(50)
    pdf.cell(0, 20, "¡Felicidades!", 0, 1, "C")
    
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(60, 64, 67)
    pdf.ln(10)
    pdf.multi_cell(0, 8, "Ya dominas Docker y Kubernetes.\n\n"
                        "Ahora puedes:\n"
                        "[OK] Containerizar aplicaciones\n"
                        "[OK] Ejecutar contenedores localmente\n"
                        "[OK] Orquestar en Kubernetes\n"
                        "[OK] Escalar automáticamente\n"
                        "[OK] Monitorear y troubleshootear\n\n"
                        "Próximos pasos:\n"
                        "- Desplegar en producción (AWS, Azure, GCP)\n"
                        "- Implementar CI/CD con Docker\n"
                        "- Usar Helm para gestionar aplicaciones\n"
                        "- Implementar observabilidad (Prometheus, Grafana)",
                        align="C")
    
    # Guardar PDF
    output_path = '/Users/daniel/curso_git_dpl/curso_git_diplomado/doc/Tutorial_Docker_Kubernetes_Paso_a_Paso.pdf'
    pdf.output(output_path)
    print(f"[OK] PDF creado: {output_path}")

if __name__ == '__main__':
    main()
