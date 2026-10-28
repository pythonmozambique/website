import json
from datetime import datetime

from browser import ajax, html


def create():
    actual_year = datetime.now().year

    footer = html.FOOTER(Class="footer-section")

    # Container principal
    container = html.DIV(Class="footer-container")

    # Seçcao Sobre
    about_section = html.DIV(Class="footer-section-group", Style="position: relative; top: -30px;")
    about_section <= html.IMG(
        src="img/pythonmozambique-horizontal-logo.png",
        alt="Python Mozambique",
        Class="footer-logo")
    about_section <= html.P(
        "Comunidade de desenvolvedores Python dedicada a promover a linguagem e compartilhar conhecimento.", Class="footer-description")
    container <= about_section




    social_section = html.DIV(Class="footer-section-group")
    social_section <= html.H3("Conecte-se", Class="footer-title")
    social_links = html.DIV(Class="footer-social-links")

    def fill_social(req):
        for item in json.loads(req.text):
            name = item["name"]
            link = html.A(
                href=item["url"],
                target="_blank",
                Class="social-link",
                title=name,
                aria_label=name,
            )
            icon = html.SPAN(Class="social-icon", aria_hidden="true")
            icon.style.maskImage = f"url('{item['logo']}')"
            icon.style.webkitMaskImage = f"url('{item['logo']}')"
            link <= icon
            social_links <= link

    ajax.get("data/social-media.json", oncomplete=fill_social)
    social_section <= social_links
    container <= social_section

    # Seção 4: Boletim Informativo (oculto por agora)
    # newsletter_section = html.DIV(Class="footer-section-group")
    # newsletter_section <= html.H3("Boletim Informativo", Class="footer-title")
    # newsletter_form = html.DIV(Class="newsletter-form")
    # newsletter_form <= html.INPUT(
    #     type="email", placeholder="Seu email", Class="newsletter-input")
    # newsletter_form <= html.BUTTON("Inscrever", Class="newsletter-btn")
    # newsletter_section <= newsletter_form
    # container <= newsletter_section

    footer <= container

    # Divisor
    footer <= html.HR(Class="footer-divider")

    # Footer Bottom
    bottom = html.DIV(Class="footer-bottom")
    bottom <= html.P(
        f"© {actual_year} Python Mozambique. Criado com ❤️ pela comunidade.", Class="footer-copyright")
    footer <= bottom

    return footer


def bind(document):
    pass
