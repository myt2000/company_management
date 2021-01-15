# -*- coding: utf-8 -*-
from odoo import http

# class StaCertStatistics(http.Controller):
#     @http.route('/sta_cert_statistics/sta_cert_statistics/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sta_cert_statistics/sta_cert_statistics/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sta_cert_statistics.listing', {
#             'root': '/sta_cert_statistics/sta_cert_statistics',
#             'objects': http.request.env['sta_cert_statistics.sta_cert_statistics'].search([]),
#         })

#     @http.route('/sta_cert_statistics/sta_cert_statistics/objects/<model("sta_cert_statistics.sta_cert_statistics"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sta_cert_statistics.object', {
#             'object': obj
#         })