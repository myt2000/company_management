# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class certificate_info(models.Model):
#     _name = 'sta_cert_statistics.sta_cert_statistics'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

'''
发证日期
公司名称
功能
平台
证书状态
发证时长

'''

class Certificate_info(models.Model):
    _name = 'certificate.info'
    _rec_name = 'company_name'
    _order = 'date desc'

    def _get_default_support_specialist(self):
        return self.env['res.users'].search([('id', '=', self.env.uid)])

    company_name = fields.Char(string="Company Name")
    date = fields.Date(string="Certificate Issuance Time", default=fields.Date.context_today)
    function = fields.Selection([('interactive', 'Interactive assistant'), ('push', 'Push streaming service')],
                                string="Function",
                                default='interactive')
    platform = fields.Many2many('certificate.platform', 'certificate_info_platform_rel', string="Platform")
    status = fields.Selection([('formal', 'Formal'), ('test', 'Test'),],
                              string="Status",
                              default='test')
    days = fields.Integer(string="Days")
    support_specialist_id = fields.Many2many('res.users', 'certificate_info_res_users_rel', string="Support Specialist", default=_get_default_support_specialist)
    remark = fields.Text(string="Remark")