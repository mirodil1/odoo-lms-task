# -*- coding: utf-8 -*-
{
    'name': "student",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': "",
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/student_action_menu.xml',
        'views/templates.xml',
    ],
}