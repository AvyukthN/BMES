from flask import Flask, render_template, request

app = Flask(__name__)

def emailer(name, subject, body):
    print(name, subject, body)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        context = {'name': 'ur mom'}
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

if __name__ == '__main__':
    app.run(debug=True)
