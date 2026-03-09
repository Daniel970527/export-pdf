import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg['Subject'] = 'Relatório diário Power BI'
msg['From'] = 'SEU_EMAIL'
msg['To'] = 'SEU_EMAIL, EMAIL_DO_GESTOR'

msg.set_content('Segue relatório diário.')

with open('relatorio.pdf', 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='relatorio.pdf')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("SEU_EMAIL", "SUA_SENHA")
    smtp.send_message(msg)
