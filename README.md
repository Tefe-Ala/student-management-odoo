# 🎓 Student Management System — Odoo 19

> A custom academic management module built from scratch with Odoo 19, Python, XML, PostgreSQL, and the Odoo ORM.

[![Odoo](https://img.shields.io/badge/Odoo-19-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-EDUCATIONAL-FF6B6B?style=for-the-badge)](LICENSE)

---

## 🚀 What is this?

The **Student Management System** is a custom Odoo 19 module designed to manage the core academic activities of an educational institution.

Instead of treating students, courses, and enrollments as isolated records, the system **models their relationships** and keeps them **synchronized automatically**.

<details>
<summary><b>📖 Why build this?</b></summary>

Many educational institutions struggle with:
- ❌ Disconnected student and course data
- ❌ Manual enrollment tracking
- ❌ Duplicate or inconsistent records
- ❌ No automatic relationship synchronization

This module solves these problems by providing a unified academic management system.
</details>

---

## 🎯 Core Workflow

```mermaid
graph TD
    A[Student] --> B[Department]
    A --> C[Courses]
    C --> D[Enrollment]
    D --> E[Academic Year]
    D --> F[Semester]
    D --> G[Status]
    B --> H[Academic Structure]
    E --> I[Planning]
    F --> J[Course Offering]
✨ Key Features
Feature	Description	Status
👨‍🎓 Student Management	Create and manage student records	✅
🏫 Department Management	Organize students by department	✅
📚 Course Management	Create and manage academic courses	✅
📅 Academic Years	Manage academic-year information	✅
🗓️ Semester Management	Organize courses by semester	✅
🔗 Student-Course Relationship	Many2many relationship between students and courses	✅
📝 Enrollment Management	Register students into courses	✅
🔄 Automatic Synchronization	Enrollment automatically updates student courses	✅
🛡️ Duplicate Prevention	Prevent duplicate enrollment for the same academic period	✅
📊 Enrollment Status	Enrolled, Completed, or Dropped	✅
🔥 Highlight Feature — Smart Enrollment Synchronization
One of the most important parts of this project is the relationship between:

Student ↔ Course ↔ Enrollment
The system doesn't simply create an enrollment record. It also keeps the Student's course information synchronized with enrollment records.

➕ When an enrollment is created



🔄 When an enrollment is updated




🗑️ When an enrollment is deleted






🎯 Result: This prevents the Enrollment model and the Student-Course relationship from becoming inconsistent.

🖥️ Screenshots
Explore the system through the screenshots below.

👨‍🎓 Student Management
<table> <tr> <td><b>Student List</b></td> <td><b>Student Form</b></td> </tr> <tr> <td><img src="screenshots/student_list.png" alt="Student List" width="400"></td> <td><img src="screenshots/student_form.png" alt="Student Form" width="400"></td> </tr> </table>
📚 Course Management
<table> <tr> <td><b>Course List</b></td> <td><b>Course Form</b></td> </tr> <tr> <td><img src="screenshots/course_list.png" alt="Course List" width="400"></td> <td><img src="screenshots/course_form.png" alt="Course Form" width="400"></td> </tr> </table>
📝 Enrollment Management
<table> <tr> <td colspan="2"><b>Enrollment Form</b></td> </tr> <tr> <td><img src="screenshots/enrollment_form1.png" alt="Enrollment Form 1" width="400"></td> <td><img src="screenshots/enrollment_form2.png" alt="Enrollment Form 2" width="400"></td> </tr> </table>
📂 Project Structure
text
student_management/
│
├── __init__.py
├── manifest.py
│
├── models/
│   ├── __init__.py
│   ├── student.py
│   ├── department.py
│   ├── course.py
│   ├── academic_year.py
│   ├── semester.py
│   └── enrollment.py
│
├── views/
│   └── student_views.xml
│
├── security/
│   └── ir.model.access.csv
│
├── screenshots/
│   ├── student_list.png
│   ├── student_form.png
│   ├── course_list.png
│   ├── course_form.png
│   ├── enrollment_list.png
│   └── enrollment_form.png
│
└── README.md
🛠️ Technology Stack
Backend
🐍 Python - Core programming language

🧩 Odoo ORM - Object-Relational Mapping

🟣 Odoo 19 Community Edition - Application Framework

Frontend / UI
📄 XML - Odoo Views

Database
🐘 PostgreSQL 17 - Relational database

Development Tools
💻 Visual Studio Code - IDE

🔀 Git - Version control

☁️ GitHub - Repository hosting

⚙️ Development Environment
The project was developed using:

✅ Odoo 19 Community Edition

✅ PostgreSQL 17

✅ Python 3.10+

✅ Windows development environment

✅ Visual Studio Code

✅ Git/GitHub

🧪 Testing
The Enrollment workflow was tested against the following scenarios:

☑ ✅ Create enrollment
☑ ✅ Update student
☑ ✅ Update course
☑ ✅ Delete enrollment
☑ ✅ Synchronize Student-Course relationship
☑ ✅ Prevent duplicate enrollment
☑ ✅ Preserve course relationship when another enrollment exists
Focus: The testing focused particularly on maintaining data consistency between related Odoo models.

📈 What This Project Demonstrates
This project demonstrates practical experience with:

☑ Odoo custom module development
☑ Python backend programming
☑ Odoo ORM
☑ Many2one relationships
☑ Many2many relationships
☑ Related fields
☑ CRUD operations
☑ create() customization
☑ write() customization
☑ XML view development
☑ Access control
☑ Relational database modeling
☑ Business workflow automation
🔮 Future Development
The system can be expanded into a more complete academic ERP solution.

<details> <summary><b>Planned Features</b></summary>
Priority	Feature
🔴 High	📊 Student results and grades
🔴 High	📅 Attendance management
🟡 Medium	👨‍🏫 Teacher management
🟡 Medium	📝 Assignment management
🟡 Medium	📈 Student performance tracking
🟢 Low	🔔 Notifications
🟢 Low	🌐 Student portal
🟢 Low	📊 Academic dashboards
🟢 Low	📑 Reporting
🟢 Low	🎓 Academic transcript generation
</details>
⚙️ Installation
1️⃣ Clone the repository
bash
git clone https://github.com/Tefe-Ala/student-management-odoo.git
2️⃣ Copy the module
Place the student_management folder inside your Odoo custom addons directory:

text
custom_addons/
└── student_management/
3️⃣ Update your Odoo configuration
Make sure your custom addons directory is included in addons_path:

Example:

ini
addons_path = addons,custom_addons
4️⃣ Restart Odoo
Restart your Odoo server.

5️⃣ Activate Developer Mode
In Odoo:

text
Settings → Activate Developer Mode
6️⃣ Update Apps List
Go to:

text
Apps → Update Apps List
7️⃣ Install the module
Search for:

text
Student Management
Then click:

text
Install
📂 Git Workflow
Future updates to this project can be pushed using:

bash
git add .
git commit -m "Describe your changes"
git push
👨‍💻 About the Project
This project was developed as a practical demonstration of Odoo technical development, focusing on:

🔧 Custom module creation

📊 Relational data modeling

🧩 ORM programming

🔄 Business workflow automation

It represents the implementation of an academic management workflow using the Odoo framework rather than relying solely on standard Odoo modules.

⭐ Support the Project
If you find this project useful or interesting:

⭐ Star the repository

🍴 Fork the project

💡 Explore the code

📢 Share it with other Odoo developers

🐛 Report issues

💬 Suggest improvements

📄 License
This project is intended for educational and development purposes.

🤝 Connect
https://img.shields.io/badge/GitHub-Tefe--Ala-181717?style=for-the-badge&logo=github
https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin

<div align="center"> <b>Built with ❤️ using Odoo 19</b> </div> ```
