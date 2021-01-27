# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Certificate_platform(models.Model):
    _name = "certificate.platform"

    name = fields.Char(string="Platform Name")
    remark = fields.Char(string="Remark")

