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

function alterDatabase(){
    // Get the modal
    var modal = document.getElementById("myModal1");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close1")[0];
  
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

function dropDatabase(){
    // Get the modal
    var modal = document.getElementById("myModal2");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close2")[0];
  
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
  peticionQuery(document.getElementById("texto").value)
}
function logout(){
  window.open("http://localhost:8000","_self") 
}

function base(tipo){
  switch(tipo){
    case "create":
      var contenido = "create database " + document.getElementById("nameBase").value + ";"
      console.log(contenido)
      peticionQuery(contenido)
      document.getElementById("myModal").style.display = "none";
      document.getElementById("nameBase").value = "";
    break;
    case "show":
      console.log("show")
      peticionQuery("show databases;")
    break;
    case "alter":
      var contenido = "alter database " + document.getElementById("nameBaseAntiguo").value 
      contenido +=  " rename to " + document.getElementById("nameBaseNuevo").value + ";"
      console.log(contenido)
      peticionQuery(contenido)
      document.getElementById("myModal1").style.display = "none";
      document.getElementById("nameBaseAntiguo").value = "";
      document.getElementById("nameBaseNuevo").value = "";
    break;
    case "drop":
      var contenido = "drop database " + document.getElementById("nameBaseDrop").value + ";"
      console.log(contenido)
      peticionQuery(contenido)
      document.getElementById("myModal2").style.display = "none";
      document.getElementById("nameBaseDrop").value = "";
    break;
  }
}



//----------------------------- tablas -------------------------------------------------
function createTable(){
  // Get the modal
  var modal = document.getElementById("myModalT1");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("closeT1")[0];

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

function extractTable(){

  var modal = document.getElementById("myModalT2");
  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("closeT2")[0];
 
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

function Table(opcion){
  switch(opcion){
    case "create":
      var contenido = "create table " + document.getElementById("nameTableCreate").value + ";"
      console.log(contenido)
      peticionQuery(contenido)
      document.getElementById("myModalT1").style.display = "none";
      document.getElementById("nameTableCreate").value = "";
    break;

    case "show":
      console.log("show")
      peticionQuery("show tables;")
    break;

    case "extract":
      var contenido = "extract table " + document.getElementById("nameTableExtract").value + ";"
      console.log(contenido)
      peticionQuery(contenido)
      document.getElementById("myModalT2").style.display = "none";
      document.getElementById("nameTableExtract").value = "";
    break;
  }
}



function mostrarSalida(data){
  document.getElementById("textoSalida").value = data
}

function peticionQuery(contenido){
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
}