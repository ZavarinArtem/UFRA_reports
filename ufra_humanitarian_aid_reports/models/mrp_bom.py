# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class MrpBom(models.Model):

    _inherit = 'mrp.bom'

    weight = fields.Float(string='Weight', digits=(15, 3))
    for_print = fields.Boolean()

    @api.model_create_multi
    def create(self, vals_list):
        return super(MrpBom, self).create(vals_list)
