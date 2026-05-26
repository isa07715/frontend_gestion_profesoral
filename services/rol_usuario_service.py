"""
rol_usuario_service.py - Servicio para conectar con la API de rol_usuario.
"""
import requests
from typing import Optional

API_URL = "http://localhost:8000/api/rol_usuario"


class RolUsuarioService:
    """Servicio para operaciones con la API de rol_usuario."""
    
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
    
    def create(self,  dict) -> bool:
        """Crea un nuevo registro."""
        try:
            response = requests.post(self.api_url, json=data)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error al crear registro: {e}")
            return False
    
    def delete(self, usuario_id: int, rol_id: int) -> bool:
        """Elimina un registro."""
        try:
            response = requests.delete(f"{self.api_url}/{usuario_id}/{rol_id}")
            return response.status_code == 204
        except Exception as e:
            print(f"Error al eliminar registro: {e}")
            return False