# -*- coding: utf-8 -*-
{
    'name': "Print Wizard for PoS Session for UFRA",

    'summary': """
        Wizard for printing all orders in session for UFRA.""",

    'author': "SPOC",
    'website': "https://spoc-odoo.com.ua/",
    'company': 'SPOC corp',
    'maintainer': 'SPOC corp',

    'category': 'Sales/Point of Sale',
    'version': '15.0.1.0.1',

    'depends': [
        'point_of_sale',
        'cha_stock',
        ],

    'data': [
        'security/ir.model.access.csv',
        'data/pos_session_actions.xml',
        'data/pos_session_templates.xml',
        'wizards/pos_print_options_wizard.xml',
    ],

    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'LGPL-3',
}
