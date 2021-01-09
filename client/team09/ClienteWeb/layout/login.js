function login(login,password){
    var user = document.getElementById("Usuario")
    var pass = document.getElementById("Password")
    
    ruta = 'http://localhost:8888/login/' + login + "-" + password 
    fetch(ruta)
    .then(response => response.json())
    .then(data => validar(data));
}

function validar(data){
    console.log(data)
    if (data.mensaje == "Exito"){
        window.open("http://localhost:8000/inicio","_self") 
    }else{
        alert("Sus credenciales no se encuentran registradas en el sitio")
    }
}