from flask import Flask, render_template, request, session
import sqlite3
import webbrowser

app = Flask(__name__)

@app.route('/')
def root():
    return 'root'

@app.route('/login_form')
def login_form():
    return render_template('login_form.html')

@app.route('/login_proc', methods=['POST'])
def login_proc():
    if request.method =='POST':
        Email = request.form['Email']
        userPwd = request.form['Password']
        if len(Email) == 0 or len(userPwd) == 0:
            return 'Email or Password not found!'
        else:
            session['logFlag'] =True
            session['Email'] == Email
            return render_template('login_form.html')

    else:
        return 'Not Found'

app.secret_key = 'sample_secret_key'


if __name__ == '__main__':
    app.debug = True
    app.run()