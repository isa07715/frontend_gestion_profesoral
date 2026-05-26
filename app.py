"""
app.py - Aplicacion Flask para el frontend.
"""
from flask import Flask, render_template
from routes.area_conocimiento_routes import area_conocimiento_bp
from routes.termino_clave_routes import termino_clave_bp
from routes.linea_investigacion_routes import linea_investigacion_bp
from routes.programa_routes import programa_bp
from routes.red_routes import red_bp
from routes.docente_routes import docente_bp
from routes.estudios_realizados_routes import estudios_realizados_bp
from routes.docente_departamento_routes import docente_departamento_bp
from routes.intereses_futuros_routes import intereses_futuros_bp
from routes.evaluacion_docente_routes import evaluacion_docente_bp
from routes.reconocimiento_routes import reconocimiento_bp
from routes.experiencia_routes import experiencia_bp
from routes.red_docente_routes import red_docente_bp
from routes.estudio_ac_routes import estudio_ac_bp
from routes.apoyo_profesoral_routes import apoyo_profesoral_bp
from routes.beca_routes import beca_bp
from routes.rol_routes import rol_bp
from routes.usuario_routes import usuario_bp
from routes.rol_usuario_routes import rol_usuario_bp



app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'gestion-profesoral-secret-key-2026'

# Registrar blueprints
app.register_blueprint(area_conocimiento_bp)
app.register_blueprint(termino_clave_bp)
app.register_blueprint(linea_investigacion_bp)
app.register_blueprint(programa_bp)
app.register_blueprint(red_bp)
app.register_blueprint(docente_bp)
app.register_blueprint(estudios_realizados_bp)
app.register_blueprint(docente_departamento_bp)
app.register_blueprint(intereses_futuros_bp)
app.register_blueprint(evaluacion_docente_bp)
app.register_blueprint(reconocimiento_bp)
app.register_blueprint(experiencia_bp) 
app.register_blueprint(red_docente_bp)
app.register_blueprint(estudio_ac_bp)
app.register_blueprint(apoyo_profesoral_bp)
app.register_blueprint(beca_bp) 
app.register_blueprint(rol_bp)  
app.register_blueprint(usuario_bp)  
app.register_blueprint(rol_usuario_bp)


@app.route('/')
def index():
    """Pagina de inicio."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Pagina sobre nosotros."""
    return render_template('about.html')


@app.route('/services')
def services():
    """Pagina de servicios."""
    return render_template('services.html')


@app.route('/contact')
def contact():
    """Pagina de contacto."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)