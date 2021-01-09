

$(document).ready(function () {


  //const div = document.getElementById("contenido");
  const pest = document.getElementById("contenido");
  pest.innerHTML = `
    <nav>
      <div class="nav nav-tabs" id="my-tab" role="tablist">
      <a class="nav-item nav-link active" id="nav-txt1-tab" data-toggle="tab" href="#nav-txt1" role="tab" aria-controls="nav-txt1" aria-selected="true">Pestaña1</a>
      </div>
      <div class="tab-content" id="nav-tabContent">
        <div class="tab-pane fade show active" id="nav-txt1" role="tabpanel" aria-labelledby="nav-home-tab">
        {{form.entrada(class_="form-control")}} 
       <!-- <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea1" value="{{ request.form.content }}" style="height: 80%"></textarea> -->
        </div>
      </div>
    </nav>
  `;
 /* div.innerHTML = `
  <ul class="nav nav-tabs">
    <li id="ePestana1" class="active" name="pestana"><a data-toggle="tab" href="#Archivo1">Archivo1</a></li>
    <li style="display:none;" id="ePestana2" name="pestana"><a data-toggle="tab" href="#Archivo2">Archivo2</a></li>
    <li style="display:none;" id="ePestana3" name="pestana"><a data-toggle="tab" href="#Archivo3">Archivo3</a></li>
    <li style="display:none;" id="ePestana4" name="pestana"><a data-toggle="tab" href="#Archivo4">Archivo4</a></li>
    <li style="display:none;" id="ePestana5" name="pestana"><a data-toggle="tab" href="#Archivo5">Archivo5</a></li>
  </ul>

  <div class="tab-content">
    <div id="Archivo1" class="tab-pane fade in active">
      <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea1"
      value="{{ request.form.content }}" style="height: 80%"></textarea>
    </div>
    <div id="Archivo2" class="tab-pane fade">
      <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea2"
      value="{{ request.form.content }}" style="height: 80%"></textarea>
    </div>
      <div id="Archivo3" class="tab-pane fade">
      <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea3"
      value="{{ request.form.content }}" style="height: 80%"></textarea>
    </div>
    <div id="Archivo4" class="tab-pane fade">
      <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea4"
      value="{{ request.form.content }}" style="height: 80%"></textarea>
    </div>
    <div id="Archivo5" class="tab-pane fade">
      <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea5"
      value="{{ request.form.content }}" style="height: 80%"></textarea>
    </div>
  </div>
  `; */

 // addCodeMirror2();
});

var contador = 2;

function agregarPestana() {

  if(contador>=6){
    return;
  }  

  // const encabezadoPestana = document.getElementById("encabezadoPestana");
  // encabezadoPestana.innerHTML += `
  //   <li class="active"><a id="pestana" data-toggle="tab" href="#pestana` + String(contador) + `">Menu ` + String(contador) + `</a></li>
  // `;

  // const encabezadoContenido = document.getElementById("encabezadoContenido");
  // encabezadoContenido.innerHTML += `
  //   <div id="pestana` + String(contador) + `" name="pestanaContenido" class="tab-pane in active">
  //     <div style="padding:10px;">

  //       <textarea placeholder="Escribir Query Aqui" name="content" id="pestanaContenidoTextArea` + String(contador) + `"
  //           value="{{ request.form.content }}" style="height: 80%">CCC</textarea>

  //     </div>
  //   </div>
  // `;

  // var editor = document.getElementById("pestanaContenidoTextArea" + String(contador));
  // addCodeMirror(editor);
  // editor.focus();
  // $('.nav-tabs a:last').tab('show');
  // contador++;


  const pestana = document.getElementById("ePestana" + String(contador));
  pestana.style.display = 'inline';

  // const cPestana = document.getElementById("Archivo" +String(contador));
  // cPestana.style.display = 'inline';

  contador++;

}



function addCodeMirror(element) {

  var codemirror = CodeMirror.fromTextArea(element, {
    mode: 'text/x-pgsql',
    lineNumbers: true, // set number
    smartIndent: true, // smart indent
    indentUnit: 4, // Smart indent in 4 spaces
    indentWithTabs: true, // Smart indent with tabs
    lineWrapping: true, // 
    // Add line number display, folder and syntax detector to the slot
    gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter", "CodeMirror-lint-markers"],
    foldGutter: true, // Enable code folding in slots
    autofocus: true, // Autofocus
    matchBrackets: true, // Match end symbols, such as "],}"
    autoCloseBrackets: true, // Auto close symbol
    styleActiveLine: true, // Display the style of the selected row
    lint: true
  });
  codemirror.setValue('');
  setTimeout(function () {
    codemirror.refresh();
  }, 1);

}





