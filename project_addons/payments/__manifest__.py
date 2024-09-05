# -*- coding: utf-8 -*-
{
    'name': "payment_all",
    'summary': "Accept payments",
    'description': "Accept payments",
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/payment_views.xml',
        'views/payment_action_menu.xml',
        'views/templates.xml',
    ],
}
