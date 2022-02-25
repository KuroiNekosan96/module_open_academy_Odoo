# -*- coding: utf-8 -*-
# from odoo import http


# class InfinityDp(http.Controller):
#     @http.route('/infinity_dp/infinity_dp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infinity_dp/infinity_dp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infinity_dp.listing', {
#             'root': '/infinity_dp/infinity_dp',
#             'objects': http.request.env['infinity_dp.infinity_dp'].search([]),
#         })

#     @http.route('/infinity_dp/infinity_dp/objects/<model("infinity_dp.infinity_dp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infinity_dp.object', {
#             'object': obj
#         })
