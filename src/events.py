from browser import html

def create():
    sec = html.DIV(Id="eventos", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Próximos Eventos")

    eventos = [
        ("PyCon Maputo 2026", "15 de Março, Maputo"),
        ("Workshop Django", "30 de Abril, Online"),
        ("Hackathon Python", "10 de Junho, Maputo")
    ]

    lista = html.UL()
    for nome, data in eventos:
        lista <= html.LI(f"{nome} — {data}")

    sec <= lista
    return sec


def bind(document):
    pass