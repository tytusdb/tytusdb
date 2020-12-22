import web,requests
from web import form
import json

myobj = {'entrada': 'somevalue'}

url = 'http://localhost:5000/ejecutar'
urls = (
    '/', 'Home', 'Boton'
)

renderHome = web.template.render("Views/Templates", base="MainLayout")
render = web.template.render("Views/Templates")
app = web.application(urls, globals())

boton = form.Form(
    
    form.Button("Ejecutar", type="button", description="ejecutar"),

)

consola = form.Form(
    form.Textarea("consolatxt")
)



# Clases/Routes

class Home:

    def GET(self):
        f = boton()
        c = consola()
        return renderHome.Home(render.Header(),render.Content(c), render.Footer(), render.SideBar(), render.Boton(f))


    def POST(self):
        dictToSend = {'entrada':'what is the answer?'}
        res = requests.post('http://127.0.0.1:5000/ejecutar', json=dictToSend)
        # print ('response from server:',res.text)
        # dictFromServer = res.json()
        f = boton()

       

        c2 = res.json()
        c3 = c2[0]['resultado']



        return renderHome.Home(render.Header(),render.Content(c3), render.Footer(), render.SideBar(), render.Boton(f))


        # f = boton()
        # c = consola()
        # if not f.validates():
        #     return renderHome.Home(render.Header(),render.Content(c), render.Footer(), render.SideBar(), render.Boton(f))
        # else:          
                
        #         #extraer el textarea
        #         x = requests.post(url, json = {'entrada':'Ejemplo'})
        #         y = json.loads(x.text)
                
        #         print(y['resultado'])
        #         return renderHome.Home(render.Header(),render.Content(c), render.Footer(), render.SideBar(), render.Boton(f))


if __name__ == "__main__":
    app.run()
