from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.docente_departamento_service import DocenteDepartamentoService
from services.docente_service import DocenteService
from services.programa_service import ProgramaService

docente_departamento_bp = Blueprint('docente_departamento', __name__, url_prefix='/api/docente_departamento')


@docente_departamento_bp.route('/')
def list():
    service = DocenteDepartamentoService()
    registros = service.get_all()
    return render_template('docente_departamento/list.html', registros=registros)


@docente_departamento_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'docente': int(request.form['docente']),
            'departamento': int(request.form['departamento']),
            'dedicacion': request.form['dedicacion'],
            'modalidad': request.form['modalidad'],
            'fecha_ingreso': request.form['fecha_ingreso'],
            'fecha_salida': request.form.get('fecha_salida', '') or None
        }
        service = DocenteDepartamentoService()
        if service.create(data):
            flash('Registro creado exitosamente', 'success')
            return redirect(url_for('docente_departamento.list'))
        else:
            flash('Error al crear el registro', 'error')

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    programa_service = ProgramaService()
    programas = programa_service.get_all()
    return render_template('docente_departamento/create.html', docentes=docentes, programas=programas, registro=None)


@docente_departamento_bp.route('/<int:docente>/<int:departamento>')
def detail(docente, departamento):
    service = DocenteDepartamentoService()
    registro = service.get_by_id(docente, departamento)
    if registro is None:
        flash('Registro no encontrado', 'error')
        return redirect(url_for('docente_departamento.list'))
    return render_template('docente_departamento/detail.html', registro=registro, docente=docente, departamento=departamento)


@docente_departamento_bp.route('/<int:docente>/<int:departamento>/edit', methods=['GET', 'POST'])
def edit(docente, departamento):
    service = DocenteDepartamentoService()
    if request.method == 'POST':
        data = {
            'dedicacion': request.form['dedicacion'],
            'modalidad': request.form['modalidad'],
            'fecha_ingreso': request.form['fecha_ingreso'],
            'fecha_salida': request.form.get('fecha_salida', '') or None
        }
        if service.update(docente, departamento, data):
            flash('Registro actualizado exitosamente', 'success')
            return redirect(url_for('docente_departamento.list'))
        else:
            flash('Error al actualizar el registro', 'error')

    registro = service.get_by_id(docente, departamento)
    if registro is None:
        flash('Registro no encontrado', 'error')
        return redirect(url_for('docente_departamento.list'))

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    programa_service = ProgramaService()
    programas = programa_service.get_all()
    return render_template('docente_departamento/edit.html', registro=registro, docente=docente, departamento=departamento, docentes=docentes, programas=programas)


@docente_departamento_bp.route('/<int:docente>/<int:departamento>/delete', methods=['POST'])
def delete(docente, departamento):
    service = DocenteDepartamentoService()
    if service.delete(docente, departamento):
        flash('Registro eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el registro', 'error')
    return redirect(url_for('docente_departamento.list'))