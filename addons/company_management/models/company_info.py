# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_info(models.Model):
    _name = 'company.info'
    _rec_name = 'company_name'

    def _get_default_support_specialist(self):
        return self.env['res.users'].search([('id', '=', self.env.uid)])

    def _get_default_product(self):
        return self.env['company.product'].search([('name', '=', 'NAMA')])

    company_name = fields.Char(string="Company Name")
    company_abbreviation = fields.Char(string="Abbreviation")
    product_name = fields.Char(string="Product Name")
    status = fields.Selection([('formal', 'Formal'), ('test', 'Test'),
                               ('abort', 'Abort')],
                              string="Status",
                              default='test')
    access_date = fields.Date(string="Access Time", default=fields.Date.context_today)
    formal_access_date = fields.Date(string="Formal Access Date")
    mail = fields.Char(string="Mail")
    version_id = fields.Many2one('company.version', string="version")
    certificate_name = fields.Char(string="Certificate Name")
    common_name = fields.Char(string="Common name")
    package_name_id = fields.Many2many('company.package', 'info_company_package_info_rel', string="Package")
    extra_function_id = fields.Many2many('company.extra', 'info_company_extra_info_rel', string="Extra Function")
    company_level_id = fields.Many2one('company.level', string="Company Level")
    saler_id = fields.Many2one('company.salers', string="Saler")
    platform = fields.Many2many('company.platform', 'info_platform_rel', string="Platform")
    product = fields.Many2many('company.product', 'info_product_rel', string="Use Product", default=_get_default_product)
    support_specialist_id = fields.Many2many('res.users', 'info_res_users_rel', string="Support Specialist", default=_get_default_support_specialist)
    contact_info = fields.Many2many('company.contact.info', 'info_contact_info_rel', string="Contact Info")
    remark = fields.Text(string="Remark")
    effective_time = fields.Char(string="Effective Time")
    demo_address = fields.Char(string="Demo Address")
    third_party = fields.Many2many('company.third.party', 'info_third_party_info', string="Third Party")


    # @api.multi
    # def company_info_export_button_form(self):
    #     view_name = 'company_excel_export_wizard_form_view'
    #     view = self.env['ir.model.data'].search([('name', '=', view_name)])
    #     view_id = view.res_id
    #     return {
    #     'name': 'Search Company Info',
    #     'type': 'ir.actions.act_window',
    #     'view_type': 'form',
    #     'view_mode': 'form',
    #     'view_id': view_id,
    #     'target': 'new',
    #     'res_model': 'base.gather.zone',
    #     'res_id': self.id,
    #     }

