from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from models import user
from datetime import datetime
from pymongo import MongoClient
from models import user
import pymongo
import dbconnect as dbc

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'



app = Flask(__name__)

app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        
@app.route('/loggedin', methods=['GET', 'POST'])
def loggedin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (dbc.validate_local(str(username),str(password))):
            #print(dbc.validate_online(str(username),str(password)))
            return redirect(url_for('dashboard'))
        return redirect(url_for('loggedin'))
        
    return render_template('login.html')

@app.route("/login",methods=['GET','POST'])
def login_page():
    return 'Login Succesfull'

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
            formdata=request.form['Fname']
            print("data is",formdata)
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/testing')
def testing():
    return render_template('test.html')  




if __name__ == '__main__':
    app.run(
        port=5000,
        host='0.0.0.0',
        debug=True,
        threaded=True
    )