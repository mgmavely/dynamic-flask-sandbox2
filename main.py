from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/bc0ec46ce1575b88c05d')
    blog_data = response.json()
    return render_template('index.html', data=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post.html/<int:id>')
def get_post(id):
    response = requests.get('https://api.npoint.io/bc0ec46ce1575b88c05d')
    blog_data = response.json()[id]
    return render_template('post.html', title=blog_data['title'], subtitle=blog_data['subtitle'],
                           author=blog_data['author'], date=blog_data['date'])


if __name__ == '__main__':
    app.run(debug=True)
