from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, DateField
from passlib.hash import sha256_crypt
from functools import wraps
from application import mysql
from application.parentOps.forms import ParentRegisterForm, RegisterStudentForm
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
                session['permissionLevel'] = 'parent'

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
##############################################################################
# Check login status
##############################################################################
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('index'))
    return wrap
###############################################################################
# Parent: student Query
###############################################################################
@parent.route('/parentDashboard')
@is_logged_in
def parentDashboard():
    parentID = session['parentID']
    if parentID == None:
        flash('Unauthorized, Please login', 'danger')
        return redirect(url_for('index'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID = s. StudentID WHERE parent_parentid = %s",[parentID])
    data = cur.fetchall()
    if data is None:
        error = 'Could not return any students with your id'
        return render_template('parent/parentLogin.html')
    cur.close()
    return render_template('parent/parentDashboard.html',data=data)

###############################################################################
# Parent: Allow parent to create an account.
###############################################################################
@parent.route('/parentRegister', methods=['Get','Post'])
def parentRegister():
    form = ParentRegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        ParentID = form.ParentID.data
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        checkUsername = cur.execute("SELECT * FROM parent WHERE Parentusername = %s", [username])
        if checkUsername > 0:
            flash('Username has been taken, please enter a unique username', 'danger')
            return render_template('parent/parentLogin.html')
        elif checkUsername == 0:
            cur.execute("INSERT INTO parent(parentFname, parentLname, parentEmail, ParentID, Parentusername, ParentPassword) VALUES(%s,%s,%s,%s,%s,%s)", (firstName, lastName, email, ParentID, username, password))
            #%d does represent a number however it will throw an error if used with a small number.
        #commit to finish
        mysql.connection.commit()

        #close connection
        cur.close()
        flash('You are now registered and can view your students instrument check out information', 'success')
        return redirect(url_for('parent.parentLogin'))
    return render_template('parent/parentRegister.html', form=form)
###############################################################################
# Parent: Allow parent add a student to their account.
###############################################################################
@parent.route('/ParentDashboardRegisterStudent', methods=['Get','Post'])
@is_logged_in
def parentAddStudent():
    parentID = session['parentID']
    form = RegisterStudentForm(request.form)
    if request.method == 'POST' and form.validate():
        StudentID = form.StudentID.data
        cur = mysql.connection.cursor()
        checkStudentID = cur.execute("SELECT * FROM student WHERE StudentID = %s", [StudentID])
        if checkStudentID > 0:
            checkDuplicates = cur.execute("SELECT * FROM parentstudent WHERE Student_studentID = %s AND Parent_ParentID = %s", ([StudentID],[parentID]))
            if checkDuplicates > 0:
                flash('duplicate entries are forbidden, sign back in to view your students','danger')
                return redirect(url_for('parent.parentLogin'))
            else: 
                results = cur.execute("INSERT INTO parentstudent(Student_StudentID, Parent_ParentID) VALUES(%s,%s)", (StudentID, parentID))
                mysql.connection.commit()
                cur.close()
                flash('Student added, please sign back into your account', 'success')
                return redirect(url_for('parent.parentLogin'))
        else:
            cur.close()
            flash('No student was found with id ' + str(StudentID))
            return render_template('parent/parentDashboard.html')
    return render_template('parent/parentAddStudent.html', form=form)
    
