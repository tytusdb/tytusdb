package main

import (
	"fmt"
	"html/template"
	"net/http"
)

func main() {
	//archivos estaticos
	http.Handle("/layout/", http.StripPrefix("/layout/", http.FileServer(http.Dir("layout/"))))

	//pagina principal
	http.HandleFunc("/", inicio)

	fmt.Println("simon aqui andamios en el 8000")

	http.ListenAndServe(":8000", nil)
}

func inicio(escritor http.ResponseWriter, lector *http.Request) {
	t := template.Must(template.ParseFiles("index.html"))
	t.Execute(escritor, "")
}
