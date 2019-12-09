# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_product(models.Model):
    _name = 'company.product'

    name = fields.Char(string="Product Name")
    remark = fields.Char(string="Remark")
    
