"""
main_routes.py — Rutas principales (Home, About, Contact, etc.)
"""
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Página de inicio."""
    return render_template('index.html')


@main_bp.route('/about')
def about():
    """Página Sobre Nosotros."""
    return render_template('about.html')


@main_bp.route('/services')
def services():
    """Página de Servicios."""
    return render_template('services.html')


@main_bp.route('/contact')
def contact():
    """Página de Contacto."""
    return render_template('contact.html')