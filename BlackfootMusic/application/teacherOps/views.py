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
teacher = Blueprint('teacher',__name__)
################################################################################
# Section: Teacher
# This is for all things teacher beginning with login.
################################################################################
@teacher.route('/teacherLogin', methods=['GET', 'POST'])
def teacherLogin():
    if request.method == 'POST':
        username = request.form['username']
        formPassword = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM teacher WHERE TeacherUsername = %s", [username])
        if result > 0:
            data = cur.fetchone()
            password = data['TeacherPassword']
            parentID = data['TeacherID']
            if sha256_crypt.verify(formPassword,password):

                session['TeacherUsername'] = username
                session['logged_in'] = True

                flash('Login was succesful', 'success')
                return redirect(url_for('teacher.teacherDashboard'))
            else:
                error = 'Incorrect username or password'
                return render_template('teacher/teacherLogin.html', error=error)

            cur.close()
        else:
            error = 'Unexpected error occured'
            return render_template('teacher/teacherLogin.html', error=error)

    return render_template('teacher/teacherLogin.html')
################################################################################
# Teacher: Teacher Dashboard
################################################################################
@teacher.route('/teacherDashboard')
def teacherDashboard():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN parentstudent ps on ps.Student_StudentID = s. StudentID JOIN parent t ON ps.Parent_ParentID = t.ParentID;")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')