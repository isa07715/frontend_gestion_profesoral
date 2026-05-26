from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.rol_service import RolService

rol_bp = Blueprint('rol', __name__, url_prefix='/api/rol')

@rol_bp.route('/')
def list():
    service = RolService()
    roles = service.get_all()
    return render_template('rol/list.html', roles=roles if roles else [])

@rol_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'nombre': request.form['nombre'],
                'descripcion': request.form['descripcion'],
                'activo': request.form.get('activo') == 'on'
            }
            
            service = RolService()
            if service.create(data):
                flash('Rol creado exitosamente', 'success')
                return redirect(url_for('rol.list'))
            else:
                flash('Error al crear el rol', 'error')
        except Exception as e:
            print(f" Error: {e}")
            flash('Error inesperado', 'error')
    
    return render_template('rol/create.html')

@rol_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = RolService()
    
    if request.method == 'POST':
        try:
            data = {
                'nombre': request.form['nombre'],
                'descripcion': request.form['descripcion'],
                'activo': request.form.get('activo') == 'on'
            }
            
            if service.update(id, data):
                flash('Rol actualizado exitosamente', 'success')
                return redirect(url_for('rol.list'))
            else:
                flash('Error al actualizar', 'error')
        except Exception as e:
            flash('Error al actualizar', 'error')

    roles = service.get_all()
    rol = next((r for r in roles if r.get('id') == id), None)
    
    return render_template('rol/edit.html', rol=rol)

@rol_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = RolService()
    if service.delete(id):
        flash('Rol eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('rol.list'))