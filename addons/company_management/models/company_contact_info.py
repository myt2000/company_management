# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company_contact_info(models.Model):
    _name = "company.contact.info"

    name = fields.Char(string="Contact Name")
    contact_type = fields.Selection([('qq', 'QQ'), ('wx', 'WX'),
                               ('dd', 'Dingding')],
                              string="Contact Type",
                              default='wx')