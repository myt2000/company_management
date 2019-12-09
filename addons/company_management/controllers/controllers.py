# -*- coding: utf-8 -*-
from odoo import http

# class CompanyManagement(http.Controller):
#     @http.route('/company_management/company_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_management/company_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_management.listing', {
#             'root': '/company_management/company_management',
#             'objects': http.request.env['company_management.company_management'].search([]),
#         })

#     @http.route('/company_management/company_management/objects/<model("company_management.company_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_management.object', {
#             'object': obj
#         })