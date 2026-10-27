from browser import html

def create():
    navbar = html.DIV(Id="navbar", Class="navbar")

    brand = html.A(href="#hero", Class="nav-brand")
    brand <= html.IMG(src="img/pythonmozambique-logo.png", alt="Python Moçambique", Class="nav-logo")
    navbar <= brand

    toggle = html.BUTTON(Class="nav-toggle", type="button")
    toggle.attrs["aria-label"] = "Abrir menu"
    toggle.attrs["aria-expanded"] = "false"
    toggle.attrs["aria-controls"] = "nav-links"
    for _ in range(3):
        toggle <= html.SPAN()
    navbar <= toggle

    links_box = html.DIV(Id="nav-links", Class="nav-links")
    links = [
        ("Home", "#home"),
        ("Sobre", "#sobre"),
        ("Eventos", "#eventos"),
        ("Recursos", "#recursos"),
        ("Contacto", "#contacto"),
        ("Conduta", "coc.html")
    ]

    for nome, href in links:
        links_box <= html.A(nome, href=href, Class="nav-link")

    navbar <= links_box
    return navbar


def bind(document):
    pass