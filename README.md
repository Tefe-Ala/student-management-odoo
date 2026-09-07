# 🎓 Student Management System — Odoo 19

> A custom academic management module built from scratch with Odoo 19, Python, XML, PostgreSQL, and the Odoo ORM.

[![Odoo](https://img.shields.io/badge/Odoo-19-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-EDUCATIONAL-FF6B6B?style=for-the-badge)](LICENSE)

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
🎯 Core workflow

                    ┌─────────────────┐
                    │     Student     │
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
       ┌──────▼──────┐               ┌──────▼──────┐
       │ Department  │               │   Courses   │
       └─────────────┘               └──────┬──────┘
                                            │
                                    ┌───────▼────────┐
                                    │   Enrollment    │
                                    └───────┬────────┘
                                            │
                         ┌──────────────────┼──────────────────┐
                         │                  │                  │
                  Academic Year         Semester           Status

        ✨ Key Features
| Feature | Description |
|---|---|
| 👨‍🎓 **Student Management** | Create and manage student records |
| 🏫 **Department Management** | Organize students by department |
| 📚 **Course Management** | Create and manage academic courses |
| 📅 **Academic Years** | Manage academic-year information |
| 🗓️ **Semester Management** | Organize courses by semester |
| 🔗 **Student–Course Relationship** | Many2many relationship between students and courses |
| 📝 **Enrollment Management** | Register students into courses |
| 🔄 **Automatic Synchronization** | Enrollment automatically updates student courses |
| 📊 **Enrollment Status** | Enrolled, Completed, or Dropped |


🖥️ Screenshots

Explore the system through the screenshots below.

👨‍🎓 Student Management

![Student List](screenshots/student_list.png)


Student Form

![Student List](screenshots/student_form.png)


📚 Course Management

![Student List](screenshots/course_list.png)


Course Form

![Student List](screenshots/course_form.png)


📝 Enrollment Management

![Student List](screenshots/enrollment_list.png)


Enrollment Form

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| 🟣 **Odoo 19** | ERP / Application Framework |
| 🐍 **Python** | Backend Development |
| 📄 **XML** | Views and UI Configuration |
| 🐘 **PostgreSQL** | Database |
| 🔗 **Odoo ORM** | Database and Business Logic |
| 🔀 **Git** | Version Control |
| ☁️ **GitHub** | Source Code Management |


## 🧪 Testing

The Enrollment workflow was thoroughly tested against the following scenarios:

### ✅ Test Cases

| # | Test Scenario | Status | Description |
|---|---------------|--------|-------------|
| 1 | Create enrollment | ✅ Passed | Verify enrollment creation triggers synchronization |
| 2 | Update student | ✅ Passed | Ensure student changes reflect in enrollments |
| 3 | Update course | ✅ Passed | Verify course changes sync with enrollments |
| 4 | Delete enrollment | ✅ Passed | Confirm deletion removes course if no other enrollments |
| 5 | Synchronize Student-Course relationship | ✅ Passed | Test automatic M2M synchronization |
| 6 | Prevent duplicate enrollment | ✅ Passed | Verify duplicate enrollment prevention |
| 7 | Preserve course relationship | ✅ Passed | Confirm course remains when other enrollments exist |

> 🎯 **Testing Focus**: The testing focused particularly on maintaining **data consistency** between related Odoo models, ensuring the **Student ↔ Course ↔ Enrollment** relationship stays synchronized at all times.
## 📈 What This Project Demonstrates

This project demonstrates practical experience with modern Odoo development across multiple domains.

### 🏗️ **Odoo Development**

| Area | Technologies & Concepts |
|------|------------------------|
| **Module Development** | Odoo custom module development |
| **Backend** | Python backend programming, Odoo ORM |
| **Frontend** | XML view development |
| **Database** | Relational database modeling, PostgreSQL |

### 🔗 **ORM & Relationships**

| Concept | Implementation |
|---------|----------------|
| **Relationships** | Many2one, Many2many relationships, Related fields |
| **Constraints** | SQL constraints, Data integrity |
| **CRUD Operations** | create(), write(), unlink() customization |

### 🔧 **Development Workflow**

| Aspect | Skills |
|--------|--------|
| **Business Logic** | Business workflow automation |
| **Security** | Access control, Security rules |
| **Version Control** | Git and GitHub workflow |

## 🔮 Future Development

The system can be expanded into a more complete academic ERP solution. Here are the planned features for future releases:

### 📊 **Academic Management**

| Priority | Feature | Description | Status |
|----------|---------|-------------|--------|
| 🔴 High | 📊 Student results and grades | Record and manage student academic performance | 🟡 Planned |
| 🔴 High | 📅 Attendance management | Track student attendance per course/session | 🟡 Planned |
| 🟡 Medium | 👨‍🏫 Teacher management | Manage teacher profiles and assignments | 🟡 Planned |
| 🟡 Medium | 📝 Assignment management | Create, submit, and grade assignments | 🟡 Planned |
| 🟡 Medium | 📈 Student performance tracking | Analytics and progress monitoring | 🟡 Planned |

### 🔔 **Communication & Portal**

| Priority | Feature | Description | Status |
|----------|---------|-------------|--------|
| 🟢 Low | 🔔 Notifications | Automated alerts for students and teachers | 🟡 Planned |
| 🟢 Low | 🌐 Student portal | Self-service portal for students | 🟡 Planned |

### 📊 **Analytics & Reporting**

| Priority | Feature | Description | Status |
|----------|---------|-------------|--------|
| 🟡 Medium | 📊 Academic dashboards | Real-time academic insights | 🟡 Planned |
| 🟢 Low | 📑 Reporting | Generate academic reports | 🟡 Planned |
| 🟢 Low | 🎓 Academic transcript generation | Official student transcripts | 🟡 Planned |

---







👨‍💻 About the Project

This project was developed as a practical demonstration of Odoo technical development, focusing on custom module creation, relational data modeling, ORM programming, and business workflow automation.

It represents the implementation of an academic management workflow using the Odoo framework rather than relying solely on standard Odoo modules.

## ⭐ Support the Project

If you find this project useful or interesting, here's how you can support it:

### 🤝 **Ways to Contribute**

<div align="center">

| Action | Why | How |
|--------|-----|-----|
| ⭐ **Star** the repository | Show your appreciation | Click the star button at the top |
| 🍴 **Fork** the project | Build upon it | Click the fork button |
| 💡 **Explore** the code | Learn from it | Browse the repository |
| 📢 **Share** with others | Help the community | Share on social media |
| 🐛 **Report** issues | Make it better | Open a GitHub issue |
| 💬 **Suggest** features | Shape the roadmap | Start a discussion |

</div>

---

### 📈 **Project Status**

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/Tefe-Ala/student-management-odoo?style=for-the-badge&logo=github)](https://github.com/Tefe-Ala/student-management-odoo/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Tefe-Ala/student-management-odoo?style=for-the-badge&logo=github)](https://github.com/Tefe-Ala/student-management-odoo/network)
[![GitHub watchers](https://img.shields.io/github/watchers/Tefe-Ala/student-management-odoo?style=for-the-badge&logo=github)](https://github.com/Tefe-Ala/student-management-odoo/watchers)

</div>

---


## 📄 License

[![License](https://img.shields.io/badge/License-EDUCATIONAL-blue)](LICENSE)

**This project is intended for educational and development purposes.**


<div align="center"> <b>Built with ❤️ using Odoo 19</b> </div>
