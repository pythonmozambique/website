from browser import html


def create():
    sec = html.DIV(Id="eventos", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    # --- SEÇÃO DE EVENTOS ---
    sec <= html.H2("Eventos e Colaborações")

    eventos_lista = [
        ("PyCon Maputo 2026", "15 de Março, Maputo", "https://th.bing.com/th/id/OIP.yoPeL8kFPnlzxd1UBb6mIgHaG1?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"),
        ("Hackathon Python", "10 de Junho, Maputo", "images/hackathon.jpg")
    ]

    ev_container = html.DIV(Class="events-container")
    for nome, data, img_url in eventos_lista:
        card = html.DIV(Class="event-card")
        card <= html.IMG(src=img_url, alt=nome, Class="event-image")
        card <= html.H3(nome)
        card <= html.P(data)
        ev_container <= card

    sec <= ev_container

    # --- SEÇÃO DE COMUNIDADES ---
    sec <= html.H2("Nossas Comunidades")

    comunidades_lista = [
        ("Workshop Django", "", "img/dg.jpeg"),
        ("DjangoGirls Maputo", "", "img/dg.jpeg"),
        ("PyLadies Maputo", "", "img/plm.jpeg"),
        ("PyLadies Beira", "", "img/plb.jpeg")
    ]

    com_container = html.DIV(Class="events-container")
    for nome, info, img_url in comunidades_lista:
        card = html.DIV(Class="event-card")
        card <= html.IMG(src=img_url, alt=nome, Class="event-image")
        card <= html.H3(nome)
        card <= html.P(info)
        com_container <= card

    sec <= com_container

    return sec


def bind(document):
    pass
