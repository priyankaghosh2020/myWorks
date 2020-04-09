from flask import flash, redirect, render_template, request, url_for, session
from main import app

app.secret_key = b'_df45@67789*eQ8zec]/'

def start() :
    app.config['USERNAME'] = 'admin'
    app.config['PASSWORD'] = 'admin'
    app.run()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Priyanka'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login' , methods=['GET', 'POST'])
def login() :
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('display'))
    return render_template('login.html', title='Home', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    app.logger.error('Logged Out(%d app)', 1)
    return redirect(url_for('display'))

@app.route('/display')
def display():
    user = {'username': 'Miguel'}
    return render_template('show_entries.html', title='Home', user=user)