from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, DateField
from passlib.hash import sha256_crypt
from functools import wraps
from application import mysql
from application.teacherOps.forms import ParentRegisterForm, RegisterStudentForm, RegisterTeacherForm, RegisterInstrumentForm
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='kindergarten';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='first';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='second';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='third';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='fourth';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='fifth';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT *FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID JOIN teacher t ON s.Teacher_TeacherID = t.TeacherID WHERE g.gradelevel ='sixth';")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT * FROM instrument i LEFT OUTER JOIN student s ON s.Instrument_InstrumentID = i.instrumentID;")
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
    result = cur.execute("SELECT * FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID WHERE i.instrumentID != 5000 order by ReturnDate ASC;")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
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
    result = cur.execute("SELECT * FROM student s JOIN instrument i ON s.Instrument_InstrumentID = i.InstrumentID WHERE i.instrumentID != 5000 order by ReturnDate DESC;")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/sorts.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@teacher.route('/teacherDashboardViewAllStudents')
@is_logged_in_with_permission
def teacherDashboardViewAllStudents():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT *FROM student s JOIN teacher i ON s.Teacher_TeacherID = i.teacherID JOIN gradelevel g ON s.Gradelevel_GradelevelID = g.GradelevelID;")
    studentInfo = cur.fetchall()

    if result > 0:
        return render_template('teacher/viewStudents.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')

