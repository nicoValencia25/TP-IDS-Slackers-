const deslizarIzquierda = document.querySelector('.deslizar-izquierda')
const deslizarDerecha = document.querySelector('.deslizar-derecha')
const mostrarImagenes = document.querySelector('.mostrar-imagenes')
const contenedorImagenes = document.querySelector('.contenedor-imagenes')
const contador = document.querySelector('.contador')
const hijos = contenedorImagenes.children
const hijosCantidad = hijos.length

let index = 0
imagenActual = hijos[index]
contador.innerHTML = `${index+1} / ${hijosCantidad}`
console.log(index)

function DeslizarIzquierda(){
    imagenActual = hijos[index]
    if (index > 0){
        index -= 1
    } else {
        index= hijosCantidad-1
    }
    MostrarImagen()
}

function DeslizarDerecha(){
    imagenActual = hijos[index]
    if (index < (hijosCantidad-1)){
        index += 1
    } else {
        index = 0
    }
    MostrarImagen()
}

function MostrarImagen(){
    console.log(index)
    mostrarImagenes.src = hijos[index].getAttribute('src')
    
    contador.innerHTML = `${index+1} / ${hijosCantidad}`
}

deslizarIzquierda.addEventListener("click", DeslizarIzquierda)

deslizarDerecha.addEventListener("click", DeslizarDerecha)