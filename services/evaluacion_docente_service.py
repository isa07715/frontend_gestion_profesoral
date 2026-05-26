"""
evaluacion_docente_service.py - Servicio para conectar con la API de evaluacion_docente.
"""
import requests
from typing import Optional

API_URL = "http://localhost:8000/api/evaluacion_docente"


class EvaluacionDocenteService:
    """Servicio para operaciones con la API de evaluacion_docente."""
    
    def __init__(self):
        self.api_url = API_URL
    
    def get_all(self, limite: int = 1000) -> list:
        """Obtiene todas las evaluaciones."""
        try:
            response = requests.get(f"{self.api_url}/?limite={limite}")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"Error al obtener evaluaciones: {e}")
            return []
    
    def get_by_id(self, id: int) -> Optional[dict]:
        """Obtiene una evaluacion por id."""
        try:
            response = requests.get(f"{self.api_url}/{id}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error al obtener evaluacion: {e}")
            return None
    
    def create(self,  dict) -> bool:
        """Crea una nueva evaluacion."""
        try:
            response = requests.post(self.api_url, json=data)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error al crear evaluacion: {e}")
            return False
    
    def update(self, id: int, data: dict) -> bool:
        """Actualiza una evaluacion."""
        try:
            response = requests.put(f"{self.api_url}/{id}", json=data)
            return response.status_code == 200
        except Exception as e:
            print(f"Error al actualizar evaluacion: {e}")
            return False
    
    def delete(self, id: int) -> bool:
        """Elimina una evaluacion."""
        try:
            response = requests.delete(f"{self.api_url}/{id}")
            return response.status_code == 204
        except Exception as e:
            print(f"Error al eliminar evaluacion: {e}")
            return False