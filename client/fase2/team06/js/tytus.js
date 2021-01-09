//commentario

var arrayCollection = [
  { id: "database", type: "bds", parent: "#", text: "databases" },
  { id: "dog", type: "bd", parent: "database", text: "Dogs" },
  { id: "base1", type: "bd", parent: "database", text: "base1" },
  { id: "table1", type: "td", parent: "base1", text: "table1" },
];
var nameingresa = "";
var parentname = "";
var autoincre = 0;
$(function () {
  $("#tree").jstree({
    plugins: [
      "themes",
      "types",
      "html_data",
      "ui",
      "crrm",
      "hotkeys",
      "contextmenu",
    ],
    core: {
      check_callback: true,
      data: arrayCollection,
    },
    types: {
      bd: {
        icon: "../img/database22.png",
      },
      td: {
        icon: "../img/tabla.png",
      },
      bds: {
        icon: "../img/servidores.png",
      },
    },
    contextmenu: {
      items: customMenu,
    },
  });
});

function resfreshJSTree() {
  $("#tree").jstree(true).settings.core.data = arrayCollection;
  $("#tree").jstree(true).refresh();
}

function customMenu(node) {
  var items = {
    Create: {
      label: "New Database",
      action: function (data) {
        var ref = $.jstree.reference(data.reference);
        sel = ref.get_selected();
        if (!sel.length) {
          return false;
        }
        parentname = sel[0];
        $("#ModalDB").modal("toggle");
      },
    },
    CreateTT: {
      label: "New Table",
      action: function (data) {
        var ref = $.jstree.reference(data.reference);
        sel = ref.get_selected();
        if (!sel.length) {
          return false;
        }

        parentname = sel[0];
        $("#Modaltable").modal("toggle");
      },
    },
  };

  if (node.type === "bd") {
    delete items.Create;
  } else if (node.type === "td") {
    delete items.Create;
  } else if (node.type === "bds") {
    delete items.CreateTT;
  } else {
    delete items.Create;
    delete items.CreateTT;
  }

  return items;
}

function Guarda() {
  var porNombre = document.getElementsByName("namedb22")[0].value;
  nameingresa = porNombre;
  if (nameingresa !== "" && parentname !== "") {
    var nuevodb = {
      id: nameingresa + autoincre,
      type: "bd",
      parent: parentname,
      text: nameingresa,
    };
    arrayCollection.push(nuevodb);
    resfreshJSTree();
    autoincre++;
  }
  nameingresa = "";
  parentname = "";
  document.getElementsByName("namedb22")[0].value = "";
  CierraPopup("#ModalDB");
  crearBD();
}

function Guardatb() {
  var porNombre = document.getElementsByName("nametb2")[0].value;
  nameingresa = porNombre;
  if (nameingresa !== "" && parentname !== "") {
    var nuevotd = {
      id: nameingresa + autoincre,
      type: "td",
      parent: parentname,
      text: nameingresa,
    };
    arrayCollection.push(nuevotd);
    resfreshJSTree();
    autoincre++;
  }
  nameingresa = "";
  parentname = "";
  document.getElementsByName("nametb2")[0].value = "";
  CierraPopup("#Modaltable");
  crearTabla();
}

function CierraPopup(namePop) {
  $(namePop).modal("hide"); //ocultamos el modal
  $("body").removeClass("modal-open"); //eliminamos la clase del body para poder hacer scroll
  $(".modal-backdrop").remove(); //eliminamos el backdrop del modal
}


var button =
  '<button class="close" type="button" title="Remove this page">×</button>';
var tabID = 1;
function resetTab() {
  var tabs = $("#tab-list li:not(:first)");
  var len = 1;

}

