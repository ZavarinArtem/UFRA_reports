# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class MrpBom(models.Model):

    _inherit = 'mrp.bom'

    weight = fields.Float(string='Weight', digits=(15, 3))
    for_print = fields.Boolean()

    def create(self, vals_list):
        a = 1
