from browser import html, alert

def create():
    sec = html.SECTION(id="hero")
    
    content_div = html.DIV(Class="hero-content")
    
    content_div <= html.H1("Bem-vindo à Comunidade Python Moçambique")
    content_div <= html.P("Unindo desenvolvedores, entusiastas e inovadores para fortalecer o ecossistema tecnológico em Moçambique.")
    
    btn = html.BUTTON("Junte-se à Comunidade", id="join-btn")
    content_div <= btn
    
    sec <= content_div
    return sec

def bind(document):
    def join(ev):
        alert("Kanimambo! Você será redirecionado para o nosso formulário de inscrição.")

    if "join-btn" in document:
        document["join-btn"].bind("click", join)