# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_platform(models.Model):
    _name = "company.platform"

    name = fields.Char(string="Platform Name")
    remark = fields.Char(string="Remark")

