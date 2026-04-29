from browser import html

def create():
   
    sec = html.SECTION(Id="sobre", Class="section about-us")
    sec.attrs['data-aos'] = 'fade-up'

   
    sec <= html.H2("Sobre Nós", Class="section-title")

    
    intro = html.P(
        "Python Moçambique é uma comunidade aberta para todos: "
        "programadores iniciantes, estudantes, profissionais e educadores. "
        "Promovemos workshops, encontros e projetos colaborativos para "
        "fortalecer o ecossistema Python local.",
        Class="section-intro"
    )
    sec <= intro

   
    content = html.DIV(Class="about-content")

    history = html.DIV(Class="about-block")
    history <= html.H3("Nossa História")
    history <= html.P("Fundada por entusiastas da programação, a comunidade nasceu para unir pessoas e compartilhar conhecimento.")
    content <= history

    mission = html.DIV(Class="about-block")
    mission <= html.H3("Missão & Valores")
    mission <= html.P("Promover inclusão, inovação e colaboração através da linguagem Python.")
    content <= mission

    team = html.DIV(Class="about-block")
    team <= html.H3("Nosso Diferencial")
    team <= html.P("Uma rede diversa que conecta talentos e cria oportunidades para todos.")
    content <= team

    sec <= content

    
    cta = html.DIV(Class="about-cta")
    cta <= html.P("Quer fazer parte? <a href='#contact'>Entre em contato</a> e junte-se a nós!")
    sec <= cta

    return sec


def bind(document):
    pass
