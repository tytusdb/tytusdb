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
