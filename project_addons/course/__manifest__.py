# -*- coding: utf-8 -*-
{
    'name': "course",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """""",
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/course_action_menu.xml',
        'views/templates.xml',
    ],
}

