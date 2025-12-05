from flask import Flask, render_template_string, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="jonathan",
    password="amongusishot34",
    database="eksempel_db"
    )

@app.route('/')
def index():

    cur = conn.cursor()
    
    cur.execute("SELECT navn, alder FROM brukere;")
    
    row = cur.fetchall()
    
    
    return render_template('index.html', brukere=row)

if __name__ == "__main__":
    app.run()