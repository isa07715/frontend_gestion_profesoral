// frontend/static/js/app.js
console.log('✅ app.js cargado correctamente');

document.addEventListener('DOMContentLoaded', function() {
    console.log('📄 DOM listo');
    
    // Validación básica de formularios
    const forms = document.querySelectorAll('form.crud-form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const required = this.querySelectorAll('[required]');
            let valid = true;
            required.forEach(field => {
                if (!field.value.trim()) {
                    valid = false;
                    field.style.borderColor = 'red';
                } else {
                    field.style.borderColor = '';
                }
            });
            if (!valid) {
                e.preventDefault();
                alert('Por favor completa los campos obligatorios');
            }
        });
    });
});