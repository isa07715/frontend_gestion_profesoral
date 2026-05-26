"""
docente_service.py - Servicio para conectar con la API de docente.
"""
import requests
from typing import Optional

API_URL = "http://localhost:8000/api/docente"


class DocenteService:
    """Servicio para operaciones con la API de docente."""
    
    def __init__(self):
        self.api_url = API_URL
    
    def get_all(self, limite: int = 1000) -> list:
        """Obtiene todos los docentes."""
        try:
            response = requests.get(f"{self.api_url}/?limite={limite}")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"Error al obtener docentes: {e}")
            return []
    
    def get_by_id(self, cedula: int) -> Optional[dict]:
        """Obtiene un docente por cedula."""
        try:
            response = requests.get(f"{self.api_url}/{cedula}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error al obtener docente: {e}")
            return None
    
    def create(self, data: dict) -> bool:
        """Crea un nuevo docente."""
        try:
            response = requests.post(self.api_url, json=data)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error al crear docente: {e}")
            return False
    
    def update(self, cedula: int, data: dict) -> bool:
        """Actualiza un docente."""
        try:
            response = requests.put(f"{self.api_url}/{cedula}", json=data)
            return response.status_code == 200
        except Exception as e:
            print(f"Error al actualizar docente: {e}")
            return False
    
    def delete(self, cedula: int) -> bool:
        """Elimina un docente."""
        try:
            response = requests.delete(f"{self.api_url}/{cedula}")
            return response.status_code == 204
        except Exception as e:
            print(f"Error al eliminar docente: {e}")
            return False