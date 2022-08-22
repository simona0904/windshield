import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from windshield.database.windshield import Windshield

EMAIL_PASS = "hrrtndzyztkpixrz"
EMAIL_USER = "cordos.simona@gmail.com"
EMAIL_SERVER = "smtp.gmail.com"
EMAIL_SERVER_PORT = 465         # post smtp pentru conexiuni securizate

def send_request_offer_email(windshield: Windshield, name: str, phone: str) -> None:
    message = MIMEMultipart("alternative")
    message["Subject"] = "Offer request"
    message["From"] = EMAIL_USER
    message["To"] = EMAIL_USER
    html = f"""
    <html>
    <body>
        <p>Offer request from {name} and {phone}</p>
        <p>For {windshield.eurocode}</p>
        <p>And {windshield.brand}, {windshield.model}, {windshield.model}, {windshield.start_year}, {windshield.end_year},
        sensor: {windshield.sensor}, camera: {windshield.camera}, heat: {windshield.heat}</p>
    </body>
    </html>
    """
    part2 = MIMEText(html, "html") 
    message.attach(part2)
    server = smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_SERVER_PORT)
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(
        EMAIL_USER,
        EMAIL_USER,
        message.as_string()
    )

   
