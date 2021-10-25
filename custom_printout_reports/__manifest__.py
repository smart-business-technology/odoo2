# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
{
    'name': "Invoice Report",

    'summary': """Invoice Report Custom""",

    'description': """ """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Accountingt',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/account_invoice.xml',
        'reports/account_quotation.xml',
        'views/reports_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
}
