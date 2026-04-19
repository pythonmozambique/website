from browser import html
from datetime import datetime


def create():
    actual_year = datetime.now().year

    footer = html.FOOTER(Class="footer-section")

    # Container principal
    container = html.DIV(Class="footer-container")

    # Seçcao Sobre
    about_section = html.DIV(Class="footer-section-group")
    about_section <= html.H3("Python Moçambique", Class="footer-title")
    about_section <= html.P(
        "Comunidade de desenvolvedores Python dedicada a promover a linguagem e compartilhar conhecimento.", Class="footer-description")
    container <= about_section

    # kkkk, seccao dos links
    links_section = html.DIV(Class="footer-section-group")
    links_section <= html.H3("Links Rápidos", Class="footer-title")
    quick_links = html.UL(Class="footer-quick-links")
    quick_links <= html.LI(html.A("Home", href="#"))
    quick_links <= html.LI(html.A("Sobre Nós", href="#aboutus"))
    quick_links <= html.LI(html.A("Eventos", href="#events"))
    quick_links <= html.LI(html.A("Contato", href="#contact"))
    links_section <= quick_links
    container <= links_section

    
    social_section = html.DIV(Class="footer-section-group")
    social_section <= html.H3("Conecte-se", Class="footer-title")
    social_links = html.DIV(Class="footer-social-links")
    social_links <= html.A(html.SPAN("Whatsapp", Class="social-icon"),
                           href="https://chat.whatsapp.com/Lqlzo70Im7B8DzXLWWFKsX", target="_blank", Class="social-link", title="Whatsapp")
    social_links <= html.A(html.SPAN("GitHub", Class="social-icon"),
                           href="https://github.com/pythonmozambique", target="_blank", Class="social-link", title="GitHub")
    social_links <= html.A(html.SPAN("Instagram", Class="social-icon"),
                           href="https://www.instagram.com/pythonmozambique", target="_blank", Class="social-link", title="Instagram")
    social_links <= html.A(html.SPAN("LinkedIn", Class="social-icon"),
                           href="https://www.linkedin.com/company/pythonmozambique", target="_blank", Class="social-link", title="LinkedIn")
    social_section <= social_links
    container <= social_section

    # Seção 4: Boletim Informativo
    newsletter_section = html.DIV(Class="footer-section-group")
    newsletter_section <= html.H3("Boletim Informativo", Class="footer-title")
    newsletter_form = html.DIV(Class="newsletter-form")
    newsletter_form <= html.INPUT(
        type="email", placeholder="Seu email", Class="newsletter-input")
    newsletter_form <= html.BUTTON("Inscrever", Class="newsletter-btn")
    newsletter_section <= newsletter_form
    container <= newsletter_section

    footer <= container

    # Divisor
    footer <= html.HR(Class="footer-divider")

    # Footer Bottom
    bottom = html.DIV(Class="footer-bottom")
    bottom <= html.P(
        f"© {actual_year} Python Moçambique. Criado com ❤️ pela comunidade.", Class="footer-copyright")
    footer <= bottom

    return footer
