from browser import html, alert

def send_message(ev):
    ev.preventDefault()
    # to change applyin logic
    alert("Obrigado pelo interesse! A equipa da Python Mozambique entrará em contacto em breve.")

def create():
    sec = html.DIV(Id="contacto", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Torna-te um Colaborador")
    sec <= html.P("Tens um projeto, uma ideia ou queres ajudar a comunidade a crescer? Envia-nos uma mensagem!")

    form = html.FORM(Class="contact-form")
    
    form <= html.LABEL("Nome:", html_for="name")
    form <= html.INPUT(Type="text", Id="name", Name="name", Placeholder="Teu nome completo", Required=True)

    form <= html.LABEL("Email:", html_for="email")
    form <= html.INPUT(Type="email", Id="email", Name="email", Placeholder="teu@email.com", Required=True)

    form <= html.LABEL("Como queres colaborar?", html_for="message")
    form <= html.TEXTAREA(Id="message", Name="message", Placeholder="Escreve brevemente como pretendes ajudar...", Required=True)

    submit_btn = html.BUTTON("Enviar Mensagem", Type="submit")
    form <= submit_btn
    
    form.bind("submit", send_message)

    sec <= form
    info_div = html.DIV(Class="social-info")
    info_div <= html.P(f"Email directo: info@pythonmozambique.org")
    sec <= info_div

    return sec

def bind(document):
    pass