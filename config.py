"""
config.py — Configuración de Flask.
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()


class Config:
    """Configuración base de Flask."""
    
    # Clave secreta para sesiones y CSRF
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    
    # URL de la API FastAPI
    API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000')
    API_TIMEOUT = int(os.getenv('API_TIMEOUT', '30'))
    
    # Configuración de sesiones
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False').lower() == 'true'
    PERMANENT_SESSION_LIFETIME = int(os.getenv('PERMANENT_SESSION_LIFETIME', '3600'))
    
    # Configuración de Flask
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', '1') == '1'


class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True


class ProductionConfig(Config):
    """Configuración para producción."""
    DEBUG = False
    SESSION_COOKIE_SECURE = True


# Diccionario de configuraciones
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}