# -*- coding: utf-8 -*-
{
    'name': "company_management",

    'summary': """
        相芯客户管理系统""",

    'description': """
        相芯客户管理系统
    """,

    'author': "Yingtian Meng",
    'website': "http://www.faceunity.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/company_contact_info.xml',
        'views/company_third_party.xml',
        'views/company_info.xml',
        'views/company_level.xml',
        'views/company_platform.xml',
        'views/company_product.xml',
        'views/company_salers.xml',
        'views/company_package.xml',
        'views/company_extra.xml',
        'views/company_version.xml',
        'views/company_menu.xml',
        'views/login_web.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}