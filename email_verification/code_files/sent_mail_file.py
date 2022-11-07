# import module
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email_verification.code_files.password_gen

generted_otp = email_verification.code_files.password_gen.gen_pass()

result_bool=0


def create_mail(user_entered_emailID):
    sender_email = "vueprojectteam@gmail.com"
    receiver_email = user_entered_emailID
    password = "dovcnwiejrumytxz"

    message = MIMEMultipart("alternative")
    message["Subject"] = "OTP Testing "
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
    <div style="margin:50px auto;width:70%;padding:20px 0">
        <div style="border-bottom:1px solid #eee">
        <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">Your Brand</a>
        </div>
        <p style="font-size:1.1em">Hi,</p>
        <p>Thank you for choosing Your OTP verification application. Use the following OTP to complete your Sign Up procedures. OTP is valid for 10 Seconds</p>
        <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">$(name)</h2>
        <p style="font-size:0.9em;">Regards,<br />Anshuman Singh</p>
        <hr style="border:none;border-top:1px solid #eee" />
        <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
        <p>Anshuman Singh</p>
        <p>B-122 Santpuram Takrohi Indira Nagar</p>
        <p>Lucknow India</p>
        </div>
    </div>
    </div>
    </body>
    </html>
    """
    html = html.replace("$(name)", generted_otp)
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return generted_otp