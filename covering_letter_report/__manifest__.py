# -*- coding: utf-8 -*-
{
    'name': "Covering Letter Report",

    'summary': """
        UFRA Covering letter for stock transfer.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "SPOC",
    'website': "https://spoc-odoo.com.ua/",
    'company': 'SPOC corp',
    'maintainer': 'SPOC corp',

    'category': 'Inventory/Inventory',
    'version': '15.0.1.0.1',

    'depends': ['stock'],

    'data': [
        'views/report_covering_letter.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
