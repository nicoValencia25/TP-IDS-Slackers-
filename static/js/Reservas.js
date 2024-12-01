document.addEventListener('DOMContentLoaded', function() {
    // Lista de rangos de fechas ocupadas en formato 'formato_salida = "%Y-%m-%d %H:%M:%S"'
    fetch('/fechas_ocupadas')
        .then(response => response.json())
        .then(data => {
            const fechasOcupadas = data;

            const fechaDesdeInput = document.getElementById('reserva_desde');
            const fechaHastaInput = document.getElementById('reserva_hasta');

            function esFechaOcupada(fecha) {
        return fechasOcupadas.some(function(rango) {
            return fecha >= rango.Desde && fecha <= rango.Hasta;
        });
    }

    fechaDesdeInput.addEventListener('input', function() {
        const fechaDesdeSeleccionada = fechaDesdeInput.value;
        if (esFechaOcupada(fechaDesdeSeleccionada)) {
            alert('La fecha de inicio seleccionada está dentro de un rango ocupado. Por favor, selecciona otra.');
            fechaDesdeInput.value = ''; // Limpia el campo de fecha
        }
    });

    fechaHastaInput.addEventListener('input', function() {
        const fechaHastaSeleccionada = fechaHastaInput.value;
        if (esFechaOcupada(fechaHastaSeleccionada)) {
            alert('La fecha de fin seleccionada está dentro de un rango ocupado. Por favor, selecciona otra.');
            fechaHastaInput.value = ''; // Limpia el campo de fecha
        }
    });

});
})
