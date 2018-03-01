from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

articles_data = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', data=articles_data)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('articles.html', id=id)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)



    