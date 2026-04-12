from browser import html

def create():
    sec = html.DIV(Id="recursos", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Recursos")

    msg = "Por enquanto, não tocaremos."
    sec <= html.P(msg, Class="placeholder-text")

    return sec


def bind(document):
    pass