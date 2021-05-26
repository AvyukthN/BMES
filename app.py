from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
from credentials import creds
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)

    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60),  nullable = False)
    
    def __repr__(self):
        return f"User({}, {})".format(self.username, self.email)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    
    def __repr__(self):
        return f"User({}, {})".format(self.username, self.email)



def emailer(name, subject, body):
    print(name, subject, body)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        for key, value in request.form.items():
            if key == 'searchReq':
                print("searchData - {}".format(value))
        
        return render_template('home.html')
        # emailer(name, subject, body)

@app.route('/aboutus', methods=['GET'])
def aboutUs():
    if request.method == 'GET':
        return render_template('aboutUs.html')

@app.route('/addpost', methods = ['GET', 'POST'])
def addPost():
    if request.method == 'GET':
        return render_template('addPost.html')

    if request.method == 'POST':
        for key, value in request.form.items():
            if key == 'title':
                title = value
            if key == 'body':
                body = value
            if key == 'projName':
                projName = value

        print(title, body, projName)
        return render_template('addPost.html')

@app.route('/question', methods = ['GET', 'POST'])
def question():
    if request.method == 'GET':
        return render_template('question.html')

    if request.method == 'POST':
        if request.form['subject'] and request.form['body']:
            subject = request.form['subject']
            body = request.form['body']

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(creds['email'], creds['pass'])

            msg = f"Subject: {subject}\n\n{body}"

            sender = creds['email'] 
            recipients = ["avyukthnilajagi@gmail.com", "tanishka.mehta06@gmail.com"]
           
            for i in range(len(recipients)):
                server.sendmail(sender, recipients[i], msg)
        
        return render_template('question.html')

@app.route('/apply', methods = ['GET', 'POST'])
def apply():
    return render_template('apply.html')

if __name__ == '__main__':
    app.run(debug=True)
