from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_mysqldb import MySQL
################################################################################
# Section: Flask Configuration
# Blueprint routes
# Here we will import our different project blueprints
################################################################################
app = Flask(__name__)
################################################################################
# Section: Flask Configuration
# Operations that enable flask to work.
################################################################################
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
################################################################################
# Section: DataBase
# This is the section that configures database info for flask.
################################################################################
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
################################################################################
# Section: Teacher
# This is for all things teacher beginning with login.
################################################################################

from application.teacherOps.views import teacher
from application.parentOps.views import parent

app.register_blueprint(teacherOps.views.teacher)
app.register_blueprint(parentOps.views.parent)

@app.route('/')
def index():
   return render_template('dashboard/index.html')


@app.route('/logout')
def logout():
   if session['logged_in'] == True:
      session.clear()
      flash("You are now logged out", 'success')
      return redirect(url_for('index'))