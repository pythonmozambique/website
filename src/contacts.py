from browser import html

def create():
    sec = html.DIV(Id="contacto", Class="section")
    sec.attrs['data-aos'] = 'fade-up'

    sec <= html.H2("Contacto")
    sec <= html.P("Email: info@pythonmozambique.org")
    sec <= html.P("Twitter: @PythonMoz")
    sec <= html.P("Discord: discord.gg/pythonmoz")

    return sec


def bind(document):
    pass