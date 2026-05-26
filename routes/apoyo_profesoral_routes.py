from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.apoyo_profesoral_service import ApoyoProfesoralService
from services.estudios_realizados_service import EstudiosRealizadosService

apoyo_profesoral_bp = Blueprint('apoyo_profesoral', __name__, url_prefix='/api/apoyo_profesoral')

@apoyo_profesoral_bp.route('/')
def list():
    service = ApoyoProfesoralService()
    apoyos = service.get_all()
    return render_template('apoyo_profesoral/list.html', apoyos=apoyos if apoyos else [])

@apoyo_profesoral_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'estudios': int(request.form['estudios']),
                'con_apoyo': int(request.form['con_apoyo']),
                'institucion': request.form['institucion'],
                'tipo': request.form['tipo']
            }
            
            service = ApoyoProfesoralService()
            if service.create(data):
                flash('Apoyo creado/actualizado exitosamente', 'success')
                return redirect(url_for('apoyo_profesoral.list'))
            else:
                flash('Error al guardar el apoyo', 'error')
                
        except ValueError:
            flash('Error: El ID del estudio debe ser un número', 'error')
        except Exception as e:
            print(f" Error: {e}")
            flash('Error inesperado', 'error')

    # Cargar la lista de estudios realizados para el dropdown
    estudios_list = EstudiosRealizadosService().get_all() or []
    
    return render_template('apoyo_profesoral/create.html', estudios_list=estudios_list)

@apoyo_profesoral_bp.route('/<int:estudios_id>/edit', methods=['GET', 'POST'])
def edit(estudios_id):
    service = ApoyoProfesoralService()
    
    if request.method == 'POST':
        try:
            data = {
                'estudios': int(request.form['estudios']), # Debe coincidir con studies_id
                'con_apoyo': int(request.form['con_apoyo']),
                'institucion': request.form['institucion'],
                'tipo': request.form['tipo']
            }
            
            if service.update(estudios_id, data):
                flash('Apoyo actualizado exitosamente', 'success')
                return redirect(url_for('apoyo_profesoral.list'))
            else:
                flash('Error al actualizar', 'error')
        except Exception as e:
            print(f"❌ Error: {e}")
            flash('Error al actualizar', 'error')

    # Buscar el apoyo actual
    apoyo_actual = service.get_all()
    apoyo = next((a for a in apoyo_actual if a.get('estudios') == estudios_id), None)
    
    estudios_list = EstudiosRealizadosService().get_all() or []
    
    return render_template('apoyo_profesoral/edit.html', apoyo=apoyo, estudios_list=estudios_list, estudios_id=estudios_id)

@apoyo_profesoral_bp.route('/<int:estudios_id>/delete', methods=['POST'])
def delete(estudios_id):
    service = ApoyoProfesoralService()
    if service.delete(estudios_id):
        flash('Apoyo eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('apoyo_profesoral.list'))