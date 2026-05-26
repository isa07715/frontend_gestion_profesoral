from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.reconocimiento_service import ReconocimientoService
from services.docente_service import DocenteService

reconocimiento_bp = Blueprint('reconocimiento', __name__, url_prefix='/api/reconocimiento')


@reconocimiento_bp.route('/')
def list():
    service = ReconocimientoService()
    reconocimientos = service.get_all()
    return render_template('reconocimiento/list.html', reconocimientos=reconocimientos)


@reconocimiento_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'tipo': request.form['tipo'],
            'fecha': request.form['fecha'],
            'institucion': request.form['institucion'],
            'nombre': request.form['nombre'],
            'ambito': request.form['ambito'],
            'docente': int(request.form['docente'])
        }
        service = ReconocimientoService()
        if service.create(data):
            flash('Reconocimiento creado exitosamente', 'success')
            return redirect(url_for('reconocimiento.list'))
        else:
            flash('Error al crear el reconocimiento', 'error')

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    return render_template('reconocimiento/create.html', docentes=docentes, registro=None)


@reconocimiento_bp.route('/<int:id>')
def detail(id):
    service = ReconocimientoService()
    reconocimiento = service.get_by_id(id)
    if reconocimiento is None:
        flash('Reconocimiento no encontrado', 'error')
        return redirect(url_for('reconocimiento.list'))
    return render_template('reconocimiento/detail.html', reconocimiento=reconocimiento)


@reconocimiento_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = ReconocimientoService()
    if request.method == 'POST':
        data = {
            'tipo': request.form['tipo'],
            'fecha': request.form['fecha'],
            'institucion': request.form['institucion'],
            'nombre': request.form['nombre'],
            'ambito': request.form['ambito'],
            'docente': int(request.form['docente'])
        }
        if service.update(id, data):
            flash('Reconocimiento actualizado exitosamente', 'success')
            return redirect(url_for('reconocimiento.list'))
        else:
            flash('Error al actualizar el reconocimiento', 'error')

    reconocimiento = service.get_by_id(id)
    if reconocimiento is None:
        flash('Reconocimiento no encontrado', 'error')
        return redirect(url_for('reconocimiento.list'))

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    return render_template('reconocimiento/edit.html', reconocimiento=reconocimiento, docentes=docentes, registro=reconocimiento)


@reconocimiento_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = ReconocimientoService()
    if service.delete(id):
        flash('Reconocimiento eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el reconocimiento', 'error')
    return redirect(url_for('reconocimiento.list'))