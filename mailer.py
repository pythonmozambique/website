import os
import smtplib
from email.message import EmailMessage

INBOX = "python.community.moz@gmail.com"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def _line(value, limit):
    text = str(value or "").replace("\r", " ").replace("\n", " ").strip()
    return text[:limit]


def send_contact(name, email, message):
    name = _line(name, 200)
    email = _line(email, 200)
    message = str(message or "").replace("\r\n", "\n").strip()
    if not name or not email or "@" not in email or not message:
        raise ValueError("invalid")
    if len(message) > 5000:
        raise ValueError("invalid")

    password = os.environ.get("SMTP_PASSWORD", "").strip()
    if not password:
        raise RuntimeError("missing-password")

    user = _line(os.environ.get("SMTP_USER", INBOX), 200) or INBOX
    mail = EmailMessage()
    mail["Subject"] = "Nova mensagem — Associe-te"
    mail["From"] = user
    mail["To"] = INBOX
    mail["Reply-To"] = email
    mail.set_content(f"Nome: {name}\nEmail: {email}\n\n{message}\n")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=20) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user, password)
        smtp.send_message(mail)


def deliver(data):
    if not isinstance(data, dict):
        return 400, {"ok": False}
    try:
        send_contact(data.get("name", ""), data.get("email", ""), data.get("message", ""))
    except ValueError:
        return 400, {"ok": False}
    except RuntimeError:
        return 503, {"ok": False}
    except Exception as exc:
        print("Falha ao enviar:", type(exc).__name__)
        return 502, {"ok": False}
    return 200, {"ok": True}
