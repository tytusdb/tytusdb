import web

urls = (
    '/', 'Home'
)

renderHome = web.template.render("Views/Templates", base="MainLayout")
render = web.template.render("Views/Templates")
app = web.application(urls, globals())


# Clases/Routes

class Home:
    def GET(self):
        return renderHome.Home(render.Header(),render.Content(), render.Footer(), render.SideBar(), render.Boton())


if __name__ == "__main__":
    app.run()
