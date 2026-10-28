import json

from browser import ajax, html, alert

INBOX = "python.community.moz@gmail.com"
SUBMIT_URL = "/api/contacto"


def send_message(ev):
    ev.preventDefault()
    form = ev.target
    button = form.select_one("button")
    name = form.select_one("[name=name]").value.strip()
    email = form.select_one("[name=email]").value.strip()
    message = form.select_one("[name=message]").value.strip()

    def fail():
        button.disabled = False
        button.text = "Enviar Mensagem"
        alert("Não foi possível enviar a mensagem. Tenta de novo ou escreve para " + INBOX + ".")

    button.disabled = True
    button.text = "A enviar..."
    payload = {"name": name, "email": email, "message": message}

    def finished(req):
        try:
            body = json.loads(req.text)
        except Exception:
            body = {}
        if req.status == 200 and body.get("ok"):
            button.disabled = False
            button.text = "Enviar Mensagem"
            form.reset()
            alert("Obrigado pelo interesse! A equipa da Python Mozambique entrará em contacto em breve.")
            return
        fail()

    ajax.post(
        SUBMIT_URL,
        data=json.dumps(payload),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        timeout=20000,
        oncomplete=finished,
        ontimeout=lambda req: fail(),
    )

def create():
    sec = html.DIV(Id="contacto", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Associe-te")
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
    info_div <= html.P(f"Email directo: python.community.moz@gmail.com")
    sec <= info_div

    return sec

def bind(document):
    pass
