"""
estudio_ac_service.py - Servicio para conectar con la API de estudio_ac.
"""
import requests
from typing import Optional

API_URL = "http://localhost:8000/api/estudio_ac"


class EstudioACService:
    """Servicio para operaciones con la API de estudio_ac."""
    
    def __init__(self):
        self.api_url = API_URL
    
    def get_all(self, limite: int = 1000) -> list:
        """Obtiene todos los registros."""
        try:
            response = requests.get(f"{self.api_url}/?limite={limite}")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"Error al obtener registros: {e}")
            return []
    
    def get_by_id(self, estudio: int, area_conocimiento: int) -> Optional[dict]:
        """Obtiene un registro por PK compuesta."""
        try:
            response = requests.get(f"{self.api_url}/{estudio}/{area_conocimiento}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error al obtener registro: {e}")
            return None
    
    def create(self,  dict) -> bool:
        """Crea un nuevo registro."""
        try:
            response = requests.post(self.api_url, json=data)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error al crear registro: {e}")
            return False
    
    def delete(self, estudio: int, area_conocimiento: int) -> bool:
        """Elimina un registro."""
        try:
            response = requests.delete(f"{self.api_url}/{estudio}/{area_conocimiento}")
            return response.status_code == 204
        except Exception as e:
            print(f"Error al eliminar registro: {e}")
            return False