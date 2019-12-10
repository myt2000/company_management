# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_info(models.Model):
    _name = 'company.info'
    _rec_name = 'company_name'

    company_name = fields.Char(string="Company Name", required=True)
    company_abbreviation = fields.Char(string="Abbreviation", required=True)
    product_name = fields.Char(string="Product Name")
    status = fields.Selection([('formal', 'Formal'), ('test', 'Test'),
                               ('abort', 'Abort')],
                              string="Status",
                              default='test')
    access_date = fields.Date(string="Access Time", default=fields.Date.context_today)
    formal_access_date = fields.Date(string="Formal Access Date")
    mail = fields.Char(string="Mail")
    version = fields.Char(string="Version")
    certificate_name = fields.Char(string="Certificate Name")
    common_name = fields.Char(string="Common name")
    package_name_id = fields.Many2many('company_package', 'info_company_package_rel', string="Package")
    extra_function_id = fields.Many2many('company_extra', 'info_company_extra_rel', string="Extra Function")
    company_level_id = fields.Many2one('company.level', string="Company Level")
    saler_id = fields.Many2one('company.salers', string="Saler")
    platform = fields.Many2many('company.platform', 'info_platform_rel', string="Platform", required=True)
    product = fields.Many2many('company.product', 'info_product_rel', string="Use Product")
    support_specialist_id = fields.Many2many('res.users', 'info_res_users_rel', string="Support Specialist")
    contact_info = fields.Many2many('company.contact.info', 'info_contact_info_rel', string="Contact Info")
    remark = fields.Text(string="Remark")
