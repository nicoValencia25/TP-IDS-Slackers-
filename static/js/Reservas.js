document.addEventListener('DOMContentLoaded', function() {
    const confirmarBtn = document.getElementById('boton_confirmar');
    const cancelarBtn = document.getElementById('cancelar_reserva');
    const precioPorAdulto = 100;
    const precioPorNino = 50;
    const cantidadAdultosInput = document.getElementById('cantidad_de_adultos');
    const cantidadNinosInput = document.getElementById('cantidad_de_niños');
    const totalElement = document.getElementById('total');



    confirmarBtn.addEventListener('click', function(event) {
        alert('Reserva Confirmada!!!!!');
        })
    cancelarBtn.addEventListener('click', function(event) {
        alert('Reserva Cancelada');
    })

    function actualizarPrecioTotal() {
        const cantidadAdultos = parseInt(cantidadAdultosInput.value) || 0;
        const cantidadNinos = parseInt(cantidadNinosInput.value) || 0;
        totalElement.Content = (cantidadAdultos * precioPorAdulto) + (cantidadNinos * precioPorNino);
    }
    cantidadAdultosInput.addEventListener('click', actualizarPrecioTotal);
    cantidadNinosInput.addEventListener('click', actualizarPrecioTotal);
    actualizarPrecioTotal();

});