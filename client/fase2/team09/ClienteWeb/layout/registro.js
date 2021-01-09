function registro(){
    var user1 = document.getElementById("name").value;
    var pass1 = document.getElementById("password").value;
    var confirmPass = document.getElementById("confirm").value;
   if(pass1 == confirmPass){
       
    ruta = 'http://localhost:8888/login/nuevo'
    fetch(ruta,
        {
            method:'POST',
            mode: 'cors',
            body: JSON.stringify({name:user1,password:pass1}),
            headers:{
                'Content-Type': 'application/json'
            }
        })
    .then(response => response.json())
    .catch(error=> cosole.log('Error:',error))
    .then(data => validar(data));  

   }else{
       alert("password incorrecto!")
   }
}

function validar(data){
    console.log(data)
    if (data.mensaje == "Exito"){
        window.open("http://localhost:8000/login","_self") 
    }else{
        alert("Ya existe el usuario!")
    }
}
function cancelar(){
    window.open("http://localhost:8000","_self") 
  }