function addCodeMirror2() {

  var editor = document.getElementById("pestanaContenidoTextArea1");
  var codemirror = CodeMirror.fromTextArea(editor, {
    mode: 'text/x-pgsql',
    lineNumbers: true
  });
  codemirror.setValue('');
  setTimeout(function () {
    codemirror.refresh();
  }, 1);



  var editor2 = document.getElementById("pestanaContenidoTextArea2");
  var codemirror2 = CodeMirror.fromTextArea(editor2, {
    mode: 'text/x-pgsql',
    lineNumbers: true
  });
  codemirror2.setValue('');
  setTimeout(function () {
    codemirror2.refresh();
  }, 1);



  var editor3 = document.getElementById("pestanaContenidoTextArea3");
  var codemirror3 = CodeMirror.fromTextArea(editor3, {
    mode: 'text/x-pgsql',
    lineNumbers: true
  });
  codemirror3.setValue('');
  setTimeout(function () {
    codemirror3.refresh();
  }, 1);



  var editor4 = document.getElementById("pestanaContenidoTextArea4");
  var codemirror4 = CodeMirror.fromTextArea(editor4, {
    mode: 'text/x-pgsql',
    lineNumbers: true
  });
  codemirror4.setValue('');
  setTimeout(function () {
    codemirror4.refresh();
  }, 1);



  var editor5 = document.getElementById("pestanaContenidoTextArea5");
  var codemirror5 = CodeMirror.fromTextArea(editor5, {
    mode: 'text/x-pgsql',
    lineNumbers: true
  });
  codemirror5.setValue('');
  setTimeout(function () {
    codemirror5.refresh();
  }, 1);


}



function actionAgregarPestana() {
  try {
    agregarPestana();
  } catch (e) {
    alert(e);
  }
}



function actionQuitarPestana() {
  try {
    quitarPestana();
  } catch (e) {
    alert(e);
  }
}


function quitarPestana() {

  if (contador == 1) {

  } else if (contador == 2) {
    // const pestana = document.getElementById("ePestana1");
    // pestana.style.display = 'none';

    // var editor5 = document.getElementById("pestanaContenidoTextArea1");
    // var codemirror5 = CodeMirror.fromTextArea(editor5, {
    //   mode: 'text/x-pgsql',
    //   lineNumbers: true
    // });
    // codemirror5.setValue('');
    // setTimeout(function () {
    //   codemirror5.refresh();
    // }, 1);
    // contador--;

    // var aaaa = document.getElementById("contenido");
    // aaaa.style.display='none';

  } else if (contador == 3) {
    const pestana = document.getElementById("ePestana2");
    pestana.style.display = 'none';

    var editor5 = document.getElementById("pestanaContenidoTextArea2");
    var codemirror5 = CodeMirror.fromTextArea(editor5, {
      mode: 'text/x-pgsql',
      lineNumbers: true
    });
    codemirror5.setValue('');
    setTimeout(function () {
      codemirror5.refresh();
    }, 1);
    contador--;

  } else if (contador == 4) {
    const pestana = document.getElementById("ePestana3");
    pestana.style.display = 'none';

    var editor5 = document.getElementById("pestanaContenidoTextArea3");
    var codemirror5 = CodeMirror.fromTextArea(editor5, {
      mode: 'text/x-pgsql',
      lineNumbers: true
    });
    codemirror5.setValue('');
    setTimeout(function () {
      codemirror5.refresh();
    }, 1);
    contador--;

  } else if (contador == 5) {
    const pestana = document.getElementById("ePestana4");
    pestana.style.display = 'none';

    var editor5 = document.getElementById("pestanaContenidoTextArea4");
    var codemirror5 = CodeMirror.fromTextArea(editor5, {
      mode: 'text/x-pgsql',
      lineNumbers: true
    });
    codemirror5.setValue('');
    setTimeout(function () {
      codemirror5.refresh();
    }, 1);
    contador--;
  } else if (contador == 6) {
    const pestana = document.getElementById("ePestana5");
    pestana.style.display = 'none';

    var editor5 = document.getElementById("pestanaContenidoTextArea5");
    var codemirror5 = CodeMirror.fromTextArea(editor5, {
      mode: 'text/x-pgsql',
      lineNumbers: true
    });
    codemirror5.setValue('');
    setTimeout(function () {
      codemirror5.refresh();
    }, 1);
    contador--;
  }

}


//function myFunction() {
  // $.ajax({
  //     url: '/',
  //     type: 'POST',
  //     data: {
  //         params: text
  //  }).done(function(){
  //      /* Do something */
  //  });
//}