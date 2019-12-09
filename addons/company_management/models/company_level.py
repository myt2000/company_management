# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_level(models.Model):
    _name = 'company.level'

    name = fields.Char(string="Level Name")
    remark = fields.Char(string="Remark")
    level_company_info_ids = fields.One2many('company.info', 'company_level_id', string="Level")
