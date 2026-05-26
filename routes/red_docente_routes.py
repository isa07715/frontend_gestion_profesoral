from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.red_docente_service import RedDocenteService
from services.red_service import RedService
from services.docente_service import DocenteService

red_docente_bp = Blueprint('red_docente', __name__, url_prefix='/api/red_docente')


@red_docente_bp.route('/')
def list():
    service = RedDocenteService()
    registros = service.get_all()
    return render_template('red_docente/list.html', registros=registros)


@red_docente_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'red': int(request.form['red']),
            'docente': int(request.form['docente']),
            'fecha_inicio': request.form['fecha_inicio'],
            'fecha_fin': request.form.get('fecha_fin', '') or None,
            'act_destacadas': request.form['act_destacadas']
        }
        service = RedDocenteService()
        if service.create(data):
            flash('Registro creado exitosamente', 'success')
            return redirect(url_for('red_docente.list'))
        else:
            flash('Error al crear el registro', 'error')

    red_service = RedService()
    redes = red_service.get_all()
    docente_service = DocenteService()
    docentes = docente_service.get_all()
    return render_template('red_docente/create.html', redes=redes, docentes=docentes, registro=None)


@red_docente_bp.route('/<int:red>/<int:docente>')
def detail(red, docente):
    service = RedDocenteService()
    registro = service.get_by_id(red, docente)
    if registro is None:
        flash('Registro no encontrado', 'error')
        return redirect(url_for('red_docente.list'))
    return render_template('red_docente/detail.html', registro=registro, red=red, docente=docente)


@red_docente_bp.route('/<int:red>/<int:docente>/edit', methods=['GET', 'POST'])
def edit(red, docente):
    service = RedDocenteService()
    if request.method == 'POST':
        data = {
            'fecha_inicio': request.form['fecha_inicio'],
            'fecha_fin': request.form.get('fecha_fin', '') or None,
            'act_destacadas': request.form['act_destacadas']
        }
        if service.update(red, docente, data):
            flash('Registro actualizado exitosamente', 'success')
            return redirect(url_for('red_docente.list'))
        else:
            flash('Error al actualizar el registro', 'error')

    registro = service.get_by_id(red, docente)
    if registro is None:
        flash('Registro no encontrado', 'error')
        return redirect(url_for('red_docente.list'))

    red_service = RedService()
    redes = red_service.get_all()
    docente_service = DocenteService()
    docentes = docente_service.get_all()
    return render_template('red_docente/edit.html', registro=registro, red=red, docente=docente, redes=redes, docentes=docentes)


@red_docente_bp.route('/<int:red>/<int:docente>/delete', methods=['POST'])
def delete(red, docente):
    service = RedDocenteService()
    if service.delete(red, docente):
        flash('Registro eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el registro', 'error')
    return redirect(url_for('red_docente.list'))