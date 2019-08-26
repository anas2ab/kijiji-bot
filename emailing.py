import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import scraper as scraper

sender_email = input("Enter the sender email: ")
receiver_email = input("Enter the receiver email: ")
password = input("enter password: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Kijiji Ad Alert!!!!"
message["From"] = sender_email
message["To"] = receiver_email

# Create the HTML version of your message
html = """\
<html>
  <body>"""
items = scraper.scraper("iphone x", "400", "900")
for item in items:
    html = html + """<p><b>%s</b><br>
       %s %s <br>
       <a href="%s">Ad Link</a>
    </p>""" % (item.title, item.price,item.date, "http://" + item.url)

html = html + """</body></html>"""


# Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )