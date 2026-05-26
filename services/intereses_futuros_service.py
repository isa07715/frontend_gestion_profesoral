import requests

class InteresesFuturosService:
    def __init__(self):
        # ✅ URL directa para evitar el error de importación
        self.base_url = "http://localhost:8000/api"
        self.api_url = f"{self.base_url}/intereses_futuros"

    def get_all(self, limite=1000):
        """Obtiene todos los intereses de investigación"""
        try:
            response = requests.get(f"{self.api_url}/", params={"limite": limite})
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"❌ Error al listar intereses: {e}")
            return []

    def create(self, data):
        """Crea un nuevo interés de investigación"""
        try:
            response = requests.post(f"{self.api_url}/", json=data)
            # 201 Created = éxito
            if response.status_code == 201:
                return True
            return False
        except Exception as e:
            print(f"❌ Error al crear interés: {e}")
            return False

    def delete(self, cedula, termino):
        """Elimina un interés específico"""
        try:
            response = requests.delete(f"{self.api_url}/{cedula}/{termino}")
            return response.status_code == 204
        except Exception as e:
            print(f"❌ Error al eliminar interés: {e}")
            return False