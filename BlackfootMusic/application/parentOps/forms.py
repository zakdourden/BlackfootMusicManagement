from flask import Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField, DateField
from passlib.hash import sha256_crypt
from functools import wraps
from application import mysql

class ParentRegisterForm(Form):
    ParentID = IntegerField('Parent ID', [validators.input_required()])
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
    StudentID = IntegerField('Student ID', [validators.input_required()])