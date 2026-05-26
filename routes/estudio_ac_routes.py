from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.estudio_ac_service import EstudioACService
from services.estudios_realizados_service import EstudiosRealizadosService
from services.area_conocimiento_service import AreaConocimientoService

estudio_ac_bp = Blueprint('estudio_ac', __name__, url_prefix='/api/estudio_ac')


@estudio_ac_bp.route('/')
def list():
    service = EstudioACService()
    registros = service.get_all()
    return render_template('estudio_ac/list.html', registros=registros)


@estudio_ac_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = {
            'estudio': int(request.form['estudio']),
            'area_conocimiento': int(request.form['area_conocimiento'])
        }
        service = EstudioACService()
        if service.create(data):
            flash('Registro creado exitosamente', 'success')
            return redirect(url_for('estudio_ac.list'))
        else:
            flash('Error al crear el registro', 'error')

    estudio_service = EstudiosRealizadosService()
    estudios = estudio_service.get_all()
    area_service = AreaConocimientoService()
    areas = area_service.get_all()
    return render_template('estudio_ac/create.html', estudios=estudios, areas=areas, registro=None)


@estudio_ac_bp.route('/<int:estudio>/<int:area_conocimiento>')
def detail(estudio, area_conocimiento):
    service = EstudioACService()
    registro = service.get_by_id(estudio, area_conocimiento)
    if registro is None:
        flash('Registro no encontrado', 'error')
        return redirect(url_for('estudio_ac.list'))
    return render_template('estudio_ac/detail.html', registro=registro, estudio=estudio, area_conocimiento=area_conocimiento)


@estudio_ac_bp.route('/<int:estudio>/<int:area_conocimiento>/delete', methods=['POST'])
def delete(estudio, area_conocimiento):
    service = EstudioACService()
    if service.delete(estudio, area_conocimiento):
        flash('Registro eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el registro', 'error')
    return redirect(url_for('estudio_ac.list'))