# Python Community Website

Para executar o projecto localmente, abra o terminal na pasta do repositório e execute:

```bash
SMTP_PASSWORD='password de aplicação do Gmail' python server.py
```

O `server.py` serve o site na porta 9090 e envia o formulário Associe-te para python.community.moz@gmail.com. A password é uma palavra-passe de aplicação dessa conta Google e não entra no repositório.

Na Vercel o site estático continua igual. O envio é a função `api/contacto.py`. A mesma password fica na variável `SMTP_PASSWORD` do projecto.
