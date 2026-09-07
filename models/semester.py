from odoo import models, fields


class Semester(models.Model):
    _name = 'student.management.semester'
    _description = 'Semester'

    name = fields.Char(
        string='Semester',
        required=True
    )

    code = fields.Char(
        string='Code',
        required=True
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )