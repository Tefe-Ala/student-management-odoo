
from odoo import models, fields, api


class Enrollment(models.Model):
    _name = 'student.management.enrollment'
    _description = 'Student Enrollment'

    student_id = fields.Many2one(
        'student.management.student',
        string='Student',
        required=True
    )

    department_id = fields.Many2one(
        'student.management.department',
        string='Department',
        related='student_id.department_id',
        store=True
    )

    course_id = fields.Many2one(
        'student.management.course',
        string='Course',
        required=True
    )

    academic_year_id = fields.Many2one(
        'student.management.academic.year',
        string='Academic Year',
        required=True
    )

    semester_id = fields.Many2one(
        'student.management.semester',
        string='Semester',
        required=True
    )

    enrollment_date = fields.Date(
        string='Enrollment Date',
        default=fields.Date.today
    )

    status = fields.Selection(
        [
            ('enrolled', 'Enrolled'),
            ('completed', 'Completed'),
            ('dropped', 'Dropped')
        ],
        string='Status',
        default='enrolled',
        required=True
    )

    # ---------------------------------------------------------
    # DUPLICATE ENROLLMENT PREVENTION
    # ---------------------------------------------------------

    _sql_constraints = [
        (
            'unique_student_course_year_semester',
            'unique(student_id, course_id, academic_year_id, semester_id)',
            'This student is already enrolled in this course for this academic year and semester.'
        ),
    ]

    # ---------------------------------------------------------
    # CREATE ENROLLMENT
    # ---------------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        enrollments = super().create(vals_list)

        for enrollment in enrollments:
            enrollment._add_course_to_student()

        return enrollments

    # ---------------------------------------------------------
    # UPDATE ENROLLMENT
    # ---------------------------------------------------------

    def write(self, vals):
        old_relationships = []

        if 'student_id' in vals or 'course_id' in vals:
            for enrollment in self:
                old_relationships.append({
                    'enrollment_id': enrollment.id,
                    'student_id': enrollment.student_id.id,
                    'course_id': enrollment.course_id.id,
                })

        result = super().write(vals)

        if 'student_id' in vals or 'course_id' in vals:

            for old in old_relationships:

                old_student_id = old['student_id']
                old_course_id = old['course_id']

                if old_student_id and old_course_id:

                    old_student = self.env[
                        'student.management.student'
                    ].browse(old_student_id)

                    other_enrollment = self.search_count([
                        ('id', '!=', old['enrollment_id']),
                        ('student_id', '=', old_student_id),
                        ('course_id', '=', old_course_id),
                    ])

                    if not other_enrollment and old_student.exists():
                        old_student.course_ids = [
                            (3, old_course_id)
                        ]

            for enrollment in self:
                enrollment._add_course_to_student()

        return result

    # ---------------------------------------------------------
    # DELETE ENROLLMENT
    # ---------------------------------------------------------

    def unlink(self):

        relationships = []

        for enrollment in self:

            if enrollment.student_id and enrollment.course_id:
                relationships.append({
                    'student_id': enrollment.student_id.id,
                    'course_id': enrollment.course_id.id,
                })

        result = super().unlink()

        for relationship in relationships:

            student_id = relationship['student_id']
            course_id = relationship['course_id']

            other_enrollment = self.search_count([
                ('student_id', '=', student_id),
                ('course_id', '=', course_id),
            ])

            if not other_enrollment:

                student = self.env[
                    'student.management.student'
                ].browse(student_id)

                if student.exists():
                    student.course_ids = [
                        (3, course_id)
                    ]

        return result

    # ---------------------------------------------------------
    # HELPER METHOD
    # ---------------------------------------------------------

    def _add_course_to_student(self):

        for enrollment in self:

            if enrollment.student_id and enrollment.course_id:

                enrollment.student_id.course_ids = [
                    (4, enrollment.course_id.id)
                ]
