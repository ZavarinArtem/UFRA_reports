# -*- coding: utf-8 -*-
{
    'name': "Numbers of people receiving aid for UFRA",

    'summary': """
        Numbers of people receiving aid for UFRA.""",

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
        'views/res_partner_views.xml',
        'views/pos_order_view.xml',
    ],

    'assets': {
        'point_of_sale.assets': [
            'ufra_number_of_people_in_pos/static/src/js/models.js',
            'ufra_number_of_people_in_pos/static/src/js/Screens/PaymentScreen/PaymentScreen.js',
        ],
        'web.assets_qweb': [
            'ufra_number_of_people_in_pos/static/src/xml/**/*',
        ],
    },

    'demo': [],
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'LGPL-3',
}
