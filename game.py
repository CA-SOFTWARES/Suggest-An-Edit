try:
    import smtplib

    n = input("You Email ID: ")
    f = input("Password: ")
    a = input("Reciever Email ID: ")
    b = input("Subject: ")
    c = input("Message: ")
    TO = a
    SUBJECT = b
    TEXT = c

    # Gmail Sign In
    gmail_sender = n
    gmail_passwd = f

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('Email Sent')
    except:
        print('Error Sending Mail')

    server.quit()
except:
    print('')
    print('Could Not Send')