"""
termino_clave_routes.py — Rutas CRUD para término clave.
PK es 'termino' (VARCHAR), no 'id'.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.termino_clave_service import TerminoClaveService

termino_clave_bp = Blueprint('termino_clave', __name__, url_prefix='/api/termino_clave') 


@termino_clave_bp.route('/')
def list():
    """Listar todos los términos clave."""
    service = TerminoClaveService()
    terminos = service.get_all()
    return render_template('termino_clave/list.html', terminos=terminos)


@termino_clave_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crear nuevo término clave."""
    if request.method == 'POST':
        data = {
            'termino': request.form['termino'],
            'termino_ingles': request.form.get('termino_ingles', '')
        }
        
        service = TerminoClaveService()
        if service.create(data):
            flash('Término clave creado exitosamente', 'success')
            return redirect(url_for('termino_clave.list'))
        else:
            flash('Error al crear el término clave', 'error')
    
    return render_template('termino_clave/create.html')


@termino_clave_bp.route('/<termino>')
def detail(termino):
    """Ver detalle de un término clave."""
    service = TerminoClaveService()
    termino_obj = service.get_by_id(termino)
    
    if termino_obj is None:
        flash('Término clave no encontrado', 'error')
        return redirect(url_for('termino_clave.list'))
    
    return render_template('termino_clave/detail.html', termino=termino_obj)


@termino_clave_bp.route('/<termino>/edit', methods=['GET', 'POST'])
def edit(termino):
    """Editar un término clave."""
    service = TerminoClaveService()
    
    if request.method == 'POST':
        data = {
            'termino_ingles': request.form.get('termino_ingles', '')
        }
        
        if service.update(termino, data):
            flash('Término clave actualizado exitosamente', 'success')
            return redirect(url_for('termino_clave.list'))
        else:
            flash('Error al actualizar el término clave', 'error')
    
    termino_obj = service.get_by_id(termino)
    if termino_obj is None:
        flash('Término clave no encontrado', 'error')
        return redirect(url_for('termino_clave.list'))
    
    return render_template('termino_clave/edit.html', termino=termino_obj)


@termino_clave_bp.route('/<termino>/delete', methods=['POST'])
def delete(termino):
    """Eliminar un término clave."""
    service = TerminoClaveService()
    
    if service.delete(termino):
        flash('Término clave eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el término clave', 'error')
    
    return redirect(url_for('termino_clave.list'))