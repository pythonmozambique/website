from browser import html


def create():
    sec = html.DIV(Id="eventos", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    # --- SEÇÃO DE EVENTOS ---
    sec <= html.H2("Eventos e Colaborações")

    eventos_lista = [
        ("Django Girls Matola 2026", "07 de Novembro de 2026 · Cidade da Matola", "img/django-girls-matola.jpg", "https://djangogirls.org/en/matola/"),
        ("Humble Data Workshop", "17 de Outubro de 2026 · Universidade Wutivi - UniTiva", "img/humble-data.png", None),
        ("Django Girls Beira", "26 de Setembro de 2026 · Universidade Zambeze", "img/django-girls-beira.jpg", "https://djangogirls.org/en/beira/"),
        ("Django Girls Manjacaze", "22 de Agosto de 2026 · Manjacaze", "img/django-girls-manjacaze.jpg", "https://djangogirls.org/en/manjacaze/"),
        ("Django Girls Marracuene", "08 de Agosto de 2026 · UCAM, Marracuene", "img/django-girls-marracuene.jpg", "https://djangogirls.org/en/marracuene/"),
    ]

    ev_container = html.DIV(Class="events-container")
    for nome, data, img_url, link in eventos_lista:
        if link:
            card = html.A(href=link, target="_blank", Class="event-card")
        else:
            card = html.DIV(Class="event-card")
        card <= html.IMG(src=img_url, alt=nome, Class="event-image")
        card <= html.H3(nome)
        card <= html.P(data)
        ev_container <= card

    sec <= ev_container

    # --- SEÇÃO DE COMUNIDADES ---
    sec <= html.H2("Nossas Comunidades")

    comunidades_lista = [
        ("Django Girls Mozambique", "", "img/dg.jpeg", "https://www.linkedin.com/company/djangogirlsmoz"),
        ("PyLadies Maputo", "", "img/plm.jpeg", None),
        ("PyLadies Beira", "", "img/plb.jpeg", None),
    ]

    com_container = html.DIV(Class="events-container")
    for nome, info, img_url, link in comunidades_lista:
        if link:
            card = html.A(href=link, target="_blank", Class="event-card")
        else:
            card = html.DIV(Class="event-card")
        card <= html.IMG(src=img_url, alt=nome, Class="event-image")
        card <= html.H3(nome)
        card <= html.P(info)
        com_container <= card

    sec <= com_container

    return sec


def bind(document):
    pass
