"""
services/_init_.py — Inicializa el paquete de servicios.
"""
from services.api_client import get_api_client
from services.area_conocimiento_service import AreaConocimientoService
from services.termino_clave_service import TerminoClaveService
from services.linea_investigacion_service import LineaInvestigacionService
from services.programa_service import ProgramaService
from services.red_service import RedService

_all_ = [
    'get_api_client',
    'AreaConocimientoService',
    'TerminoClaveService',
    'LineaInvestigacionService',
    'ProgramaService',
    'RedService',
]