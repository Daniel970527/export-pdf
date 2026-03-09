import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['Subject'] = 'Relatorio diario'
msg['From'] = 'SEU_EMAIL'
msg['To'] = 'EMAIL_DESTINO'

msg.set_content('Segue relatorio em anexo.')

with open('relatorio.pdf','rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='pdf',
        filename='relatorio.pdf'
    )

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login("SEU_EMAIL","SENHA_APP")
    smtp.send_message(msg)
