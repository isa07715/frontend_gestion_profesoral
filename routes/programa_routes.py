"""
programa_routes.py — Rutas CRUD para programa académico.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.programa_service import ProgramaService

programa_bp = Blueprint('programa', __name__, url_prefix='/api/programa')  


@programa_bp.route('/')
def list():
    """Listar todos los programas académicos."""
    service = ProgramaService()
    programas = service.get_all()
    return render_template('programa/list.html', programas=programas)


@programa_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crear nuevo programa académico."""
    if request.method == 'POST':
        data = {
            'id': int(request.form['id']),
            'nombre': request.form['nombre'],
            'tipo': request.form['tipo'],
            'nivel': request.form['nivel'],
            'fecha_creacion': request.form['fecha_creacion'],
            'fecha_cierre': request.form.get('fecha_cierre', ''),
            'numero_cohortes': request.form['numero_cohortes'],
            'cant_graduados': request.form['cant_graduados'],
            'fecha_actualizacion': request.form['fecha_actualizacion'],
            'ciudad': request.form['ciudad'],
            'facultad': int(request.form['facultad'])
        }
        
        service = ProgramaService()
        if service.create(data):
            flash('Programa académico creado exitosamente', 'success')
            return redirect(url_for('programa.list'))
        else:
            flash('Error al crear el programa académico', 'error')
    
    return render_template('programa/create.html')


@programa_bp.route('/<int:id>')
def detail(id):
    """Ver detalle de un programa académico."""
    service = ProgramaService()
    programa = service.get_by_id(id)
    
    if programa is None:
        flash('Programa no encontrado', 'error')
        return redirect(url_for('programa.list'))
    
    return render_template('programa/detail.html', programa=programa)


@programa_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    """Editar un programa académico."""
    service = ProgramaService()
    
    if request.method == 'POST':
        data = {
            'nombre': request.form['nombre'],
            'tipo': request.form['tipo'],
            'nivel': request.form['nivel'],
            'fecha_creacion': request.form['fecha_creacion'],
            'fecha_cierre': request.form.get('fecha_cierre', ''),
            'numero_cohortes': request.form['numero_cohortes'],
            'cant_graduados': request.form['cant_graduados'],
            'fecha_actualizacion': request.form['fecha_actualizacion'],
            'ciudad': request.form['ciudad'],
            'facultad': int(request.form['facultad'])
        }
        
        if service.update(id, data):
            flash('Programa académico actualizado exitosamente', 'success')
            return redirect(url_for('programa.list'))
        else:
            flash('Error al actualizar el programa académico', 'error')
    
    programa = service.get_by_id(id)
    if programa is None:
        flash('Programa no encontrado', 'error')
        return redirect(url_for('programa.list'))
    
    return render_template('programa/edit.html', programa=programa)


@programa_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """Eliminar un programa académico."""
    service = ProgramaService()
    
    if service.delete(id):
        flash('Programa académico eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el programa académico', 'error')
    
    return redirect(url_for('programa.list'))