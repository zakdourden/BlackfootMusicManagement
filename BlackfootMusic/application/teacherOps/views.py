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
            firstName = data['TeacherFname']
            if sha256_crypt.verify(formPassword,password):

                session['TeacherUsername'] = username
                session['logged_in'] = True
                session['permissionLevel'] = 'teacher'
                session['parentID'] = None
                session['name'] = firstName

                flash('Login was succesful', 'success')
                return redirect(url_for('teacher.teacherDashboard'))
            else:
                error = 'Incorrect username or password'
                return render_template('teacher/teacherLogin.html', error=error)

            cur.close()
        else:
            error = 'Not authorized, error'
            return render_template('teacher/teacherLogin.html', error=error)

    return render_template('teacher/teacherLogin.html')
###############################################################################
# Teacher: Check permissions
###############################################################################
def is_logged_in_with_permission(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            if session['permissionLevel'] == 'teacher' or session['permissionLevel'] == 'admin':
                return f(*args, **kwargs)
            elif session['permissionLevel'] == 'parent':
                flash('You do not have the right permissions!','danger')
                return redirect(url_for('index'))
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('index'))
    return wrap
################################################################################
# Teacher: Teacher Dashboard
################################################################################
@teacher.route('/teacherDashboard')
@is_logged_in_with_permission
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
################################################################################
# Teacher: Begin student sorting k-6
# Check inventory is also part of theis section.
################################################################################
@teacher.route('/teacherDashboardSortk')
@is_logged_in_with_permission
def teacherDashboardSortk():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='kindergarten';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@teacher.route('/teacherDashboardSort1')
@is_logged_in_with_permission
def teacherDashboardSort1():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='first';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSort2')
def teacherDashboardSort2():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='second';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSort3')
def teacherDashboardSort3():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='third';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSort4')
def teacherDashboardSort4():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='fourth';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSort5')
def teacherDashboardSort5():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='fifth';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')    

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSort6')
def teacherDashboardSort6():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID JOIN parentstudent ps on ps.Student_StudentID  = s. StudentID JOIN parent q ON ps.Parent_ParentID = q.ParentID WHERE g.gradelevel ='sixith';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')    

@is_logged_in_with_permission
@teacher.route('/teacherDashboardCheckInventory')
def teacherDashboardCheckInventory():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM instrument i LEFT OUTER JOIN student s ON s.studentID = i.instrumentID;")
    instrumentInfo = cur.fetchall()
    if result > 0:
        return render_template('teacher/instrumentInventory.html', instrumentInfo=instrumentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')    

@is_logged_in_with_permission
@teacher.route('/teacherDashboardCheckParent')
def teacherDashboardCheckParent():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM parent;")
    parentInfo = cur.fetchall()
    if result > 0:
        return render_template('teacher/checkParent.html', parentInfo=parentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')    

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSortDueDate')
def teacherDashboardDueDate():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN parentstudent ps on ps.Student_StudentID = s. StudentID JOIN parent t ON ps.Parent_ParentID = t.ParentID order by ReturnDate ASC;")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@is_logged_in_with_permission
@teacher.route('/teacherDashboardSortRecent')
def teacherDashboardSortRecent():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN parentstudent ps on ps.Student_StudentID = s. StudentID JOIN parent t ON ps.Parent_ParentID = t.ParentID order by ReturnDate DESC;")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/teacherDashboard.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')
################################################################################
# Teacher: Editing students and deleting them
################################################################################