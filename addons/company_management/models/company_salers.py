# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_salers(models.Model):
    _name = "company.salers"

    name = fields.Char(string="Saler Name")
    mail = fields.Char(string="Mail")
    department = fields.Char(string="Department")
    remark = fields.Char(string="Remark")
    salers_company_info_ids = fields.One2many('company.info', 'saler_id', string="Company Info")
