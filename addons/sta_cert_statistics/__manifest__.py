# -*- coding: utf-8 -*-
{
    'name': "sta_cert_statistics",

    'summary': """
        STA发证信息统计""",

    'description': """
        STA发证信息统计
    """,

    'author': "Meng yingtian brooks",
    'website': "http://www.faceunity.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/certificate_info.xml',
        'views/certificate_platform.xml',
        'wizards/certificate_info_excel_export_wizard.xml',
        'views/sta_cert_statistics_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/certificate_info_export_excel_button.xml',
    ],
    'application': True,
    'auto_install': False,
}