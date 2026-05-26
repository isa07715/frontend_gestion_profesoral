"""
area_conocimiento_routes.py — Rutas CRUD para área de conocimiento.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.area_conocimiento_service import AreaConocimientoService

area_conocimiento_bp = Blueprint('area_conocimiento', __name__, url_prefix='/api/area_conocimiento')


@area_conocimiento_bp.route('/')
def list():
    """Listar todas las áreas de conocimiento."""
    service = AreaConocimientoService()
    areas = service.get_all()
    return render_template('area_conocimiento/list.html', areas=areas)


@area_conocimiento_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crear nueva área de conocimiento."""
    if request.method == 'POST':
        try:
            data = {
                'id': int(request.form['id']),
                'gran_area': request.form['gran_area'],
                'area': request.form['area'],
                'disciplina': request.form['disciplina']
            }

            service = AreaConocimientoService()

            if service.create(data):
                flash('Área de conocimiento creada exitosamente', 'success')
                return redirect(url_for('area_conocimiento.list'))
            else:
                flash('Error al crear el área de conocimiento', 'error')

        except Exception as e:
            print(e)
            flash(f'Error: {e}', 'error')

    return render_template('area_conocimiento/create.html')


@area_conocimiento_bp.route('/<int:id>')
def detail(id):
    """Ver detalle de un área de conocimiento."""
    service = AreaConocimientoService()
    area = service.get_by_id(id)
    
    if area is None:
        flash('Área de conocimiento no encontrada', 'error')
        return redirect(url_for('area_conocimiento.list'))
    
    return render_template('area_conocimiento/detail.html', area=area)


@area_conocimiento_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """Editar un área de conocimiento."""
    service = AreaConocimientoService()
    
    if request.method == 'POST':
        data = {
            'gran_area': request.form['gran_area'],
            'area': request.form['area'],
            'disciplina': request.form['disciplina']
        }
        
        if service.update(id, data):
            flash('Área de conocimiento actualizada exitosamente', 'success')
            return redirect(url_for('area_conocimiento.list'))
        else:
            flash('Error al actualizar el área de conocimiento', 'error')
    
    area = service.get_by_id(id)
    if area is None:
        flash('Área de conocimiento no encontrada', 'error')
        return redirect(url_for('area_conocimiento.list'))
    
    return render_template('area_conocimiento/edit.html', area=area)


@area_conocimiento_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """Eliminar un área de conocimiento (borrado lógico)."""
    service = AreaConocimientoService()
    
    if service.delete(id):
        flash('Área de conocimiento eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar el área de conocimiento', 'error')
    
    return redirect(url_for('area_conocimiento.list'))