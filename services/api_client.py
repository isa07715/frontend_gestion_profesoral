"""
api_client.py — Cliente HTTP para consumir la API FastAPI.
"""
import requests
from flask import current_app, session


class APIClient:
    """Cliente para hacer peticiones a la API FastAPI."""
    
    def __init__(self):
        try:
            self.base_url = current_app.config.get('API_BASE_URL', 'http://localhost:8000')
            self.timeout = current_app.config.get('API_TIMEOUT', 30)
        except RuntimeError:
            self.base_url = 'http://localhost:8000'
            self.timeout = 30
        
        self.session = requests.Session()
        
        if session and 'token' in session:
            self.session.headers.update({
                'Authorization': f"Bearer {session['token']}"
            })
    
    def _handle_response(self, response):
        """Manejar respuesta de la API."""
        print("STATUS CODE:", response.status_code)
        print("RESPONSE TEXT:", response.text)


        if response.status_code == 401:
            if session:
                session.pop('token', None)
                session.pop('user', None)
            return None
        
        if response.status_code in [200, 201, 204]:
            if response.status_code == 204:
                return True
            try:
                return response.json()
            except:
                return None
        
        return None
    
    def get(self, endpoint, params=None):
        """GET request."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.get(url, params=params, timeout=self.timeout)
            return self._handle_response(response)
        except requests.RequestException as e:
            print(f"Error en GET {endpoint}: {e}")
            return None
    
    def post(self, endpoint, data=None):
        """POST request."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.post(url, json=data, timeout=self.timeout)
            return self._handle_response(response)
        except requests.RequestException as e:
            print(f"Error en POST {endpoint}: {e}")
            return None
    
    def put(self, endpoint, data=None):
        """PUT request."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.put(url, json=data, timeout=self.timeout)
            return self._handle_response(response)
        except requests.RequestException as e:
            print(f"Error en PUT {endpoint}: {e}")
            return None
    
    def delete(self, endpoint):
        """DELETE request."""
        try:
            url = f"{self.base_url}{endpoint}"
            response = self.session.delete(url, timeout=self.timeout)
            return self._handle_response(response)
        except requests.RequestException as e:
            print(f"Error en DELETE {endpoint}: {e}")
            return False


def get_api_client():
    """Factory para obtener un cliente API."""
    return APIClient()