# Frontend Gestión Profesoral - Flask

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 📋 Descripción

Frontend desarrollado con *Flask* para el Sistema de Gestión Profesoral de la Universidad. 
Esta aplicación consume la API REST (FastAPI) y presenta la interfaz de usuario al navegador.

*Entrega 1:* CRUD para 5 tablas sin claves foráneas.

## 📊 Tablas Implementadas

| # | Tabla | Endpoint Flask | API Backend |
|---|-------|---------------|-------------|
| 1 | area_conocimiento | /api/area_conocimiento | GET/POST/PUT/DELETE |
| 2 | termino_clave | /api/termino_clave | GET/POST/PUT/DELETE |
| 3 | linea_investigacion | /api/linea_investigacion | GET/POST/PUT/DELETE |
| 4 | programa | /api/programa | GET/POST/PUT/DELETE |
| 5 | red | /api/red | GET/POST/PUT/DELETE |

## 🏗️ Arquitectura
┌─────────────────┐         HTTP/REST         ┌─────────────────┐
│     FLASK       │ ◄──────────────────────► │    FASTAPI      │
│   (Frontend)    │        JSON/JWT           │   (Backend)     │
│   Puerto: 5000  │                           │   Puerto: 8000  │
└─────────────────┘                           └────────┬────────┘
                                                       │
                                                       ▼
                                                ┌─────────────┐
                                                │  PostgreSQL │
                                                │   Puerto:   │
                                                │    5432     │
                                                └─────────────┘
## 🚀 Instalación

### 1. Prerrequisitos

- Python 3.10+
- API FastAPI ejecutándose en http://localhost:8000
- Base de datos gestion_profesoral creada en PostgreSQL

### 2. Clonar o navegar al proyecto

```bash
cd frontend
# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt
```

---

# Configuración del entorno Flask
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=tu_clave_secreta_muy_segura_12345

# URL de la API FastAPI (Backend)
API_BASE_URL=http://localhost:8000
API_TIMEOUT=30

# Configuración de sesiones
SESSION_COOKIE_SECURE=False
PERMANENT_SESSION_LIFETIME=3600