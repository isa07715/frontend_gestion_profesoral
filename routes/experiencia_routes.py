from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.experiencia_service import ExperienciaService
from services.docente_service import DocenteService

experiencia_bp = Blueprint('experiencia', __name__, url_prefix='/api/experiencia')

@experiencia_bp.route('/')
def list():
    service = ExperienciaService()
    experiencias = service.get_all()
    return render_template('experiencia/list.html', experiencias=experiencias if experiencias else [])

@experiencia_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'nombre_cargo': request.form['nombre_cargo'],
                'institucion': request.form['institucion'],
                'tipo': request.form['tipo'],
                'fecha_inicio': request.form.get('fecha_inicio') or None,
                'fecha_fin': request.form.get('fecha_fin') or None,
                'docente': int(request.form['docente'])
            }
            
            service = ExperienciaService()
            if service.create(data):
                flash('Experiencia creada exitosamente', 'success')
                return redirect(url_for('experiencia.list'))
            else:
                flash('Error al crear la experiencia', 'error')
                
        except ValueError:
            flash('Error: La cédula debe ser un número', 'error')
        except Exception as e:
            print(f"❌ Error: {e}")
            flash('Error al crear', 'error')

    docentes = DocenteService().get_all() or []
    return render_template('experiencia/create.html', docentes=docentes)

@experiencia_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = ExperienciaService()
    
    if request.method == 'POST':
        try:
            data = {
                'nombre_cargo': request.form['nombre_cargo'],
                'institucion': request.form['institucion'],
                'tipo': request.form['tipo'],
                'fecha_inicio': request.form.get('fecha_inicio') or None,
                'fecha_fin': request.form.get('fecha_fin') or None,
                'docente': int(request.form['docente'])
            }
            
            if service.update(id, data):
                flash('Experiencia actualizada exitosamente', 'success')
                return redirect(url_for('experiencia.list'))
            else:
                flash('Error al actualizar', 'error')
        except Exception as e:
            print(f"❌ Error: {e}")
            flash('Error al actualizar', 'error')

    experiencia = service.get_all()
    exp = next((e for e in experiencia if e.get('id') == id), None)
    docentes = DocenteService().get_all() or []
    
    return render_template('experiencia/edit.html', experiencia=exp, docentes=docentes)

@experiencia_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = ExperienciaService()
    if service.delete(id):
        flash('Experiencia eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('experiencia.list'))