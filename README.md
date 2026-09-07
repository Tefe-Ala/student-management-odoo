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
