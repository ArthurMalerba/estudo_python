import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Start Servidor
host = "smtp.gmail.com"
port = "587"
login = "arhur.malerba@gmail.com"
senha = "#M@lerb@79#"

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()

server.login(login,senha)

# Contruir o email tipo MIME

corpo = "Olá tudo bem ? "

mensagem = MIMEMultipart()

mensagem['From'] = login
mensagem['To'] = "arthur.malerba@yahoo.com.br"
mensagem['Subject'] = "Mensagem Enviada"
mensagem.attach(MIMEText(corpo,'plain'))

#enviar Email
server.sendmail(mensagem['From'],mensagem['To'],mensagem.as_string())

server.quit()
