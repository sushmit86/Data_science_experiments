from flask import Flask , render_template
app = Flask(__name__)

posts = [
        {
            'author':'Sushmit Roy',
            'title':'Blog Post 1',
            'content': 'Maths is great',
            'date_posted':'Dec 4,2018'
        },
        {
            'author':'Moitri Roy',
            'title':'Blog Post 2',
            'content': 'Instagram is great',
            'date_posted':'Dec 4,2018'
        }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)
