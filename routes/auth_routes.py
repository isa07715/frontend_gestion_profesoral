"""
auth_routes.py — Rutas de autenticación (login, logout)
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.api_client import get_api_client

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Consumir API de login
        api = get_api_client()
        response = api.post('/api/login', {
            'username': username,
            'password': password
        })
        
        if response and 'access_token' in response:
            # Guardar token en sesión
            session['token'] = response['access_token']
            session['user'] = response.get('user', {})
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Credenciales inválidas', 'error')
    
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    """Cerrar sesión."""
    session.pop('token', None)
    session.pop('user', None)
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('main.index'))