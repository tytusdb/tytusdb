function login(){
    var user = document.getElementById("username").value;
    var pass = document.getElementById("password").value;
    console.log(user,pass)
    ruta = 'http://localhost:8888/login/' + user + "-" + pass
  
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