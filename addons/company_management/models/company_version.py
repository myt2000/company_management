# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_version(models.Model):
    _name = "company.version"

    name = fields.Char(string="Version")
    remark = fields.Char(string="Remark")
    version_company_info_ids = fields.One2many('company.info', 'version_id', string="Company Info")