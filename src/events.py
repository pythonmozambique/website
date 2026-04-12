from browser import html


def create():
    sec = html.DIV(Id="eventos", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Eventos e Colaborações")

    eventos = [
        ("PyCon Maputo 2026", "15 de Março, Maputo"),
        ("Workshop Django", "30 de Abril, Online"),
        ("Hackathon Python", "10 de Junho, Maputo"),
        ("DjangoGirls Maputo", "TBC, Maputo"),
        ("PyLadies Maputo", "TBC, Online"),
        ("PyLadies Beira", "TBC, Beira")
    ]

    # Container para os cards
    container = html.DIV(Class="events-container")
    for nome, data in eventos:
        # Cada evento é um card
        card = html.DIV(Class="event-card")
        card <= html.H3(nome)
        card <= html.P(data)
        container <= card

    sec <= container
    return sec


def bind(document):
    pass
