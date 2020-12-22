def generar_img(temp : str):
    from graphviz import Source
    s = Source(temp, filename="src\\Reports\\tree_report", format="png")
    s.view()