$(document).ready(function () {
  $("#btn-add-tab").click(function () {
    tabID++;
    $("#tab-list").append(
      $(
        '<li class="active nav-item"><a href="#query' +
          tabID +
          '"  class="nav-link" role="tab" data-toggle="tab">   Query ' +
          tabID +
          '   <button class="close" type="button" title="Remove this page">×</button></a></li>'
      )
    );
    $("#tab-content").append(
      $(
        '<div class="tab-pane fade" id="query' +
          tabID +
          '"><textarea rows="15"  class="form-control" aria-label="With textarea"></textarea></div>'
      )
    );
  });

  $('a[data-toggle="tab"]').on("shown.bs.tab", function (e) {
    // here is the new selected tab id
    var selectedTabId = e.target.href;
    console.log(selectedTabId);
  });
  
  $("#save").click(function () {
    saveTextAsFile();
  });
  let input = document.querySelector("input[name='abrir']");
  
  input.addEventListener("change", (event) => {
    let files = input.files;

    var filename = input.files[0].name;

    tabID++;
    $("#tab-list").append(
      $(
        '<li class="active nav-item"><a href="#query' +
          tabID +
          '"  class="nav-link" role="tab" data-toggle="tab">' +
          filename +
          '   <button class="close" type="button" title="Remove this page">×</button></a></li>'
      )
    );
    $("#tab-content").append(
      $(
        '<div class="tab-pane fade" id="query' +
          tabID +
          '"><textarea rows="15"  name="query' +
          tabID +
          '" class="form-control" aria-label="With textarea"></textarea></div>'
      )
    );

    let textarea = document.querySelector(
      "textarea[name='query" + tabID + "']"
    );

    if (files.length == 0) return;

    const file = files[0];

    let reader = new FileReader();

    reader.onload = (e) => {
      const file = e.target.result;

      // This is a regular expression to identify carriage
      // Returns and line breaks
      const lines = file.split(/\r\n|\n/);
      textarea.value = lines.join("\n");
    };

    reader.onerror = (e) => alert(e.target.error.name);

    reader.readAsText(file);
  });
  $("#tab-list").on("click", ".close", function () {
    var tabID = $(this).parents("a").attr("href");
    $(this).parents("li").remove();
    $(tabID).remove();

    //display first tab
    var tabFirst = $("#tab-list a:first");
    //resetTab();
    tabFirst.tab("show");
  });
  
  var list = document.getElementById("tab-list");

});

function input2(elemID, text) {
  var elem = document.getElementById(elemID);
  elem.innerHTML += text + "\n";
}

function saveTextAsFile() {
  var textToWrite = document.getElementById("entrada").value;
  var textFileAsBlob = new Blob([textToWrite], { type: "text/plain" });
  var fileNameToSaveAs = "query.sql";

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  if (window.webkitURL != null) {
    // Chrome allows the link to be clicked without actually adding it to the DOM.
    downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
  } else {
    // Firefox requires the link to be added to the DOM before it can be clicked.
    downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
  }

  downloadLink.click();
}

function destroyClickedElement(event) {
  // remove the link from the DOM
  document.body.removeChild(event.target);
}

function limpiar(elemID) {
  var elem = document.getElementById(elemID);
  elem.innerHTML = "";
}

function ejecutarScript() {
  var texto = eel.PYejecutarScript().value;
  alert("Ejecuntando...");
  console.log(texto);
}

function guardarArchivo() {
  //este solo sobreescribia el archivo, asi que no retnorna nada
  var texto = eel.PYguardarArchivo(x, y);
  alert("Guardado");
  //console.log(texto);
}

function crearBD() {
  var texto = eel.PYcrearBD().value;
  alert("Se ha creado la base de datos");
  console.log(texto);
}
function crearTabla() {
  var texto = eel.PYcrearTabla().value;
  alert("Se ha creado la tabla");
  console.log(texto);
}

function cerrar() {
  window.close();
}

function analize() {
  var text = document.getElementById("entrada").value;
  eel.analize(text);
}


eel.expose(printText);
function printText(text) {
  var elem = document.getElementById("salida");
  elem.innerHTML += text + "\n";
}

eel.expose(addTable);
function addTable(table) {
  //removeElement("tabl");
  const container = document.querySelector("#tablee");
  removeAllChildNodes(container);
  addElement("tablee", "div", "tabl", table);
  //console.log("CLEAR");
  //document.getElementById("tablee").insertAdjacentHTML("afterend", table);
}

eel.expose(addElement);
function addElement(parentId, elementTag, elementId, html) {
  // Adds an element to the document
  var p = document.getElementById(parentId);
  var newElement = document.createElement(elementTag);
  newElement.setAttribute("id", elementId);
  newElement.innerHTML = html;
  p.appendChild(newElement);
}

eel.expose(removeElement);
function removeElement(elementId) {
  // Removes an element from the document
  var element = document.getElementById(elementId);
  element.parentNode.removeChild(element);
}

eel.expose(removeAllChildNodes);
function removeAllChildNodes(parent) {
  while (parent.firstChild) {
    parent.removeChild(parent.firstChild);
  }
}
