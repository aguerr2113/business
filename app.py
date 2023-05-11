import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from config import mail_username , mail_password


app = Flask(__name__)


app.config['SECRET_KEY'] = "SecretKey"
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password
app.static_folder = 'static'


mail = Mail(app)



@app.route('/')
def index():
    print(os.path.abspath(app.static_folder))

    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def contact():

    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(
            subject = f'Mail from {name}',
            body = f'Name: {name}\nEmail: " {email}\n\n\n{message}',
            sender = email, 
            recipients = [mail_username]
            )
        mail.send(msg)
        return render_template('index.html', success = True)
    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)