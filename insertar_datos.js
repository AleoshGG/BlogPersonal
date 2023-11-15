function face(url) {
    window.location.href = url;
}
function insta(url) {
    window.location.href = url;
}
function githup(url) {
    window.location.href = url;
}
function link(url) {
    window.location.href = url;
}
function x(url) {
    window.location.href = url;
}


function enviarDatos() {    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    // Llamada a la función en Python para insertar en la base de datos
    fetch(`insertar_datos?name=${name}&email=${email}`)
        .then(response => {
            if (response.ok) {
                console.log('Datos insertados correctamente');
            } else {
                console.error('Error al insertar datos');
            }
        })
}


