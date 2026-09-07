from odoo import models, fields


class Course(models.Model):
    _name = 'student.management.course'
    _description = 'Course'

    name = fields.Char(
        string='Course Name',
        required=True
    )

    code = fields.Char(
        string='Course Code',
        required=True
    )

    department_id = fields.Many2one(
        'student.management.department',
        string='Department',
        required=True
    )

    credit_hours = fields.Integer(
        string='Credit Hours',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    student_ids = fields.Many2many(
        'student.management.student',
        'student_course_rel',
        'course_id',
        'student_id',
        string='Students'
    )