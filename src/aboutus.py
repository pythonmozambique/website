from browser import html

def create():
    sec = html.DIV(Id="sobre", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Sobre Nós")
    sec <= html.P(
        "Python Moçambique é uma comunidade aberta para todos: programadores iniciantes, estudantes, profissionais e educadores. "
        "Promovemos workshops, encontros e projetos colaborativos para fortalecer o ecossistema Python local."
    )

    return sec


def bind(document):
    pass