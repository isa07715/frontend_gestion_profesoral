"""
termino_clave_service.py — Servicio para consumir la API de término clave.
"""
from services.api_client import get_api_client


class TerminoClaveService:
    """Servicio para operaciones de término clave."""
    
    def __init__(self):
        self.api = get_api_client()
        self.endpoint = '/api/termino_clave'
    
    def get_all(self, limite=1000):
        """Obtener todos los términos clave."""
        return self.api.get(self.endpoint, params={'limite': limite})
    
    def get_by_id(self, termino):
        """Obtener un término clave."""
        return self.api.get(f"{self.endpoint}/{termino}")
    
    def create(self, data):
        """Crear un nuevo término clave."""
        return self.api.post(self.endpoint, data)
    
    def update(self, termino, data):
        """Actualizar un término clave."""
        return self.api.put(f"{self.endpoint}/{termino}", data)
    
    def delete(self, termino):
        """Eliminar un término clave."""
        return self.api.delete(f"{self.endpoint}/{termino}")