# -*- coding: utf-8 -*-
{
    'name': "group",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """""",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'course', 'student', 'teacher',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/group_views.xml',
        'views/group_action_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

