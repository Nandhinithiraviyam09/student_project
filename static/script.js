async function addStudent() {

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const course = document.getElementById("course").value;

    const response = await fetch('/add_student', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            name,
            email,
            course
        })
    });

    const data = await response.json();

    alert(data.message);

    loadStudents();
}

async function loadStudents() {

    const response = await fetch('/students');

    const students = await response.json();

    const studentList = document.getElementById('studentList');

    studentList.innerHTML = '';

    students.forEach(student => {

        studentList.innerHTML += `
            <div class="student-card">
                <h3>${student.name}</h3>
                <p>${student.email}</p>
                <p>${student.course}</p>
            </div>
        `;
    });
}

loadStudents();