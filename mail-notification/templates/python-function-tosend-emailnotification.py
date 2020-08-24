
from flask import Flask, render_template
from flask_mail import Mail
from flask_mail import Message




app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tta2yta@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


# Function to send Email Notification

def sendNotificationEmail(email):
    try:
        msg = Message("PlayRoom",
                    sender="tta2yta@gmail.com",
                    recipients=[email])
        
        msg.html =render_template('PlayroomEmailNotification.html')
                           
        mail.send(msg)
        return "Succesfully send email notification" + email
    except:
        return "Pleae Try again"
