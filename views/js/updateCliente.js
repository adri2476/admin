console.log(location.search)     // lee los argumentos pasados a este formulario
var args = location.search.substr(1).split('&');  
//separa el string por los “&” creando una lista [“id=3” , “nombre=’tv50’” , ”precio=1200”,”stock=20”]
console.log(args)
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
}
//decodeUriComponent elimina los caracteres especiales que recibe en la URL 
document.getElementById("txtId").value = decodeURIComponent(parts[0][1])
document.getElementById("txtCodigo").value = decodeURIComponent(parts[1][1]) 
document.getElementById("txtApellidoNombre").value = decodeURIComponent(parts[2][1])
document.getElementById("txtIva").value =decodeURIComponent( parts[3][1])
document.getElementById("txtTelefono").value =decodeURIComponent( parts[4][1])
function modificar() {
    let id = document.getElementById("txtId").value
    let c = document.getElementById("txtCodigo").value
    let a = document.getElementById("txtApellidoNombre").value
    let i = document.getElementById("txtIva").value
    let t = document.getElementById("txtTelefono").value
    let cliente = {
        txtCodigo: c,
        txtApellidoNombre: a,
        txtIva: i,
        txtTelefono: t
    }
    let url = "http://localhost:5000/clientes/"+id
    var options = {
        body: JSON.stringify(cliente),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json'},
       redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            window.location.href = "/views/index.html";  //NUEVO      
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        }) 
    
}
