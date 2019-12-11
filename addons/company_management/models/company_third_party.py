# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_third_party(models.Model):
    _name = "company.third.party"

    name = fields.Char(string="Third Party")
    remark = fields.Char(string="Remark")