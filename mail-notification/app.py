
from flask import Flask, render_template
from flask_mail import Mail
from flask_mail import Message




app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tta2yta@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def hello():
    # return render_template("index_1.html")
    return "Hello"

@app.route('/email',  methods=['GET', 'POST'])
def sendNotificationEmail():
    # try:
        email="yordanossari@gmail.com"
        email1="tta2yta@gmail.com"
        email2="jcuevasmunoz@gmail.com"
        email3="francisco.contreras@playroom.gg"
        email4="francisco.contrerasa@mail.udp.cl"
        email5="sebastianecontreras@gmail.com"
        msg = Message("PlayRoom",
                    sender="tta2yta@gmail.com",
                    recipients=[email])
        
        msg.html =render_template('email_table-main-backup.html')
        # msg.add_alternative()
                           
        mail.send(msg)
        return "Succesfully send email notification header today seb new10 T" + email1
    # except:
        # return "Pleae Try again"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)