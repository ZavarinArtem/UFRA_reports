# -*- coding: utf-8 -*-
{
    'name': "Custom Products in MRP Unbuild for UFRA",

    'summary': """
        Custom Products in Unbuild for UFRA.""",

    'author': "SPOC",
    'website': "https://spoc-odoo.com.ua/",
    'company': 'SPOC corp',
    'maintainer': 'SPOC corp',

    'category': 'Manufacturing/Manufacturing',
    'version': '15.0.1.0.1',

    'depends': [
        'mrp',
        ],

    'data': [
        'security/ir.model.access.csv',
        'views/mrp_unbuild_views.xml',
        'wizards/mrp_clear_custom_products_wizard.xml',
    ],

    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'LGPL-3',
}
