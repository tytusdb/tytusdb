function peticion(){
  fetch('http://localhost:8888')
  .then(response => response.json())
  .then(data => console.log(data));
}

function createScript(){
  alert("Se creará un nuevo script.")
}

function openScript(){
  alert("Se abrirá un nuevo script.")
}

function createDatabase(){
  alert("Se creará una base de datos.")
}

function deleteDatabase(){
  alert("Se eliminará una base de datos.")
}

function drop(){
  alert("Se realizará drop de una tabla de la base de datos actual.")
}

function backup(){
  alert("Se realizará un backup de una base de datos")
}

function info(){
  alert("Se desplegará una página de ayuda de tytusdb.")
}

function server(){
  alert("Se desplegarán todas las bases de datos existentes.")
}

function ejecutar(){
  alert("Se ejecutara el script.")
}
function logout(){
  window.open("http://localhost:8000","_self") 
}

