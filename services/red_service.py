"""
red_service.py — Servicio para consumir la API de red académica.
"""
from services.api_client import get_api_client


class RedService:
    """Servicio para operaciones de red académica."""
    
    def __init__(self):
        self.api = get_api_client()
        self.endpoint = '/api/red'
    
    def get_all(self, limite=1000):
        """Obtener todas las redes académicas."""
        return self.api.get(self.endpoint, params={'limite': limite})
    
    def get_by_id(self, idr):
        """Obtener una red académica por ID."""
        return self.api.get(f"{self.endpoint}/{idr}")
    
    def create(self, data):
        """Crear una nueva red académica."""
        return self.api.post(self.endpoint, data)
    
    def update(self, idr, data):
        """Actualizar una red académica."""
        return self.api.put(f"{self.endpoint}/{idr}", data)
    
    def delete(self, idr):
        """Eliminar una red académica."""
        return self.api.delete(f"{self.endpoint}/{idr}")