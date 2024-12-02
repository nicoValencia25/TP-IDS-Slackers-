document.addEventListener('DOMContentLoaded', function() {
    const confirmarBtn = document.getElementById('boton_confirmar');
    const cancelarBtn = document.getElementById('cancelar_reserva');


    confirmarBtn.addEventListener('click', function(event) {
        alert('Reserva Confirmada!!!!!');
        })
    cancelarBtn.addEventListener('click', function(event) {
        alert('Reserva Cancelada');
    })
});