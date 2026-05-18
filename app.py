from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host=os.environ.get("MYSQLHOST"),
    user=os.environ.get("MYSQLUSER"),
    password=os.environ.get("MYSQLPASSWORD"),
    database=os.environ.get("MYSQLDATABASE"),
    port=int(os.environ.get("MYSQLPORT"))
)

cursor = db.cursor()

# HOME PAGE
@app.route('/')
def home():

    # FETCH STUDENTS
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return render_template(
        'index.html',
        students=students
    )

# ADD STUDENT
@app.route('/add', methods=['POST'])
def add_student():

    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    # INSERT DATA
    sql = "INSERT INTO students(name, email, course) VALUES (%s, %s, %s)"
    values = (name, email, course)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

# DELETE STUDENT
@app.route('/delete/<int:id>')
def delete_student(id):

    sql = "DELETE FROM students WHERE id=%s"
    value = (id,)

    cursor.execute(sql, value)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)