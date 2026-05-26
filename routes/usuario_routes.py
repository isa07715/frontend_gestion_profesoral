from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario', __name__, url_prefix='/api/usuario')

@usuario_bp.route('/')
def list():
    service = UsuarioService()
    usuarios = service.get_all()
    return render_template('usuario/list.html', usuarios=usuarios if usuarios else [])

@usuario_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'username': request.form['username'],
                'password': request.form['password'],
                'email': request.form['email'],
                'nombre_completo': request.form['nombre_completo'],
                'activo': request.form.get('activo') == 'on'
            }
            service = UsuarioService()
            if service.create(data):
                flash('Usuario creado exitosamente', 'success')
                return redirect(url_for('usuario.list'))
            else:
                flash('Error al crear el usuario', 'error')
        except Exception as e:
            print(f"❌ Error: {e}")
            flash('Error inesperado', 'error')
    
    return render_template('usuario/create.html')

@usuario_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = UsuarioService()
    if request.method == 'POST':
        try:
            data = {
                'username': request.form['username'],
                'password': request.form['password'],
                'email': request.form['email'],
                'nombre_completo': request.form['nombre_completo'],
                'activo': request.form.get('activo') == 'on'
            }
            if service.update(id, data):
                flash('Usuario actualizado exitosamente', 'success')
                return redirect(url_for('usuario.list'))
            else:
                flash('Error al actualizar', 'error')
        except Exception as e:
            flash('Error al actualizar', 'error')

    usuarios = service.get_all()
    usuario = next((u for u in usuarios if u.get('id') == id), None)
    return render_template('usuario/edit.html', usuario=usuario)

@usuario_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = UsuarioService()
    if service.delete(id):
        flash('Usuario eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('usuario.list'))