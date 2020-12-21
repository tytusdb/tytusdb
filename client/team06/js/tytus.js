//commentario
var a;
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
