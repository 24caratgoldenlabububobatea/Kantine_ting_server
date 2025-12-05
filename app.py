from flask import Flask, render_template, redirect
import mysql.connector
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.secret_key = 'hemmlig_nokkel'

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="jonathan",
        password="amongusishot34",
        database="eksempel_db"
    )