@is_logged_in_with_permission
@teacher.route('/teacherDashboardCheckTeachers')
def teacherDashboardCheckTeacher():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM teacher")
    teacherInfo = cur.fetchall()
    if result > 0:
        return render_template('teacher/checkTeacher.html', teacherInfo=teacherInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')    
################################################################################
# Teacher: Editing students, parents and deleting them
################################################################################
@teacher.route('/createParent', methods=['Get','Post'])
@is_logged_in_with_permission
def createParent():
    form = ParentRegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        parentID = form.parentID.data
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        checkUsername = cur.execute("SELECT * FROM parent WHERE Parentusername = %s", [username])
        checkEmail = cur.execute("SELECT * FROM parent WHERE parentEmail =%s", [email])
        if checkUsername > 0:
            flash('Username has been taken, please enter a unique username', 'danger')
            return render_template('teacher/teacherDashboard.html')
        elif checkEmail > 0:
            flash('Email is already registered to an account, if you have forgotten your password please send an email to Easton@gmail.com', 'danger')
            return render_template('teacher/teacherDashboard.html')
        elif checkUsername == 0 and checkEmail == 0:
            cur.execute("INSERT INTO parent(parentFname, parentLname, parentEmail, ParentID, Parentusername, ParentPassword) VALUES(%s,%s,%s,%s,%s,%s)", (firstName, lastName, email, parentID, username, password))
            #%d does represent a number however it will throw an error if used with a small number.
        #commit to finish
        mysql.connection.commit()

        #close connection
        cur.close()
        flash('Parent created', 'success')
        return redirect(url_for('teacher.teacherDashboard'))
    return render_template('teacher/createParent.html', form=form)
################################################################################
# Teacher: Create Student
################################################################################
@teacher.route('/createStudent', methods=['Get','Post'])
@is_logged_in_with_permission
def createStudent():
    form = RegisterStudentForm(request.form)
    if request.method == 'POST' and form.validate():
        studentID = form.studentID.data
        firstName = form.firstName.data
        lastName = form.lastName.data
        gradelevel = form.gradelevel.data
        teacherID = form.teacherID.data
        instrumentID = "5000"

        # create cursor
        cur = mysql.connection.cursor()

        checkStudentID = cur.execute("SELECT * FROM student WHERE StudentID =%s", [studentID])
        if checkStudentID > 0:
            flash('Student already exsists', 'danger')
            return render_template('teacher/teacherDashboard.html')
        else:
            cur.execute("INSERT INTO student(StudentID, StudentFname, StudentLname, Gradelevel_GradelevelID, Teacher_TeacherID, Instrument_InstrumentID) VALUES(%s,%s,%s,%s,%s,%s)", (studentID, firstName, lastName, gradelevel, teacherID, instrumentID))
            #%d does represent a number however it will throw an error if used with a small number.
        #commit to finish
        mysql.connection.commit()

        #close connection
        cur.close()
        flash('student created', 'success')
        return redirect(url_for('teacher.teacherDashboard'))
    return render_template('teacher/createStudent.html', form=form)
################################################################################
# Teacher: Create Teacher
################################################################################
@teacher.route('/createTeacher', methods=['Get','Post'])
@is_logged_in_with_permission
def createTeacher():
    form = RegisterTeacherForm(request.form)
    if request.method == 'POST' and form.validate():
        teacherID = form.teacherID.data
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        checkUsername = cur.execute("SELECT * FROM teacher WHERE TeacherUsername = %s", [username])
        checkEmail = cur.execute("SELECT * FROM teacher WHERE TeacherEmail =%s", [email])
        if checkUsername > 0:
            flash('Username has been taken, please enter a unique username', 'danger')
            return render_template('teacher/teacherDashboard.html')
        elif checkEmail > 0:
            flash('Email is already registered to an account, if you have forgotten your password please send an email to Easton@gmail.com', 'danger')
            return render_template('teacher/teacherDashboard.html')
        elif checkUsername == 0 and checkEmail == 0:
            cur.execute("INSERT INTO teacher(TeacherID, TeacherFname, TeacherLname, TeacherEmail, TeacherUsername, TeacherPassword) VALUES(%s,%s,%s,%s,%s,%s)", (teacherID, firstName, lastName, email, username, password))
            #%d does represent a number however it will throw an error if used with a small number.
        #commit to finish
        mysql.connection.commit()

        #close connection
        cur.close()
        flash('teacher created', 'success')
        return redirect(url_for('teacher.teacherDashboard'))
    return render_template('teacher/createTeacher.html', form=form)
################################################################################
# Teacher: Create Instrument
################################################################################
@teacher.route('/createInstrument', methods=['Get','Post'])
@is_logged_in_with_permission
def createInstrument():
    form = RegisterInstrumentForm(request.form)
    if request.method == 'POST' and form.validate():
        instrumentID = form.instrumentID.data
        instrumentName = form.instrumentName.data.lower()
        instrumentLost = "0"
        instrumentCheckedOut = "0"
        checkOutDate = "0000-00-00"
        returnDate = "0000-00-00"
        
        # create cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO instrument(InstrumentID, InstrumentName, InstrumentLost, InstrumentCheckedOut, CheckOutDate, ReturnDate) VALUES(%s,%s,%s,%s,%s,%s)", (instrumentID, instrumentName, instrumentLost, instrumentCheckedOut, checkOutDate, returnDate))
        #%d does represent a number however it will throw an error if used with a small number.
        #commit to finish
        mysql.connection.commit()

        #close connection
        cur.close()
        flash('instrument created', 'success')
        return redirect(url_for('teacher.teacherDashboard'))
    return render_template('teacher/createInstrument.html', form=form)
################################################################################
# Teacher: Edit Students
################################################################################
@teacher.route('/editStudent/<string:studentID>', methods=['GET', 'POST'])
@is_logged_in_with_permission
def editStudent(studentID):
    # Create cursor
    cur = mysql.connection.cursor()
    # Get student by id
    result = cur.execute("SELECT * FROM student WHERE StudentID = %s", [studentID])
    student = cur.fetchone()
    sessionStudentID = student['StudentID']
    cur.close()
    # Get form
    form = RegisterStudentForm(request.form)

    # Populate student from DB
    form.studentID.data = student['StudentID']
    form.firstName.data = student['StudentFname']
    form.lastName.data = student['StudentLname']
    form.gradelevel.data = student['Gradelevel_GradelevelID']
    form.teacherID.data = student['Teacher_TeacherID']
    form.instrumentID.data = student['Instrument_InstrumentID']

    if request.method == 'POST' and form.validate():
        studentID = request.form['studentID']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        gradelevel = request.form['gradelevel']
        teacherID = request.form['teacherID']
        instrumentID = request.form['instrumentID']

        # Create Cursor
        cur = mysql.connection.cursor()
        # Execute
        cur.execute ("""
        UPDATE student
        SET StudentID=%s, StudentFname=%s, StudentLname=%s, Gradelevel_GradelevelID=%s, Teacher_TeacherID=%s, Instrument_InstrumentID=%s
        WHERE StudentID=%s
        """, (studentID, firstName, lastName, gradelevel, teacherID, instrumentID, sessionStudentID))
        # Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('Student updated', 'success')

        return redirect(url_for('teacher.teacherDashboard'))

    return render_template('teacher/editStudent.html', form=form)
################################################################################
# Teacher: Edit Parents
################################################################################
@teacher.route('/editParent/<string:parentID>', methods=['GET', 'POST'])
@is_logged_in_with_permission
def editParent(parentID):
    # Create cursor
    cur = mysql.connection.cursor()
    # Get student by id
    result = cur.execute("SELECT * FROM parent WHERE ParentID = %s", [parentID])
    parent = cur.fetchone()
    sessionParentID = parent['ParentID']
    sessionPassword = parent['ParentPassword']
    cur.close()
    # Get form
    form = ParentRegisterForm(request.form)

    # Populate student from DB
    form.parentID.data = parent['ParentID']
    form.firstName.data = parent['ParentFname']
    form.lastName.data = parent['parentLname']
    form.email.data = parent['parentEmail']
    form.username.data = parent['Parentusername']

    if request.method == 'POST':
        parentID = request.form['parentID']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        username = request.form['username']

        #create cursor to update the rest of the database
        cur = mysql.connection.cursor()
        # Execute
        cur.execute ("""
        UPDATE parent
        SET ParentID=%s, ParentFname=%s, parentLname=%s, parentEmail=%s, Parentusername=%s
        WHERE ParentID=%s
        """, (parentID, firstName, lastName, email, username, sessionParentID))

         # Commit to DB
        mysql.connection.commit()

         #Close connection
        cur.close()

        flash('Parent updated', 'success')

        return redirect(url_for('teacher.teacherDashboard'))

    return render_template('teacher/editParent.html', form=form)
################################################################################
# Teacher: Checkout instruments
################################################################################
@teacher.route('/checkOutInstrument', methods=['Get','Post'])
@is_logged_in_with_permission
def checkOutInstrument():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM student LEFT JOIN instrument ON student.Instrument_InstrumentID = 5000 WHERE instrument.InstrumentID = 5000;")
    studentInfo = cur.fetchall()
    if result > 0:
        return render_template('teacher/checkOutInstrument.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')
################################################################################
# Teacher: Checkout Established
################################################################################
@teacher.route('/assignInstruments/<string:studentID>', methods=['Get','Post'])
@is_logged_in_with_permission
def assignInstruments(studentID):
    # Create cursor
    cur = mysql.connection.cursor()
    # Get student by id
    result = cur.execute("SELECT * FROM student WHERE StudentID = %s", [studentID])
    student = cur.fetchone()
    sessionStudentID = student['StudentID']
    # Get form
    form = RegisterInstrumentForm(request.form)

    if request.method == 'POST':
        instrumentID = request.form['instrumentID']
        checkOutDate = request.form['checkOutDate']
        returnDate = request.form['returnDate']

        checkForInstrument = cur.execute("SELECT * FROM instrument WHERE InstrumentID = %s", [instrumentID])
        if checkForInstrument > 0:
             cur.execute ("""
            UPDATE instrument
            SET InstrumentCheckedOut =%s, CheckOutDate =%s, ReturnDate =%s
            WHERE InstrumentID=%s
            """, ("1", checkOutDate, returnDate, instrumentID))
             mysql.connection.commit()

             cur.execute ("""
            UPDATE student
            SET Instrument_InstrumentID =%s
            WHERE StudentID=%s
            """, (instrumentID, sessionStudentID))
             mysql.connection.commit()

        cur.close()
        flash('Instrument Checked Out', 'success')
        return redirect(url_for('teacher.teacherDashboard'))
    return render_template('teacher/assignInstruments.html', form=form)
################################################################################
# Teacher: Return Instrument
################################################################################
@teacher.route('/returnInstrument', methods=['Get','Post'])
@is_logged_in_with_permission
def returnInstrument():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM student LEFT JOIN instrument ON student.Instrument_InstrumentID = instrument.InstrumentID WHERE student.Instrument_InstrumentID != 5000;")
    studentInfo = cur.fetchall()
    if result > 0:
        return render_template('teacher/returnInstrument.html', studentInfo=studentInfo)
    else:
        message = 'No db entries found Found'
        return render_template('teacher/teacherDashboard.html', message=message)
    # Close connection
    cur.close()
    return('teacher/teacherDashboard.html')
################################################################################
# Teacher: DB updates the checkout
################################################################################
@teacher.route('/restockInstruments/<string:studentID>', methods=['Get','Post'])
@is_logged_in_with_permission
def restockInstruments(studentID):
    # Create cursor
    cur = mysql.connection.cursor()
    # Get student by id
    result = cur.execute("SELECT * FROM student WHERE StudentID = %s", [studentID])
    student = cur.fetchone()
    sessionStudentID = student['StudentID']
    # Get form
    form = RegisterInstrumentForm(request.form)

    if request.method == 'POST':
        instrumentID = request.form['instrumentID']

        checkForInstrument = cur.execute("SELECT * FROM instrument WHERE InstrumentID = %s", [instrumentID])
        if checkForInstrument > 0:
             cur.execute ("""
            UPDATE instrument
            SET InstrumentCheckedOut =%s, CheckOutDate =%s, ReturnDate =%s
            WHERE InstrumentID=%s
            """, ("0", "0000-00-00", "0000-00-00", instrumentID))
             mysql.connection.commit()

             cur.execute ("""
            UPDATE student
            SET Instrument_InstrumentID =%s
            WHERE StudentID=%s
            """, ("5000", sessionStudentID))
             mysql.connection.commit()

        cur.close()
        flash('Instrument Returned', 'success')
        return redirect(url_for('teacher.teacherDashboard'))
    return render_template('teacher/restockInstruments.html', form=form)