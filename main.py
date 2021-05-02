from flask import Flask, render_template, request
import random
from datetime import datetime
import requests
import smtplib

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/bc0ec46ce1575b88c05d')
    blog_data = response.json()
    return render_template('index.html', data=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        my_email = ""
        password = ""
        mesg = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        print(mesg)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=mesg)

        return "<h1>Sucessfully sent your message</h1>"
    else:
        return render_template('contact.html')


@app.route('/post/<int:id>')
def get_post(id):
    response = requests.get('https://api.npoint.io/bc0ec46ce1575b88c05d')
    blog_data = response.json()[id]
    return render_template('posts.html', title=blog_data['title'], subtitle=blog_data['subtitle'],
                           author=blog_data['author'], date=blog_data['date'])


if __name__ == '__main__':
    app.run(debug=True)
