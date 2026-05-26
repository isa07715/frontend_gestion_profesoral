"""
area_conocimiento_service.py — Servicio para consumir la API de área de conocimiento.
"""
from services.api_client import get_api_client


class AreaConocimientoService:
    """Servicio para operaciones de área de conocimiento."""
    
    def __init__(self):
        self.api = get_api_client()  
        self.endpoint = '/api/area_conocimiento'
    
    def get_all(self, limite=1000):
        """Obtener todas las áreas de conocimiento."""
        return self.api.get(self.endpoint, params={'limite': limite})
    
    def get_by_id(self, id):
        """Obtener un área de conocimiento por ID."""
        return self.api.get(f"{self.endpoint}/{id}")
    
    def create(self, data):
        """Crear un nuevo área de conocimiento."""
        return self.api.post(self.endpoint, data)
    
    def update(self, id, data):
        """Actualizar un área de conocimiento."""
        return self.api.put(f"{self.endpoint}/{id}", data)
    
    def delete(self, id):
        """Eliminar un área de conocimiento."""
        return self.api.delete(f"{self.endpoint}/{id}")