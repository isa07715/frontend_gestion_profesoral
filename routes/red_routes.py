"""
red_routes.py — Rutas CRUD para red académica.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.red_service import RedService

red_bp = Blueprint('red', __name__, url_prefix='/api/red') 


@red_bp.route('/')
def list():
    """Listar todas las redes académicas."""
    service = RedService()
    redes = service.get_all()
    return render_template('red/list.html', redes=redes)


@red_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crear nueva red académica."""
    if request.method == 'POST':
        data = {
            'idr': int(request.form['idr']),
            'nombre': request.form['nombre'],
            'url': request.form['url'],
            'pais': request.form['pais']
        }
        
        service = RedService()
        if service.create(data):
            flash('Red académica creada exitosamente', 'success')
            return redirect(url_for('red.list'))
        else:
            flash('Error al crear la red académica', 'error')
    
    return render_template('red/create.html')


@red_bp.route('/<int:idr>')
def detail(idr):
    """Ver detalle de una red académica."""
    service = RedService()
    red = service.get_by_id(idr)
    
    if red is None:
        flash('Red no encontrada', 'error')
        return redirect(url_for('red.list'))
    
    return render_template('red/detail.html', red=red)


@red_bp.route('/<int:idr>/edit', methods=['GET', 'POST'])
def edit(idr):
    """Editar una red académica."""
    service = RedService()
    
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'url': request.form['url'],
            'pais': request.form['pais']
        }
        
        if service.update(idr, data):
            flash('Red académica actualizada exitosamente', 'success')
            return redirect(url_for('red.list'))
        else:
            flash('Error al actualizar la red académica', 'error')
    
    red = service.get_by_id(idr)
    if red is None:
        flash('Red no encontrada', 'error')
        return redirect(url_for('red.list'))
    
    return render_template('red/edit.html', red=red)


@red_bp.route('/<int:idr>/delete', methods=['POST'])
def delete(idr):
    """Eliminar una red académica."""
    service = RedService()
    
    if service.delete(idr):
        flash('Red académica eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar la red académica', 'error')
    
    return redirect(url_for('red.list'))