# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Company_extra(models.Model):
    _name = 'company.extra'

    name = fields.Char(string="Extra Name")
    remark = fields.Char(string="Remark")
