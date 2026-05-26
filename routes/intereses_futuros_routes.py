from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.intereses_futuros_service import InteresesFuturosService
from services.docente_service import DocenteService
from services.termino_clave_service import TerminoClaveService

intereses_futuros_bp = Blueprint('intereses_futuros', __name__, url_prefix='/api/intereses_futuros')

@intereses_futuros_bp.route('/')
def list():
    service = InteresesFuturosService()
    intereses = service.get_all()
    return render_template('intereses_futuros/list.html', intereses=intereses if intereses else [])

@intereses_futuros_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'docente': int(request.form['docente']),
                'termino_clave': request.form['termino_clave']
            }
            
            print(f"🔵 [DEBUG] Enviando a API: {data}")
            
            service = InteresesFuturosService()
            resultado = service.create(data)
            
            print(f"🔴 [DEBUG] Respuesta API: {resultado}")
            
            if resultado:
                flash('Interés creado exitosamente', 'success')
                return redirect(url_for('intereses_futuros.list'))
            else:
                flash('Error al crear (posiblemente ya existe o error de datos)', 'error')
                
        except ValueError:
            flash('Error: La cédula debe ser un número', 'error')
        except Exception as e:
            print(f"❌ [DEBUG] Excepción: {e}")
            flash('Error inesperado', 'error')

    docentes = DocenteService().get_all() or []
    terminos = TerminoClaveService().get_all() or []
    
    return render_template('intereses_futuros/create.html', docentes=docentes, terminos=terminos)

@intereses_futuros_bp.route('/<cedula>/<termino>/delete', methods=['POST'])
def delete(cedula, termino):
    service = InteresesFuturosService()
    if service.delete(cedula, termino):
        flash('Eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('intereses_futuros.list'))