from odoo import models, fields


class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'

    name = fields.Char(
        string='Student Name',
        required=True
    )

    student_id = fields.Char(
        string='Student ID',
        required=True
    )

    email = fields.Char(
        string='Email'
    )

    phone = fields.Char(
        string='Phone'
    )

    date_of_birth = fields.Date(
        string='Date of Birth'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    department_id = fields.Many2one(
        'student.management.department',
        string='Department',
        required=True
    )

    course_ids = fields.Many2many(
        'student.management.course',
        'student_course_rel',
        'student_id',
        'course_id',
        string='Courses'
    )