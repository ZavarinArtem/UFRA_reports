# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    picking_type_code = fields.Selection([('incoming', 'Receipt'), ('outgoing', 'Delivery'), ('internal', 'Internal Transfer')], 'Type of Operation')
    driver_id = fields.Many2one(comodel_name='res.partner',
                                string="Driver")
    driver_secondary_id = fields.Many2one(comodel_name='res.partner',
                                          string="Secondary Driver")
    number_of_adults = fields.Integer(string="Number of Adults")
    number_of_children = fields.Integer(string="Number of Children")

    def _select_sale(self, fields=None):
        res = super(SaleReport, self)._select_sale(fields)
        return """
        %s 
        , NULL as picking_type_code
        , 0 as number_of_adults
        , 0 as number_of_children
        , s.driver_id as driver_id
        , s.driver_secondary_id as driver_secondary_id
        """ % res

    def _group_by_sale(self, groupby=''):
        res = super(SaleReport, self)._group_by_sale(groupby)
        return """
        %s
        , s.driver_id
        , s.driver_secondary_id
        """ % res

    def _select_pos(self, fields=None):
        res = super(SaleReport, self)._select_pos(fields)
        return """
        %s 
        , pos.picking_type_code as picking_type_code
        , pos.number_of_adults as number_of_adults
        , pos.number_of_children as number_of_children
        , pos.driver_id as driver_id
        , pos.driver_secondary_id as driver_secondary_id
        """ % res

    def _group_by_pos(self):
        res = super(SaleReport, self)._group_by_pos()
        return """
        %s
        , pos.picking_type_code
        , pos.number_of_adults
        , pos.number_of_children
        , pos.driver_id
        , pos.driver_secondary_id        
        """ % res
