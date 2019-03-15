from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, DateField
from passlib.hash import sha256_crypt
from functools import wraps
from application import mysql
################################################################################
# Section: Flask Configuration
# Operations that enable flask to work.
################################################################################
parent = Blueprint('parent', __name__)
################################################################################
# Section: Parent
# This is for all things parent beginning with login.
################################################################################
@parent.route('/parentLogin', methods=['GET', 'POST'])
def parentLogin():
    if request.method == 'POST':
        username = request.form['username']
        formPassword = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM parent WHERE Parentusername = %s", [username])
        if result > 0:
            data = cur.fetchone()
            password = data['ParentPassword']
            parentID = data['ParentID']
            firstName = data['ParentFname']
            if sha256_crypt.verify(formPassword,password):

                session['logged_in'] = True
                session['username'] = username
                session['parentID'] = parentID
                session['firstName'] = firstName

                flash('Login was succesful', 'success')
                return redirect(url_for('parent.parentDashboard', parentID=parentID))
            else:
                error = 'Incorrect username or password'
                return render_template('parent/parentLogin.html', error=error)

            cur.close()
        else:
            error = 'Unexpected error occured'
            return render_template('parent/parentLogin.html', error=error)

    return render_template('parent/parentLogin.html')
###############################################################################
# Parent: student Query
###############################################################################
@parent.route('/parentDashboard')
def parentDashboard():
    parentID = session['parentID']
    cur = mysql.connection.cursor()
    cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID = s. StudentID WHERE parent_parentid = %s",[parentID])
    data = cur.fetchall()
    if data is None:
        error = 'Could not return any students with your id'
        return error
    cur.close()
    return render_template('parent/parentDashboard.html',data=data)