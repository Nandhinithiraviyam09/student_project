from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MYSQL CONNECTION

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="asdf",
    database="student_db"
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])

def home():

    if request.method == 'POST':

        student_name = request.form['student_name']
        student_email = request.form['student_email']
        student_course = request.form['student_course']

        sql = """
        INSERT INTO students
        (student_name, student_email, student_course)

        VALUES (%s, %s, %s)
        """

        values = (
            student_name,
            student_email,
            student_course
        )

        cursor.execute(sql, values)

        db.commit()

        print("Student Registered Successfully")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)