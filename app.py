from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

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

            server.login("avyukthnilajagi@gmail.com", "Night04Monkey$")

            msg = f"Subject: {subject}\n\n{body}"

            sender = "avyukthnilajagi@gmail.com"
            recipients = ["avyukthnilajagi@gmail.com", "tanishka.mehta06@gmail.com"]
           
            for i in range(len(recipients)):
                server.sendmail(sender, recipients[i], msg)
        
        return render_template('question.html')


if __name__ == '__main__':
    app.run(debug=True)
