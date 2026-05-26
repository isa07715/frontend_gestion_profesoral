from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.linea_investigacion_service import LineaInvestigacionService

linea_investigacion_bp = Blueprint('linea_investigacion', __name__, url_prefix='/api/linea_investigacion')

@linea_investigacion_bp.route('/')
def list():
    service = LineaInvestigacionService()
    lineas = service.get_all()
    return render_template('linea_investigacion/list.html', lineas=lineas if lineas else [])

@linea_investigacion_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'nombre': request.form['nombre'],
                'descripcion': request.form['descripcion']
            }
            
            service = LineaInvestigacionService()
            if service.create(data):
                flash('Línea creada exitosamente', 'success')
                return redirect(url_for('linea_investigacion.list'))
            else:
                flash('Error al crear la línea', 'error')
                
        except Exception as e:
            print(f"❌ Error: {e}")
            flash('Error al crear', 'error')
    
    return render_template('linea_investigacion/create.html')

@linea_investigacion_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = LineaInvestigacionService()
    
    if request.method == 'POST':
        try:
            data = {
                'nombre': request.form['nombre'],
                'descripcion': request.form['descripcion']
            }
            
            if service.update(id, data):
                flash('Línea actualizada exitosamente', 'success')
                return redirect(url_for('linea_investigacion.list'))
            else:
                flash('Error al actualizar', 'error')
        except Exception as e:
            flash('Error al actualizar', 'error')

    lineas = service.get_all()
    linea = next((l for l in lineas if l.get('id') == id), None)
    
    return render_template('linea_investigacion/edit.html', linea=linea)

@linea_investigacion_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = LineaInvestigacionService()
    if service.delete(id):
        flash('Línea eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar', 'error')
    return redirect(url_for('linea_investigacion.list'))