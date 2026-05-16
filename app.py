from flask import Flask, render_template, request, redirect
import mysql.connector
from urllib.parse import urlparse
import os

app = Flask(__name__)

# MYSQL PUBLIC URL
mysql_url = os.environ.get("MYSQL_PUBLIC_URL")

# PARSE DATABASE URL
url = urlparse(mysql_url)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host=url.hostname,
    user=url.username,
    password=url.password,
    database=url.path[1:],
    port=url.port
)

@app.route('/', methods=['GET', 'POST'])
def home():

    cursor = db.cursor()

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

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    return render_template(
        'index.html',
        students=students
    )

if __name__ == '__main__':
    app.run(debug=True)