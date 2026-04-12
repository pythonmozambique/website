from browser import html

def create():
    sec = html.DIV(Id="recursos", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Recursos")

    links = [
        ("Documentação Python", "https://docs.python.org/3/"),
        ("PyPI - Pacotes Python", "https://pypi.org/"),
        ("Tutorial Brython", "https://brython.info/")
    ]

    lista = html.UL()
    for nome, url in links:
        lista <= html.LI(html.A(nome, href=url, target="_blank"))

    sec <= lista
    return sec


def bind(document):
    pass