"""
Aplicación web simple con Flask para tutorial de Docker y Kubernetes
"""
from flask import Flask, render_string
import os

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tutorial Docker & Kubernetes</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            padding: 40px;
            text-align: center;
        }
        h1 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        .logo {
            font-size: 80px;
            margin: 20px 0;
        }
        p {
            color: #555;
            line-height: 1.6;
            margin: 15px 0;
            font-size: 16px;
        }
        .info-box {
            background: #f0f4ff;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .status {
            display: inline-block;
            background: #0f966e;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            margin: 10px 0;
            font-weight: bold;
        }
        .tech-stack {
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
            flex-wrap: wrap;
        }
        .tech {
            background: #f0f4ff;
            padding: 15px 20px;
            margin: 5px;
            border-radius: 5px;
            font-weight: bold;
            color: #667eea;
        }
        .footer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 2px solid #eee;
            color: #999;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">🐳 ☸️</div>
        <h1>Tutorial Docker & Kubernetes</h1>
        
        <div class="status">✓ Contenedor ejecutándose correctamente</div>
        
        <p>¡Bienvenido! Esta aplicación está corriendo en un <strong>contenedor Docker</strong></p>
        
        <div class="info-box">
            <strong>Información del contenedor:</strong>
            <p>Hostname: {{ hostname }}</p>
            <p>Puerto: 5000 (mapeado a 8080)</p>
            <p>Estado: {{ status }}</p>
        </div>
        
        <h2 style="color: #764ba2; margin-top: 30px;">Stack Tecnológico</h2>
        <div class="tech-stack">
            <div class="tech">🐳 Docker</div>
            <div class="tech">☸️ Kubernetes</div>
            <div class="tech">🐍 Python</div>
            <div class="tech">⚡ Flask</div>
        </div>
        
        <div class="info-box" style="border-left-color: #764ba2;">
            <strong>Próximos pasos:</strong>
            <p>1. Explorar más ejemplos</p>
            <p>2. Desplegar en Kubernetes</p>
            <p>3. Escalar la aplicación</p>
        </div>
        
        <div class="footer">
            <p>Tutorial de Docker y Kubernetes - Tema Anthropic/Google</p>
            <p>Aprende a containerizar y orquestar aplicaciones</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    hostname = os.getenv('HOSTNAME', 'local-container')
    status = '🟢 Activo'
    return render_string(html_template, hostname=hostname, status=status)

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'docker-kubernetes-tutorial'}, 200

if __name__ == '__main__':
    # Escucha en todos los interfaces (0.0.0.0) para que sea accesible desde fuera del contenedor
    app.run(host='0.0.0.0', port=5000, debug=True)
