import xlwt
import StringIO
import base64

from odoo import  models, fields, api
from odoo.exceptions import ValidationError, AccessError, UserError

class Company_excel_export(models.TransientModel):
    _name = 'company.excel.export.wizard'

    def _get_default_support_specialist(self):
        return self.env['res.users'].search([('id', '=', self.env.uid)])

    access_date = fields.Date(string="Access Search Time", default=fields.Date.context_today)
    formal_access_date = fields.Date(string="Formal Access Search Date", default=fields.Date.context_today)
    support_specialist_id = fields.Many2many('res.users', 'info_res_users_wizard_rel', string="Support Specialist Choose",
                                             default=_get_default_support_specialist)

    @api.multi
    def export_excel_data(self):
        pass