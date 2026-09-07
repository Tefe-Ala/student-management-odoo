from odoo import models, fields


class AcademicYear(models.Model):
    _name = 'student.management.academic.year'
    _description = 'Academic Year'

    name = fields.Char(
        string='Academic Year',
        required=True
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )