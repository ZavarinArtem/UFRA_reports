# -*- coding: utf-8 -*-
{
    'name': "Humanitarian Aid Reports for UFRA",

    'summary': """
        Humanitarian Aid Reports for UFRA: Covering Letter and Act of Acceptance.""",

    'author': "SPOC",
    'website': "https://spoc-odoo.com.ua/",
    'company': 'SPOC corp',
    'maintainer': 'SPOC corp',

    'category': 'Inventory',
    'version': '15.0.1.0.1',

    'depends': [
        'point_of_sale',
        'purchase',
        'sale',
        'stock',
        'cha_stock',
        'partner_contact_birthdate',
        'partner_identification', ],

    'data': [
        'views/report_covering_letter.xml',
        'views/report_act_of_acceptance.xml',
        'views/res_partner_view.xml',
        'views/mrp_bom_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
