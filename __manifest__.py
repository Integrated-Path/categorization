# -*- coding: utf-8 -*-
{
    'name': "Categorization",

    'summary': """Creating partner fields (ex: customers, vendors) that can be used to filter accross several modules""",

    'author': "Integerated Path",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale', 'stock', 'product', 'purchase', 'account', 'sales_customisations'],

    # always loaded
    'data': [
        # 'views/categorization_views.xml',
    ],
}
