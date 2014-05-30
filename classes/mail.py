__author__ = 'vovacooper'

import smtplib
from logger import logger
from email.MIMEText import MIMEText

HOST = 'smtp.gmail.com'
PORT = '587'
USERNAME = 'deltaprice1@gmail.com'
PASSWORD = 'vc1123581311'

class Mail:
    @staticmethod
    def send_mail(to_list, from_address, subject, body):
        server = smtplib.SMTP()
        server.connect(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(USERNAME, PASSWORD)

        notice = "Completed"
        #to_list = ["vovacooper@gmail.com"]

        #from_address = '"IT Staff" '
        #subject = 'deltaprice server maintenance notice'
        #message = '''
        #The deltaprice database server maintenance is
        #%s
        #''' % notice

        _hdr = "From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (from_address, to_list, subject)
        server.sendmail("it@vlsmaps.com", to_list, _hdr+body)
        server.quit

########################################################################################################################
if __name__ == "__main__":
    message = '''
    The deltaprice database server maintenance is
    %s
    '''
    SendMail.send_mail(["vovacooper@gmail.com"], '"IT Staff" ', 'deltaprice server maintenance notice', message)

