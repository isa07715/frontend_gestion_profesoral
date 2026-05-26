"""
rol_usuario_routes.py - Rutas CRUD para rol_usuario.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.rol_usuario_service import RolUsuarioService
from services.usuario_service import UsuarioService
from services.rol_service import RolService

rol_usuario_bp = Blueprint('rol_usuario', __name__, url_prefix='/api/rol_usuario')


@rol_usuario_bp.route('/')
def list():
    """Listar todos los registros de rol_usuario."""
    service = RolUsuarioService()
    registros = service.get_all()
    return render_template('rol_usuario/list.html', registros=registros)


@rol_usuario_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Crear nuevo registro en rol_usuario."""
    if request.method == 'POST':
        data = {
            'usuario_id': int(request.form['usuario_id']),
            'rol_id': int(request.form['rol_id'])
        }

        service = RolUsuarioService()
        if service.create(data):
            flash('Registro creado exitosamente', 'success')
            return redirect(url_for('rol_usuario.list'))
        else:
            flash('Error al crear el registro', 'error')

    usuario_service = UsuarioService()
    usuarios = usuario_service.get_all()
    rol_service = RolService()
    roles = rol_service.get_all()
    return render_template('rol_usuario/create.html', usuarios=usuarios, roles=roles, registro=None)


@rol_usuario_bp.route('/<int:usuario_id>/<int:rol_id>/edit', methods=['GET', 'POST'])
def edit(usuario_id, rol_id):
    """Editar un registro de rol_usuario."""
    service = RolUsuarioService()

    if request.method == 'POST':
        # Como es PK compuesta, no hay nada que actualizar
        # Solo redireccionamos con mensaje
        flash('La PK compuesta no se puede modificar. Elimine y cree un nuevo registro si necesita cambiar.', 'info')
        return redirect(url_for('rol_usuario.list'))

    registro = service.get_by_id(usuario_id, rol_id)
    if registro is None:
        flash('Registro no encontrado', 'error')
        return redirect(url_for('rol_usuario.list'))

    usuario_service = UsuarioService()
    usuarios = usuario_service.get_all()
    rol_service = RolService()
    roles = rol_service.get_all()
    
    return render_template('rol_usuario/edit.html', registro=registro, usuario_id=usuario_id, rol_id=rol_id, usuarios=usuarios, roles=roles)


@rol_usuario_bp.route('/<int:usuario_id>/<int:rol_id>/delete', methods=['POST'])
def delete(usuario_id, rol_id):
    """Eliminar un registro."""
    service = RolUsuarioService()

    if service.delete(usuario_id, rol_id):
        flash('Registro eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el registro', 'error')

    return redirect(url_for('rol_usuario.list'))