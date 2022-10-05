# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class /opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report(models.Model):
#     _name = '/opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report./opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report'
#     _description = '/opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report./opt/odoo15/pjts/work/spoc-odoo/ufra_reports/covering_letter_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
