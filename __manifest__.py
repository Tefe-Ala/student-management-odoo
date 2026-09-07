{
    'name': 'Student Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students, courses, and enrollments',
    'description': """
        This module allows you to manage students, courses, and enrollments in an educational institution.
    """,
    'author': 'Tefera Alagaw',
    'website': 'https://www.tefecite.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}