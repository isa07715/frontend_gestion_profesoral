"""
estudios_realizados_service.py - Servicio para conectar con la API de estudios_realizados.
"""
import requests
from typing import Optional

API_URL = "http://localhost:8000/api/estudios_realizados"


class EstudiosRealizadosService:
    """Servicio para operaciones con la API de estudios_realizados."""
    
    def __init__(self):
        self.api_url = API_URL
    
    def get_all(self, limite: int = 1000) -> list:
        """Obtiene todos los estudios_realizados."""
        try:
            response = requests.get(f"{self.api_url}/?limite={limite}")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"Error al obtener estudios: {e}")
            return []
    
    def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene un estudios_realizados por id."""
        try:
            response = requests.get(f"{self.api_url}/{id}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error al obtener estudio: {e}")
            return None
    
    def create(self, data: dict) -> bool:
        """Crea un nuevo estudios_realizados."""
        try:
            response = requests.post(self.api_url, json=data)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error al crear estudio: {e}")
            return False
    
    def update(self, id: int, data: dict) -> bool:
        """Actualiza un estudios_realizados."""
        try:
            response = requests.put(f"{self.api_url}/{id}", json=data)
            return response.status_code == 200
        except Exception as e:
            print(f"Error al actualizar estudio: {e}")
            return False
    
    def delete(self, id: int) -> bool:
        """Elimina un estudios_realizados."""
        try:
            response = requests.delete(f"{self.api_url}/{id}")
            return response.status_code == 204
        except Exception as e:
            print(f"Error al eliminar estudio: {e}")
            return False