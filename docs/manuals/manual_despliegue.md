# Manual de Despliegue

Este manual describe cómo desplegar la aplicación SENA_TEST en un entorno de producción o desarrollo.

## Requisitos del sistema
- Python 3.12 o superior
- Docker y Docker Compose (opcional, recomendado)
- Acceso a internet para instalar dependencias

## Instalación y ejecución (modo local)
1. Clonar el repositorio:
   ```powershell
   git clone <repository-url>
   cd SENA_TEST
   ```
2. Crear y activar un entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
4. Ejecutar la aplicación:
   ```powershell
   python src/main.py
   ```

## Despliegue con Docker Compose (Recomendado)
1. Desde la raíz del proyecto, construir y ejecutar ambos servicios:
   ```powershell
   docker-compose up --build
   ```
2. Acceder a la API en http://localhost:8000
3. Acceder al frontend en http://localhost:3000

## Despliegue con Docker (servicios individuales)
- Puede construir y ejecutar cada servicio por separado usando sus respectivos Dockerfile.

## Variables de entorno
- Configure las variables necesarias en un archivo `.env` si es requerido.

## Pruebas
- Para ejecutar pruebas unitarias:
   ```powershell
   pytest
   ```

## Producción
- Se recomienda usar un servidor web como Nginx como proxy inverso.
- Configure HTTPS para seguridad.
- Realice backups periódicos de la base de datos.

---

Para más detalles, consulte la documentación técnica o contacte al equipo de desarrollo.
