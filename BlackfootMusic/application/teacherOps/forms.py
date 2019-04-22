from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, DateField, BooleanField
from passlib.hash import sha256_crypt
from functools import wraps
from application import mysql
from datetime import date

class ParentRegisterForm(Form):
    parentID = IntegerField('Parent ID', [validators.input_required()])
    firstName = StringField('First name', [validators.Length(min=1, max=50), validators.input_required()])
    lastName = StringField('Last name', [validators.Length(min=1, max=50), validators.input_required()])
    email = StringField('Email', [validators.Length(min=4, max=50), validators.input_required()])
    username = StringField('Username', [validators.Length(min=3, max=25), validators.input_required()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('confirm Password')

class RegisterStudentForm(Form):
    studentID = IntegerField('Student ID', [validators.input_required()])
    firstName = StringField('First name', [validators.Length(min=1, max=50), validators.input_required()])
    lastName = StringField('Last name', [validators.Length(min=1, max=50), validators.input_required()])
    gradelevel = IntegerField('Grade ID &nbsp<sup><em>valid options are 0-7</em></sup>', [validators.input_required()])
    teacherID = IntegerField('Teacher ID &nbsp<sup><em>valid options are 0-2</em></sup>', [validators.input_required()])
    instrumentID = IntegerField('Instrument ID')

class RegisterTeacherForm(Form):
    teacherID = IntegerField('Teacher ID', [validators.input_required()])
    firstName = StringField('First name', [validators.Length(min=1, max=50), validators.input_required()])
    lastName = StringField('Last name', [validators.Length(min=1, max=50), validators.input_required()])
    email = StringField('Email', [validators.Length(min=4, max=50), validators.input_required()])
    username = StringField('Username', [validators.Length(min=3, max=25), validators.input_required()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('confirm Password')

class RegisterInstrumentForm(Form):
    instrumentID = StringField('Instrument ID', [validators.Length(min=1, max=50), validators.input_required()])
    instrumentName = StringField('Instrument name', [validators.Length(min=1, max=50), validators.input_required()])
    instrumentLost = BooleanField('Instrument lost?')
    instrumentCheckedOut = BooleanField('Checking out an instrument?')
    checkOutDate = DateField('check out date &nbsp<sup><em>valid date format is YYYY-MM-DD</em></sup>',default=date.today)
    returnDate = DateField('End Date &nbsp<sup><em>valid date format is YYYY-MM-DD</em></sup>',default=date.today)

