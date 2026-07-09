#!/bin/bash

# Script helper: Comandos útiles para el tutorial Docker y Kubernetes
# Uso: bash run_tutorial.sh <comando>

set -e

PROJECT_DIR="/Users/daniel/curso_git_dpl/curso_git_diplomado"
TUTORIAL_DIR="$PROJECT_DIR/src/docker_kubernetes_tutorial"
DOC_DIR="$PROJECT_DIR/doc"

echo "🐳 Tutorial Docker & Kubernetes Helper 🐳"
echo "==========================================="
echo ""

case "$1" in
  
  generate-pptx)
    echo "📊 Generando presentación PPTX..."
    cd "$PROJECT_DIR"
    python3 "$TUTORIAL_DIR/generate_tutorial.py"
    echo "✅ Presentación lista: $DOC_DIR/Tutorial_Docker_Kubernetes.pptx"
    ;;
  
  generate-pdf)
    echo "📄 Generando PDF paso a paso..."
    cd "$PROJECT_DIR"
    python3 "$TUTORIAL_DIR/generate_tutorial_pdf.py"
    echo "✅ PDF listo: $DOC_DIR/Tutorial_Docker_Kubernetes_Paso_a_Paso.pdf"
    ;;
  
  generate-all)
    echo "📊 Generando presentación PPTX..."
    python3 "$TUTORIAL_DIR/generate_tutorial.py"
    echo "✅ Presentación lista"
    echo ""
    echo "📄 Generando PDF paso a paso..."
    python3 "$TUTORIAL_DIR/generate_tutorial_pdf.py"
    echo "✅ PDF listo"
    ;;
  
  docker-build)
    echo "🔨 Construyendo imagen Docker..."
    cd "$PROJECT_DIR"
    docker build -t mi-app-web:latest .
    echo "✅ Imagen construida: mi-app-web:latest"
    ;;
  
  docker-run)
    echo "🚀 Ejecutando contenedor Docker..."
    echo "   Accede a: http://localhost:8080"
    echo "   Presiona Ctrl+C para detener"
    echo ""
    docker run -p 8080:5000 mi-app-web:latest
    ;;
  
  docker-logs)
    echo "📝 Mostrando logs de contenedor..."
    CONTAINER_ID=$(docker ps -q -f ancestor=mi-app-web:latest | head -1)
    if [ -z "$CONTAINER_ID" ]; then
      echo "❌ No hay contenedor ejecutándose"
    else
      docker logs -f "$CONTAINER_ID"
    fi
    ;;
  
  docker-stop)
    echo "⏹️  Deteniendo contenedor Docker..."
    CONTAINER_ID=$(docker ps -q -f ancestor=mi-app-web:latest | head -1)
    if [ -z "$CONTAINER_ID" ]; then
      echo "❌ No hay contenedor ejecutándose"
    else
      docker stop "$CONTAINER_ID"
      echo "✅ Contenedor detenido"
    fi
    ;;
  
  k8s-deploy)
    echo "☸️  Desplegando en Kubernetes..."
    cd "$PROJECT_DIR"
    kubectl apply -f "$TUTORIAL_DIR/kubernetes.yaml"
    echo "✅ Aplicación desplegada"
    echo ""
    echo "Esperando que los pods inicien..."
    sleep 5
    kubectl get pods -n docker-kubernetes-tutorial
    ;;
  
  k8s-port-forward)
    echo "🔗 Port-forwarding a Kubernetes..."
    echo "   Accede a: http://localhost:8080"
    echo "   Presiona Ctrl+C para detener"
    echo ""
    kubectl port-forward -n docker-kubernetes-tutorial service/mi-app-web 8080:8080
    ;;
  
  k8s-logs)
    echo "📝 Mostrando logs de pods..."
    if [ -z "$2" ]; then
      PODS=$(kubectl get pods -n docker-kubernetes-tutorial -o jsonpath='{.items[0].metadata.name}')
      kubectl logs -f "$PODS" -n docker-kubernetes-tutorial
    else
      kubectl logs -f "$2" -n docker-kubernetes-tutorial
    fi
    ;;
  
  k8s-scale)
    REPLICAS=${2:-5}
    echo "📈 Escalando a $REPLICAS replicas..."
    kubectl scale deployment/mi-app-web --replicas=$REPLICAS -n docker-kubernetes-tutorial
    echo "✅ Escalado completado"
    ;;
  
  k8s-status)
    echo "📊 Estado de la aplicación en Kubernetes:"
    echo ""
    echo "Deployments:"
    kubectl get deployments -n docker-kubernetes-tutorial
    echo ""
    echo "Pods:"
    kubectl get pods -n docker-kubernetes-tutorial
    echo ""
    echo "Services:"
    kubectl get services -n docker-kubernetes-tutorial
    ;;
  
  k8s-delete)
    echo "🗑️  Eliminando aplicación de Kubernetes..."
    kubectl delete namespace docker-kubernetes-tutorial
    echo "✅ Aplicación eliminada"
    ;;
  
  *)
    echo "Uso: bash run_tutorial.sh <comando>"
    echo ""
    echo "Comandos disponibles:"
    echo ""
    echo "📊 Generar materiales:"
    echo "  generate-pptx    - Generar presentación PPTX"
    echo "  generate-pdf     - Generar PDF paso a paso"
    echo "  generate-all     - Generar ambos"
    echo ""
    echo "🐳 Docker:"
    echo "  docker-build     - Construir imagen Docker"
    echo "  docker-run       - Ejecutar contenedor (http://localhost:8080)"
    echo "  docker-logs      - Ver logs del contenedor"
    echo "  docker-stop      - Detener contenedor"
    echo ""
    echo "☸️  Kubernetes:"
    echo "  k8s-deploy       - Desplegar en Kubernetes"
    echo "  k8s-port-forward - Habilitar acceso web (http://localhost:8080)"
    echo "  k8s-status       - Ver estado de la aplicación"
    echo "  k8s-logs         - Ver logs de pods"
    echo "  k8s-scale N      - Escalar a N replicas (default: 5)"
    echo "  k8s-delete       - Eliminar aplicación de Kubernetes"
    echo ""
    ;;
esac
