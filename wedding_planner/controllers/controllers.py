# -*- coding: utf-8 -*-
from odoo import http

# class WeddingPlanner(http.Controller):
#     @http.route('/wedding_planner/wedding_planner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wedding_planner/wedding_planner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wedding_planner.listing', {
#             'root': '/wedding_planner/wedding_planner',
#             'objects': http.request.env['wedding_planner.wedding_planner'].search([]),
#         })

#     @http.route('/wedding_planner/wedding_planner/objects/<model("wedding_planner.wedding_planner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wedding_planner.object', {
#             'object': obj
#         })