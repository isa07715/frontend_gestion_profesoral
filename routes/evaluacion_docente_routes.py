from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.evaluacion_docente_service import EvaluacionDocenteService
from services.docente_service import DocenteService

evaluacion_docente_bp = Blueprint('evaluacion_docente', __name__, url_prefix='/api/evaluacion_docente')


@evaluacion_docente_bp.route('/')
def list():
    service = EvaluacionDocenteService()
    evaluaciones = service.get_all()
    return render_template('evaluacion_docente/list.html', evaluaciones=evaluaciones)


@evaluacion_docente_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'calificacion': float(request.form['calificacion']),
            'semestre': request.form['semestre'],
            'docente': int(request.form['docente'])
        }
        service = EvaluacionDocenteService()
        if service.create(data):
            flash('Evaluacion creada exitosamente', 'success')
            return redirect(url_for('evaluacion_docente.list'))
        else:
            flash('Error al crear la evaluacion', 'error')

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    return render_template('evaluacion_docente/create.html', docentes=docentes, registro=None)


@evaluacion_docente_bp.route('/<int:id>')
def detail(id):
    service = EvaluacionDocenteService()
    evaluacion = service.get_by_id(id)
    if evaluacion is None:
        flash('Evaluacion no encontrada', 'error')
        return redirect(url_for('evaluacion_docente.list'))
    return render_template('evaluacion_docente/detail.html', evaluacion=evaluacion)


@evaluacion_docente_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = EvaluacionDocenteService()
    if request.method == 'POST':
        data = {
            'calificacion': float(request.form['calificacion']),
            'semestre': request.form['semestre'],
            'docente': int(request.form['docente'])
        }
        if service.update(id, data):
            flash('Evaluacion actualizada exitosamente', 'success')
            return redirect(url_for('evaluacion_docente.list'))
        else:
            flash('Error al actualizar la evaluacion', 'error')

    evaluacion = service.get_by_id(id)
    if evaluacion is None:
        flash('Evaluacion no encontrada', 'error')
        return redirect(url_for('evaluacion_docente.list'))

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    return render_template('evaluacion_docente/edit.html', evaluacion=evaluacion, docentes=docentes, registro=evaluacion)


@evaluacion_docente_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = EvaluacionDocenteService()
    if service.delete(id):
        flash('Evaluacion eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar la evaluacion', 'error')
    return redirect(url_for('evaluacion_docente.list'))