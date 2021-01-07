package main

import (
	"fmt"
	"html/template"
	"net/http"
)

func main() {
	//archivos estaticos
	http.Handle("/layout/", http.StripPrefix("/layout/", http.FileServer(http.Dir("layout/"))))
	http.Handle("/codemirror/", http.StripPrefix("/codemirror/", http.FileServer(http.Dir("codemirror/"))))

	//pagina principal
	http.HandleFunc("/", login)
	http.HandleFunc("/inicio", inicio)
	http.HandleFunc("/registro", registro)

	fmt.Println("simon aqui andamios en el 8000")

	http.ListenAndServe(":8000", nil)

}

func login(escritor http.ResponseWriter, lector *http.Request) {
	t := template.Must(template.ParseFiles("login.html"))
	t.Execute(escritor, "")
}

func inicio(escritor http.ResponseWriter, lector *http.Request) {
	t := template.Must(template.ParseFiles("index.html"))
	t.Execute(escritor, "")
}

func registro(escritor http.ResponseWriter, lector *http.Request) {
	t := template.Must(template.ParseFiles("registro.html"))
	t.Execute(escritor, "")
}
