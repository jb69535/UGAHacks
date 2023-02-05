from flask import Flask, request,session,render_template,redirect,url_for
import sqlite3

app = Flask(__name__)

@app.route('/index')
def main():
    return render_template('/index.html')


@app.route('/registration')
def login():
    return render_template('/registration.html')


@app.route('/login', methods=['post'])
def login():
    Email = request.form['Email']
    Password = request.form['pwd']

    if len(Email) == 0 or len(Password) == 0:
        return Email + ', ' + Password + 'Login Data Not Found.'
    else:
        con = sqlite3.connect("UserData.db")
        cursor = con.cursor()
        sql = "select idx, Email, Password from member where Email =?"
        cursor.execute(sql, (Email,))
        rows = cursor.fetchall()
        for rs in rows:
            print(rs)
            if Email == rs[1] and Password == rs[2]:
                session['logFlag'] = True
                session['idx'] = rs[0]
                session['Email'] = Email

                return redirect(url_for('index.html'))

            else:
                return redirect(url_for('registration.html'))


app.secret_key = 'sample_secret_key'

if __name__ == '__main__':
    app.debug = True
    app.run()