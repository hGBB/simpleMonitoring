import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):

    msg = EmailMessage()
    msg.set_content(body)

    gmail_user = "hggbdevelopment@gmail.com"
    gmail_password = ""
    msg['Subject'] = subject
    msg['From'] = "hggbdevelopment@gmail.com"
    msg['To'] = to
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.quit()
