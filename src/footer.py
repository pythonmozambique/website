from browser import html
from datetime import datetime

def create():
    actual_year = datetime.now().year
    
    footer = html.FOOTER(Class="footer-section")
    
    content = html.DIV(Class="footer-content")
    
    text = f"© {actual_year} Python Moçambique. Criado com ❤️ pela comunidade."
    content <= html.P(text, Class="footer-text")
    
    links = html.DIV(Class="footer-links")
    links <= html.A("Whatsapp", href="https://chat.whatsapp.com/Lqlzo70Im7B8DzXLWWFKsX", target="_blank")
    links <= html.SPAN(" | ")
    links <= html.A("GitHub", href="https://github.com/pythonmozambique", target="_blank")
    links <= html.SPAN(" | ")
    links <= html.A("Instagram", href="https://www.instagram.com/pythonmozambique", target="_blank")
    links <= html.SPAN(" | ")
    links <= html.A("LinkedIn", href="https://www.linkedin.com/company/pythonmozambique", target="_blank")
    
    footer <= content
    footer <= links
    
    return footer