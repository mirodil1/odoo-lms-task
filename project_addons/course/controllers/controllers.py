# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectAddons/course(http.Controller):
#     @http.route('/project_addons/course/project_addons/course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_addons/course/project_addons/course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_addons/course.listing', {
#             'root': '/project_addons/course/project_addons/course',
#             'objects': http.request.env['project_addons/course.project_addons/course'].search([]),
#         })

#     @http.route('/project_addons/course/project_addons/course/objects/<model("project_addons/course.project_addons/course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_addons/course.object', {
#             'object': obj
#         })

