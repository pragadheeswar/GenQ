from flask import Flask,render_template,request,flash,url_for,redirect
from getA import getA
from getB import getB
from getC import getC
from getA50 import getA50
from getB50 import getB50
from  addQ import addQ
import sqlite3

app = Flask(__name__)
app.secret_key = "roman_prakash"

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/teacher',methods=["get","POST"])
def teacher():
    if request.method=="POST":
        name = request.form["name"]
        # email =  request.form['email']
        password = request.form['password']

        if password != 'password' or name != 'teacher':
            flash("invalid password")
            return redirect(url_for('teacher'))
        else:
            flash("successfully logged in")
            return redirect(url_for('get'))

    return render_template('teacher.html')

@app.route('/admin',methods=["GET","POST"])
def admin():
    if request.method=="POST":
        name = request.form["name"]
        # email =  request.form['email']
        password = request.form['password']

        if password != 'password' or name != 'admin':
            flash("invalid password")
            return redirect(url_for('admin'))
        else:
            flash("successfully logged in")
            return redirect(url_for('insertion'))

    return render_template('admin.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/insertion',methods=["POST","GET"])
def insertion():
    if request.method=="POST":
        subject=request.form['subject']
        question=request.form['question']
        unit=request.form['unit']
        level=request.form['level']
        importance=request.form['importance']
        mark=request.form['mark']
        addQ(subject,question,unit,level,mark,importance)
    return render_template('insertion.html')

@app.route('/get',methods=["POST","GET"])
def get(): 
    if request.method=="POST":
        course=request.form['course']
        subject=request.form['subjectcode']
        sem=request.form['sem']
        questionpaper=request.form['questionpaper']
        marks=request.form['marks']
        timing=request.form['timing']
        unit=request.form.getlist('unit')
        if marks=="100":
            two_mark=getA()
            twelve_mark=getB()
            sixteen_mark=getC()
            return render_template('question1.html',name=questionpaper,timing=timing,marks=marks,two_mark=two_mark,
            twelve_mark=twelve_mark,sixteen_mark=sixteen_mark)
        else:
            two_mark_50=getA50(unit)
            twelve_mark_50=getB50(unit)
            return render_template('question2.html',name=questionpaper,timing=timing,marks=marks,two_mark=two_mark_50,twelve_mark=twelve_mark_50)
    return render_template('get.html')

@app.route('/database_Two')
def database_Two():
    connection=sqlite3.connect("questions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Two_marks")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('database.html',heading="Two Marks",rows=rows)

@app.route('/database_Twelve')
def database_Twelve():
    connection=sqlite3.connect("questions.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Twelve_marks")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('database.html',heading="Twelve Marks",rows=rows)

if __name__ == "__main__":
    app.run(debug=True)