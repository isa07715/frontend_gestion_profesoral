"""
programa_service.py — Servicio para consumir la API de programa académico.
"""
from services.api_client import get_api_client


class ProgramaService:
    """Servicio para operaciones de programa académico."""
    
    def __init__(self):
        self.api = get_api_client()
        self.endpoint = '/api/programa'
    
    def get_all(self, limite=1000):
        """Obtener todos los programas académicos."""
        return self.api.get(self.endpoint, params={'limite': limite})
    
    def get_by_id(self, id):
        """Obtener un programa académico por ID."""
        return self.api.get(f"{self.endpoint}/{id}")
    
    def create(self, data):
        """Crear un nuevo programa académico."""
        return self.api.post(self.endpoint, data)
    
    def update(self, id, data):
        """Actualizar un programa académico."""
        return self.api.put(f"{self.endpoint}/{id}", data)
    
    def delete(self, id):
        """Eliminar un programa académico."""
        return self.api.delete(f"{self.endpoint}/{id}")