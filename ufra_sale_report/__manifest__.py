# -*- coding: utf-8 -*-
{
    'name': "Sales Report for UFRA",

    'summary': """
        Sales Report for UFRA.""",

    'author': "SPOC",
    'website': "https://spoc-odoo.com.ua/",
    'company': 'SPOC corp',
    'maintainer': 'SPOC corp',

    'category': 'Sales/Sales',
    'version': '15.0.1.0.1',

    'depends': [
        'sale',
        'pos_sale',
        'cha_stock',
        'ufra_number_of_people_in_pos',
        ],

    'data': [
    ],

    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'LGPL-3',
}
