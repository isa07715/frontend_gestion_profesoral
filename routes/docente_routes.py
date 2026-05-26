"""
docente_routes.py - Rutas CRUD para docente.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.docente_service import DocenteService
from services.linea_investigacion_service import LineaInvestigacionService  # ✅ Import corregido

docente_bp = Blueprint('docente', __name__, url_prefix='/api/docente')


@docente_bp.route('/')
def list():
    service = DocenteService()
    docentes = service.get_all()
    return render_template('docente/list.html', docentes=docentes)


@docente_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'cedula': int(request.form['cedula']),
            'nombres': request.form['nombres'],
            'apellidos': request.form['apellidos'],
            'genero': request.form['genero'],
            'cargo': request.form['cargo'],
            'fecha_nacimiento': request.form['fecha_nacimiento'],
            'correo': request.form['correo'],
            'telefono': request.form['telefono'],
            'url_cvlac': request.form['url_cvlac'],
            'fecha_actualizacion': request.form['fecha_actualizacion'],
            'escalafon': request.form['escalafon'],
            'perfil': request.form['perfil'],
            'cat_minciencia': request.form.get('cat_minciencia', ''),
            'conv_minciencia': request.form['conv_minciencia'],
            'nacionalidaad': request.form['nacionalidaad'],
            'linea_investigacion_principal': int(request.form['linea_investigacion_principal']) if request.form.get('linea_investigacion_principal') else None
        }
        service = DocenteService()
        if service.create(data):
            flash('Docente creado exitosamente', 'success')
            return redirect(url_for('docente.list'))
        else:
            flash('Error al crear el docente', 'error')

    # ✅ Usar LineaInvestigacionService (no Servicio)
    li_service = LineaInvestigacionService()
    lineas = li_service.get_all()
    return render_template('docente/create.html', lineas=lineas, registro=None)


@docente_bp.route('/<int:cedula>')
def detail(cedula):
    service = DocenteService()
    docente = service.get_by_id(cedula)
    if docente is None:
        flash('Docente no encontrado', 'error')
        return redirect(url_for('docente.list'))
    return render_template('docente/detail.html', docente=docente)


@docente_bp.route('/<int:cedula>/edit', methods=['GET', 'POST'])
def edit(cedula):
    service = DocenteService()
    if request.method == 'POST':
        data = {
            'cedula': int(request.form['cedula']),
            'nombres': request.form['nombres'],
            'apellidos': request.form['apellidos'],
            'genero': request.form['genero'],
            'cargo': request.form['cargo'],
            'fecha_nacimiento': request.form['fecha_nacimiento'],
            'correo': request.form['correo'],
            'telefono': request.form['telefono'],
            'url_cvlac': request.form['url_cvlac'],
            'fecha_actualizacion': request.form['fecha_actualizacion'],
            'escalafon': request.form['escalafon'],
            'perfil': request.form['perfil'],
            'cat_minciencia': request.form.get('cat_minciencia', ''),
            'conv_minciencia': request.form['conv_minciencia'],
            'nacionalidaad': request.form['nacionalidaad'],
            'linea_investigacion_principal': int(request.form['linea_investigacion_principal']) if request.form.get('linea_investigacion_principal') else None
        }
        if service.update(cedula, data):
            flash('Docente actualizado exitosamente', 'success')
            return redirect(url_for('docente.list'))
        else:
            flash('Error al actualizar el docente', 'error')

    docente = service.get_by_id(cedula)
    if docente is None:
        flash('Docente no encontrado', 'error')
        return redirect(url_for('docente.list'))

    # ✅ Usar LineaInvestigacionService (no Servicio)
    li_service = LineaInvestigacionService()
    lineas = li_service.get_all()
    return render_template('docente/edit.html', docente=docente, lineas=lineas, registro=docente)


@docente_bp.route('/<int:cedula>/delete', methods=['POST'])
def delete(cedula):
    service = DocenteService()
    if service.delete(cedula):
        flash('Docente eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el docente', 'error')
    return redirect(url_for('docente.list'))