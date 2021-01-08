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
  // Get the modal
  var modal = document.getElementById("myModal");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks on the button, open the modal
  modal.style.display = "block";

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
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

function base(tipo){
  switch(tipo){
    case "create":
      var contenido = "create database " + document.getElementById("nameBase").value + ";"
      console.log(contenido)
      fetch('http://localhost:8888/query',
          {
              method:'POST',
              mode: 'cors',
              body: JSON.stringify({query: contenido}),
              headers:{
                  'Content-Type': 'application/json'
              }
          })
      .then(response => response.json())
      .catch(error=> cosole.log('Error:',error))
      .then(data => mostrarSalida(data));
      document.getElementById("myModal").style.display = "none";
      document.getElementById("nameBase").value = "";
    break;
    case "show":
      console.log("show")
      fetch('http://localhost:8888/query',
      {
          method:'POST',
          mode: 'cors',
          body: JSON.stringify({query: "show databases;"}),
          headers:{
              'Content-Type': 'application/json'
          }
      })
      .then(response => response.json())
      .catch(error=> cosole.log('Error:',error))
      .then(data => mostrarSalida(data));  
    break;
    case "alter":

    break;
    case "drop":
    break;
  }
}

function mostrarSalida(data){
  document.getElementById("textoSalida").value = data
}