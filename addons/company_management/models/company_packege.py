# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Company_package(models.Model):
    _name = 'company.package'

    name = fields.Char(string="Package Name")
    remark = fields.Char(string="Remark")
