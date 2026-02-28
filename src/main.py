from browser import document, html

# --- NAVBAR ---
navbar = html.DIV(Id="navbar", Class="navbar")
links = [("Home", "#home"), ("Sobre", "#sobre"), ("Eventos", "#eventos"),
         ("Recursos", "#recursos"), ("Contacto", "#contacto")]

for nome, href in links:
    navbar <= html.A(nome, href=href, Class="nav-link")

document <= navbar

# --- HOME / HERO ---
home_section = html.DIV(Id="home", Class="section")
home_section <= html.H1("Bem-vindo à Comunidade Python Moçambique")
home_section <= html.P("A nossa missão é conectar, educar e inspirar todos os entusiastas de Python em Moçambique.")
home_section <= html.BUTTON("Junte-se à Comunidade", Id="join-btn")
document <= home_section

# --- SOBRE ---
sobre_section = html.DIV(Id="sobre", Class="section")
sobre_section <= html.H2("Sobre Nós")
sobre_section <= html.P("Python Moçambique é uma comunidade aberta para todos: programadores iniciantes, estudantes, profissionais e educadores. "
                        "Promovemos workshops, encontros e projetos colaborativos para fortalecer o ecossistema Python local.")
document <= sobre_section

# --- EVENTOS ---
eventos_section = html.DIV(Id="eventos", Class="section")
eventos_section <= html.H2("Próximos Eventos")
eventos = [
    ("PyCon Maputo 2026", "15 de Março, Maputo"),
    ("Workshop Django", "30 de Abril, Online"),
    ("Hackathon Python", "10 de Junho, Maputo")
]
lista_eventos = html.UL()
for nome, data in eventos:
    lista_eventos <= html.LI(f"{nome} — {data}")
eventos_section <= lista_eventos
document <= eventos_section

# --- RECURSOS ---
recursos_section = html.DIV(Id="recursos", Class="section")
recursos_section <= html.H2("Recursos")
links_recursos = [
    ("Documentação Python", "https://docs.python.org/3/"),
    ("PyPI - Pacotes Python", "https://pypi.org/"),
    ("Tutorial Brython", "https://brython.info/")
]
lista_recursos = html.UL()
for nome, url in links_recursos:
    lista_recursos <= html.LI(html.A(nome, href=url, target="_blank"))
recursos_section <= lista_recursos
document <= recursos_section

# --- CONTACTO ---
contacto_section = html.DIV(Id="contacto", Class="section")
contacto_section <= html.H2("Contacto")
contacto_section <= html.P("Email: info@pythonmozambique.org")
contacto_section <= html.P("Twitter: @PythonMoz")
contacto_section <= html.P("Discord: discord.gg/pythonmoz")
document <= contacto_section

# --- RODAPÉ ---
footer = html.DIV(Id="footer", Class="footer")
footer <= html.P("© 2026 Python Moçambique. Todos os direitos reservados.")
document <= footer

# --- EVENTOS INTERACTIVOS ---
def join(ev):
    alert("Obrigado por se juntar à comunidade! Siga-nos nas redes sociais.")

from browser import alert
document["join-btn"].bind("click", join)