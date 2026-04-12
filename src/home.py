from browser import html, alert

def create():
    sec = html.DIV(Id="home", Class="section")

    sec <= html.H1("Bem-vindo à Comunidade Python Moçambique")
    sec <= html.P("A nossa missão é conectar e inspirar.")
    sec <= html.BUTTON("Junte-se à Comunidade", Id="join-btn")

    return sec


def bind(document):
    def join(ev):
        alert("Obrigado por se juntar à comunidade!")

    document["join-btn"].bind("click", join)