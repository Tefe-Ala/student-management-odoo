from odoo import models, fields


class Department(models.Model):
    _name = 'student.management.department'
    _description = 'Department'

    name = fields.Char(
        string='Department Name',
        required=True
    )

    code = fields.Char(
        string='Department Code',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )
    student_ids = fields.One2many(
        'student.management.student',
        'department_id',
        string='Students'
    )
    course_ids = fields.One2many(
        'student.management.course',
        'department_id',
        string='Courses'
)