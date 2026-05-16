from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# MYSQL CONNECTION
db = mysql.connector.connect(
    host=os.environ.get("MYSQLHOST"),
    user=os.environ.get("MYSQLUSER"),
    password=os.environ.get("MYSQLPASSWORD"),
    database=os.environ.get("MYSQLDATABASE"),
    port=int(os.environ.get("MYSQLPORT"))
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        student_name = request.form['student_name']
        student_email = request.form['student_email']
        student_course = request.form['student_course']

        sql = """
        INSERT INTO students(name, email, course)
        VALUES(%s, %s, %s)
        """

        values = (
            student_name,
            student_email,
            student_course
        )

        cursor.execute(sql, values)

        db.commit()

        return redirect('/')

    # FETCH STUDENTS
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    return render_template(
        'index.html',
        students=students
    )

if __name__ == '__main__':
    app.run(debug=True)