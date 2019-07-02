# -*- coding: utf-8 -*-
from odoo import http

# class Emiya(http.Controller):
#     @http.route('/emiya/emiya/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emiya/emiya/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emiya.listing', {
#             'root': '/emiya/emiya',
#             'objects': http.request.env['emiya.emiya'].search([]),
#         })

#     @http.route('/emiya/emiya/objects/<model("emiya.emiya"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emiya.object', {
#             'object': obj
#         })