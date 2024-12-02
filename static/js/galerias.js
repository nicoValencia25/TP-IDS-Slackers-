// Inicializa la galería del hotel (sus id son las mismas pero sin un número identificador al final ej: 'contenedorImagenes')
InicializarGaleria("")

//Abre el modal correspondiente según la id que pase como parámetro el evento onclick asignado dinámicamente a cada nombre del tipo de habitación
function Abrir(tipoID) {
    const modal = document.querySelector(`#modalHabitacion${tipoID}`)
    modal.style.display = 'flex'
    InicializarGaleria(tipoID)
}

//Cierra el modal correspondiente según la id que pase como parámetro el evento onclick asignado dinámicamente a cada "X" del modal
function Cerrar(tipoID) {
    const modal = document.querySelector(`#modalHabitacion${tipoID}`)
    modal.style.display = 'none'
}

//Cierra el modal actual si se hace click por fuera del contenido del mismo
window.addEventListener("click", (e) => {
    if (e.target.classList.contains('modal')) {
        e.target.style.display = 'none'
    }
})

function InicializarGaleria(tipoID) {
    //Asigna elementos del DOM dinámicamente
    const contenedor = document.getElementById(`contenedorImagenes${tipoID}`)
    const mostrarImagenes = document.getElementById(`mostrarImagenes${tipoID}`)
    const contador = document.getElementById(`contador${tipoID}`)
    const hijos = contenedor.children
    let index = 0
    const hijosCantidad = hijos.length

    //Te lleva a la imágen anterior, si estás en la primera imágen te lleva a la última
    function DeslizarIzquierda() {
        index = (index > 0) ? index - 1 : hijosCantidad - 1
        MostrarImagen(index)
    }

    //Te lleva a la imágen siguiente, si estás en la última imágen te lleva a la primera
    function DeslizarDerecha() {
        index = (index < hijosCantidad - 1) ? index + 1 : 0
        MostrarImagen(index)
    }

    //Actualiza la imágen a mostrar y el contador
    function MostrarImagen(index) {
        mostrarImagenes.src = hijos[index].getAttribute('src')
        contador.innerHTML = `${index + 1} / ${hijosCantidad}`
    }

    document.getElementById(`deslizarIzquierda${tipoID}`).addEventListener('click', DeslizarIzquierda)
    document.getElementById(`deslizarDerecha${tipoID}`).addEventListener('click', DeslizarDerecha)

    MostrarImagen(index)
}




deslizarIzquierda.addEventListener("click", DeslizarIzquierda)

deslizarDerecha.addEventListener("click", DeslizarDerecha)
