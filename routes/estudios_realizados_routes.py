from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.estudios_realizados_service import EstudiosRealizadosService
from services.docente_service import DocenteService

estudios_realizados_bp = Blueprint('estudios_realizados', __name__, url_prefix='/api/estudios_realizados')


@estudios_realizados_bp.route('/')
def list():
    service = EstudiosRealizadosService()
    estudios = service.get_all()
    # Evita TypeError: 'NoneType' object is not iterable en el template
    if estudios is None:
        estudios = []
    return render_template('estudios_realizados/list.html', estudios=estudios)


@estudios_realizados_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            # 1. Campos obligatorios (siempre se envían)
            data = {
                'titulo': request.form['titulo'].strip(),
                'universidad': request.form['universidad'].strip(),
                'tipo': request.form['tipo'].strip(),
                'docente': int(request.form['docente']),
                'ins_acreditada': int(request.form.get('ins_acreditada', 0))
            }

            # 2. Campos opcionales: SOLO se agregan si el usuario escribió algo
            # Esto evita enviar "" o None que causan el error 422 en Pydantic
            if request.form.get('fecha'):
                data['fecha'] = request.form['fecha']
                
            if request.form.get('ciudad'):
                data['ciudad'] = request.form['ciudad'].strip()
                
            if request.form.get('pais'):
                data['pais'] = request.form['pais'].strip()
                
            if request.form.get('metodologia'):
                data['metodologia'] = request.form['metodologia'].strip()
                
            # ⚠️ IMPORTANTE: Si tu modelo Pydantic NO tiene 'perfil_egresado', 
            # el backend rechazará el request. Solo lo enviamos si existe en el form.
            if request.form.get('perfil_egresado'):
                data['perfil_egresado'] = request.form['perfil_egresado'].strip()

            print(f"📤 Datos enviados a API: {data}")  # Para depurar en consola

            service = EstudiosRealizadosService()
            if service.create(data):
                flash('Estudio creado exitosamente', 'success')
                return redirect(url_for('estudios_realizados.list'))
            else:
                flash('Error al crear el estudio. Verifica los datos.', 'error')

        except ValueError:
            flash('Error: La cédula del docente debe ser un número válido.', 'error')
        except Exception as e:
            print(f"❌ Error en create estudios_realizados: {e}")
            flash('Error inesperado al crear el estudio.', 'error')

    # Cargar docentes para el select
    docente_service = DocenteService()
    docentes = docente_service.get_all()
    if docentes is None: docentes = []
    
    return render_template('estudios_realizados/create.html', docentes=docentes, registro=None)


@estudios_realizados_bp.route('/<int:id>')
def detail(id):
    service = EstudiosRealizadosService()
    estudio = service.get_by_id(id)
    if estudio is None:
        flash('Estudio no encontrado', 'error')
        return redirect(url_for('estudios_realizados.list'))
    return render_template('estudios_realizados/detail.html', estudio=estudio)


@estudios_realizados_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    service = EstudiosRealizadosService()
    
    if request.method == 'POST':
        try:
            # Mismo filtro seguro que en create
            data = {
                'titulo': request.form['titulo'].strip(),
                'universidad': request.form['universidad'].strip(),
                'tipo': request.form['tipo'].strip(),
                'docente': int(request.form['docente']),
                'ins_acreditada': int(request.form.get('ins_acreditada', 0))
            }

            if request.form.get('fecha'):
                data['fecha'] = request.form['fecha']
            if request.form.get('ciudad'):
                data['ciudad'] = request.form['ciudad'].strip()
            if request.form.get('pais'):
                data['pais'] = request.form['pais'].strip()
            if request.form.get('metodologia'):
                data['metodologia'] = request.form['metodologia'].strip()
            if request.form.get('perfil_egresado'):
                data['perfil_egresado'] = request.form['perfil_egresado'].strip()

            # El ID ya viene de la URL (def edit(id)), no del form
            if service.update(id, data):
                flash('Estudio actualizado exitosamente', 'success')
                return redirect(url_for('estudios_realizados.list'))
            else:
                flash('Error al actualizar el estudio.', 'error')

        except ValueError:
            flash('Error: La cédula del docente debe ser un número válido.', 'error')
        except Exception as e:
            print(f"❌ Error en edit estudios_realizados: {e}")
            flash('Error inesperado al actualizar.', 'error')

    # GET: Cargar datos actuales
    estudio = service.get_by_id(id)
    if estudio is None:
        flash('Estudio no encontrado', 'error')
        return redirect(url_for('estudios_realizados.list'))

    docente_service = DocenteService()
    docentes = docente_service.get_all()
    if docentes is None: docentes = []
    
    return render_template('estudios_realizados/edit.html', estudio=estudio, docentes=docentes, registro=estudio)


@estudios_realizados_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    service = EstudiosRealizadosService()
    try:
        if service.delete(id):
            flash('Estudio eliminado exitosamente', 'success')
        else:
            flash('No se pudo eliminar el estudio.', 'error')
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")
        flash('Error al eliminar el estudio.', 'error')
    return redirect(url_for('estudios_realizados.list'))