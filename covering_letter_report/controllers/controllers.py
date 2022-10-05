# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo15/pjts/work/spoc-odoo/ufraReports/coveringLetterReport(http.Controller):
#     @http.route('//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report.listing', {
#             'root': '//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report',
#             'objects': http.request.env['/opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report./opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report'].search([]),
#         })

#     @http.route('//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report//opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report/objects/<model("/opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report./opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report.object', {
#             'object': obj
#         })
