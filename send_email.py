import smtplib, ssl


def send_email(sender, message, subject, send_method="TLS"):
    receiver = "mkappdevtester@gmail.com"
    host = "smtp.gmail.com"
    gmail_user = "mkappdevtester@gmail.com"
    gmail_pwd = "mvup rrgo cvrz eess".replace(" ", "")
    send_method = "TLS".upper() # TLS | SSL

    message = f"""\
Subject: {subject}

From: {sender}

{message}
"""

    if send_method == "TLS":
        port = 587

        svr = smtplib.SMTP(host, port)
        svr.starttls()
        svr.login(gmail_user, gmail_pwd)
        svr.sendmail(gmail_user, gmail_user, message)

    if send_method == "SSL":
        port = 465
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(gmail_user, gmail_pwd)
            server.sendmail(gmail_user, receiver, message)



if __name__ == "__main__":
    # For testing the function directly

    local_msg = """\
This message was sent via the function call, plus injected message.

Bye
From the tester.
"""
    send_email(sender="mkappdevtester@gmail.com", message=local_msg, subject="This is a test")