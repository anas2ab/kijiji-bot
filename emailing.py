import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import scraper as scraper
import gc
import telegram

bot = telegram.Bot(token='964759299:AAF0gXoaC9vZxK41N5BJyj1iZ8yWZ8smbyg')


# 879588310
# def email(item, min_price, max_price, id_list, senderE, receiverE, password):
def email(item, min_price, max_price, id_list, chat_id):
    # Create the HTML version of your message
    # html = """\
    # <html>
    #  <body>"""
    html = ""
    items = scraper.scraper(item, min_price, max_price, id_list)
    if len(items) != 0:
        for item in items:
            # html = html + """<p><b>%s</b><br>
            #html = '<b>%s</b> %s %s ><a href="%s">Ad Link</a>' % (item.title, item.price, item.date, "http://" + item.url)
            title = item.title
            price = item.price
            date = item.date
            url = item.url
            title = title.replace("*", " ")
            date = date.replace("< ", "")
            text = '<b>' + title + '</b>' + '\n' + price + '\n' + date + '\n' + '<a href="http://' + url + '">Ad link</a>'
            bot.send_message(chat_id=chat_id,
                             text=text,
                             parse_mode=telegram.ParseMode.HTML)

        # html = html + """</body></html>"""


        #    sender_email = senderE
        #    receiver_email = receiverE
        #    password = password

        # message = MIMEMultipart("alternative")
        # message["Subject"] = "Kijiji Ad Alert!!!!"
        # message["From"] = sender_email
        # message["To"] = receiver_email

        # Turn these into plain/html MIMEText objects
        # part1 = MIMEText(text, "plain")
        # part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        # message.attach(part1)
        # message.attach(part2)

        # Create secure connection with server and send email
        # context = ssl.create_default_context()
        # with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # server.login(sender_email, password)
        # server.sendmail(
        # sender_email, receiver_email, message.as_string()
        # )

    return None


gc.collect()
