from flask import Flask, render_template
app = Flask(__name__)


posts = [
    { 'author' : 'John Doe',
     'title' : 'first post',
     'message' : 'first message',
     'date' : 'June 05, 2023'
    },
    { 'author' : 'Mary Smith',
     'title' : 'second post',
     'message' : 'second message',
     'date' : 'June 06, 2023'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)