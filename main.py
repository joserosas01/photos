import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_mail import Mail, Message
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'NJAIRUGUH8E983UREA'


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ABOUT")
def about():
    return render_template("ABOUT.html")

@app.route("/PRICES")
def prices():
    return render_template("PRICES.html")

@app.route("/PHOTOS")
def photos():
    return render_template("PHOTOS.html")

@app.route("/racetrack1")
def racetrack1():
    return render_template("racetrack1.html")

@app.route("/racetrack2")
def racetrack2():
    return render_template("racetrack2.html")

@app.route("/racetrack3")
def racetrack3():
    return render_template("racetrack3.html")

@app.route("/racetrack4")
def racetrack4():
    return render_template("racetrack4.html")

@app.route("/racetrack1-location1")
def racetrack1_location1():
    return render_template("racetrack1-location1.html")

@app.route("/racetrack1-location2")
def racetrack1_location2():
    return render_template("racetrack1-location2.html")

@app.route("/racetrack1-location3")
def racetrack1_location3():
    return render_template("racetrack1-location3.html")

@app.route("/racetrack1-location4")
def racetrack1_location4():
    return render_template("racetrack1-location4.html")


SENDER_EMAIL = 'flash.bot@outlook.com'
RECIPIENT_EMAIL = 'joserosas barrios@gmail.com'  # Replace with your valid recipient email address
SMTP_SERVER = 'smtp.office365.com'  # Replace with your SMTP server address
SMTP_PORT = 587  # Replace with your SMTP server port
EMAIL_PASSWORD = 'Rosas12029'  # Replace with your email password

@app.route("/", methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        photo = request.form['photo']
        comment = request.form['comment']

        # Send email
        send_email(name, email, number, photo, comment)

        # Provide feedback to the user that the form was submitted
        flash('Form submitted successfully!', 'success')

    return render_template("home.html")


def send_email(name, email, number, photo, comment):
    # Create a MIME multipart message
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECIPIENT_EMAIL
    message['Subject'] = 'CUSTOMER REQUEST'

    # Email body
    body = f'''
    Name: {name}
    Email: {email}
    Phone Number: {number}
    Photo to Purchase: {photo}
    Additional Comments: {comment}
    '''

    # Attach the body to the message
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())

if __name__ == "__main__":
    app.run(debug=True)