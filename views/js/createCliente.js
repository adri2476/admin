function guardar() {
 
    let c = document.getElementById("txtCodigo").value
    let a = document.getElementById("txtApellidoNombre").value
    let i = document.getElementById("txtIva").value
    let t = document.getElementById("txtTelefono").value
 
    let cliente = {
        codigo: c,
        apellidoNombre: a,
        iva: i,
        telefono:t
    }

    let url = "http://localhost:5000/clientes"
    var options = {
        body: JSON.stringify(cliente),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            window.location.href = "./clientes.html";  //NUEVO  
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
 
}
