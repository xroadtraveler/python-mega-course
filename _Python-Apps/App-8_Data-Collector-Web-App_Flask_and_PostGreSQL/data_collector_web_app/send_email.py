from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height, count):
    from_email = "travis.rillos.test@gmail.com"   # sending email
    from_password = "gfozveheopokvqbb"   # app password
    to_email = email
    
    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>. Average height of all users is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people" % (height, average_height, count)

    msg=MIMEText(message, 'html')   # sets to HTML code
    msg['Subject'] = subject   # subject line
    msg['To'] = to_email   # target email
    msg['From'] = from_email   # sending email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)