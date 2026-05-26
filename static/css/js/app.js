/**
 * app.js — JavaScript principal para el frontend.
 * Gestión Profesoral - Universidad
 */

// ============================================
// INICIALIZACIÓN
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('Gestión Profesoral - Frontend cargado');
    
    // Inicializar componentes
    initFlashMessages();
    initForms();
    initTables();
    initNavigation();
});

// ============================================
// FLASH MESSAGES
// ============================================

function initFlashMessages() {
    // Auto-ocultar mensajes flash después de 5 segundos
    const flashMessages = document.querySelectorAll('.flash-message');
    
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });
}

// ============================================
// FORMULARIOS
// ============================================

function initForms() {
    // Validación de formularios CRUD
    const forms = document.querySelectorAll('.crud-form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Validación personalizada si es necesaria
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                } else {
                    field.classList.remove('error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showFlashMessage('Por favor complete todos los campos requeridos', 'error');
            }
        });
    });
    
    // Confirmación en formularios de eliminación
    const deleteForms = document.querySelectorAll('form[onsubmit*="confirm"]');
    
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('¿Está seguro de que desea eliminar este registro?')) {
                e.preventDefault();
            }
        });
    });
}

// ============================================
// TABLAS
// ============================================

function initTables() {
    // Búsqueda en tablas
    const searchInputs = document.querySelectorAll('.table-search');
    
    searchInputs.forEach(input => {
        input.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const table = this.closest('.table-container').querySelector('.table');
            const rows = table.querySelectorAll('tbody tr');
            
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    });
    
    // Ordenamiento de columnas
    const sortableHeaders = document.querySelectorAll('.table th[data-sortable]');
    
    sortableHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const columnIndex = this.cellIndex;
            const table = this.closest('.table');
            const tbody = table.querySelector('tbody');
            const rows = Array.from(tbody.querySelectorAll('tr'));
            
            rows.sort((a, b) => {
                const aText = a.cells[columnIndex].textContent.trim();
                const bText = b.cells[columnIndex].textContent.trim();
                
                // Intentar comparar como números
                const aNum = parseFloat(aText);
                const bNum = parseFloat(bText);
                
                if (!isNaN(aNum) && !isNaN(bNum)) {
                    return aNum - bNum;
                }
                
                // Comparar como texto
                return aText.localeCompare(bText);
            });
            
            rows.forEach(row => tbody.appendChild(row));
        });
    });
}

// ============================================
// NAVEGACIÓN
// ============================================

function initNavigation() {
    // Menú responsive para móvil
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav ul');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Highlight de menú activo
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
}

// ============================================
// UTILIDADES
// ============================================

/**
 * Mostrar mensaje flash dinámicamente
 */
function showFlashMessage(message, type = 'info') {
    const container = document.querySelector('.flash-messages') || createFlashContainer();
    
    const flash = document.createElement('div');
    flash.className = flash-message flash-${type};
    flash.innerHTML = `
        ${message}
        <button class="flash-close" onclick="this.parentElement.remove()">×</button>
    `;
    
    container.appendChild(flash);
    
    // Auto-ocultar después de 5 segundos
    setTimeout(() => {
        flash.style.opacity = '0';
        setTimeout(() => flash.remove(), 300);
    }, 5000);
}

/**
 * Crear contenedor de flash messages si no existe
 */
function createFlashContainer() {
    const container = document.createElement('div');
    container.className = 'flash-messages container';
    
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.insertBefore(container, mainContent.firstChild);
    } else {
        document.body.insertBefore(container, document.body.firstChild);
    }
    
    return container;
}

/**
 * Formatear fecha para mostrar
 */
function formatDate(dateString) {
    if (!dateString) return 'N/A';
    
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('es-CO', options);
}

/**
 * Formatear número con separadores de miles
 */
function formatNumber(number) {
    if (number === null || number === undefined) return 'N/A';
    
    return new Intl.NumberFormat('es-CO').format(number);
}

/**
 * Validar email
 */
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

/**
 * Confirmar acción peligrosa
 */
function confirmAction(message = '¿Está seguro de realizar esta acción?') {
    return confirm(message);
}

// ============================================
// API CLIENT (JavaScript)
// ============================================

const API_BASE_URL = 'http://localhost:8000';

/**
 * Hacer petición GET a la API
 */
async function apiGet(endpoint) {
    try {
        const response = await fetch(${API_BASE_URL}${endpoint}, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        
        if (!response.ok) {
            throw new Error(HTTP error! status: ${response.status});
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error en API GET:', error);
        showFlashMessage('Error al cargar datos', 'error');
        return null;
    }
}

/**
 * Hacer petición POST a la API
 */
async function apiPost(endpoint, data) {
    try {
        const response = await fetch(${API_BASE_URL}${endpoint}, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        
        if (!response.ok) {
            throw new Error(HTTP error! status: ${response.status});
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error en API POST:', error);
        showFlashMessage('Error al guardar datos', 'error');
        return null;
    }
}

/**
 * Hacer petición PUT a la API
 */
async function apiPut(endpoint, data) {
    try {
        const response = await fetch(${API_BASE_URL}${endpoint}, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        
        if (!response.ok) {
            throw new Error(HTTP error! status: ${response.status});
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error en API PUT:', error);
        showFlashMessage('Error al actualizar datos', 'error');
        return null;
    }
}

/**
 * Hacer petición DELETE a la API
 */
async function apiDelete(endpoint) {
    try {
        const response = await fetch(${API_BASE_URL}${endpoint}, {
            method: 'DELETE',
        });
        
        return response.ok;
    } catch (error) {
        console.error('Error en API DELETE:', error);
        showFlashMessage('Error al eliminar datos', 'error');
        return false;
    }
}

// ============================================
// EXPORTAR FUNCIONES (para usar en otros JS)
// ============================================

window.GestionProfesoral = {
    showFlashMessage,
    formatDate,
    formatNumber,
    isValidEmail,
    confirmAction,
    api: {
        get: apiGet,
        post: apiPost,
        put: apiPut,
        delete: apiDelete,
    },
};