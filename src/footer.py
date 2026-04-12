from browser import html

def create():
    sec = html.DIV(Id="footer", Class="footer")

    sec <= html.P("© 2026 Python Moçambique. Todos os direitos reservados.")

    return sec


def bind(document):
    pass