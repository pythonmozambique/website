from browser import html

def create():
    navbar = html.DIV(Id="navbar", Class="navbar")

    links = [
        ("Home", "#home"),
        ("Sobre", "#sobre"),
        ("Eventos", "#eventos"),
        ("Recursos", "#recursos"),
        ("Contacto", "#contacto")
    ]

    for nome, href in links:
        navbar <= html.A(nome, href=href, Class="nav-link")

    return navbar


def bind(document):
    pass