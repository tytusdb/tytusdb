function peticion(){
  fetch('http://localhost:8888')
  .then(response => response.json())
  .then(data => console.log(data));
}