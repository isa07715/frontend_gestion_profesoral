import requests

class ExperienciaService:
    def __init__(self):
        self.base_url = "http://localhost:8000/api"
        self.api_url = f"{self.base_url}/experiencia"

    def get_all(self, limite=1000):
        try:
            response = requests.get(f"{self.api_url}/", params={"limite": limite})
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print(f"❌ Error al listar experiencias: {e}")
            return []

    def create(self, data):
        try:
            response = requests.post(f"{self.api_url}/", json=data)
            if response.status_code == 201:
                return True
            return False
        except Exception as e:
            print(f"❌ Error al crear experiencia: {e}")
            return False

    def update(self, id, data):
        try:
            response = requests.put(f"{self.api_url}/{id}", json=data)
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Error al actualizar: {e}")
            return False

    def delete(self, id):
        try:
            response = requests.delete(f"{self.api_url}/{id}")
            return response.status_code == 204
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")
            return False