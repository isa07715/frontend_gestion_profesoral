from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.beca_service import BecaService
from services.estudios_realizados_service import EstudiosRealizadosService

beca_bp = Blueprint('beca', __name__, url_prefix='/api/beca')

@beca_bp.route('/')
def list():
    service = BecaService()
    becas = service.get_all()
    return render_template('beca/list.html', becas=becas if becas else [])

@beca_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'estudios': int(request.form['estudios']),
                'tipo': request.form['tipo'],
                'institucion': request.form['institucion'],
                'fecha_inicio': request.form.get('fecha_inicio') or None,
                'fecha_fin': request.form.get('fecha_fin') or None
            }
            
            service = BecaService()
            if service.create(data):
                flash('Beca creada/actualizada exitosamente', 'success')
                return redirect(url_for('beca.list'))
            else:
                flash('Error al guardar la beca', 'error')
        except Exception as e:
            print(f"❌ Error: {e}")
            flash('Error inesperado', 'error')

    estudios_list = EstudiosRealizadosService().get_all() or []
    return render_template('beca/create.html', estudios_list=estudios_list)

@beca_bp.route('/<int:estudios_id>/delete', methods=['POST'])
def delete(estudios_id):
    service = BecaService()
    if service.delete(estudios_id):
        flash('Beca eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('beca.list'))