from odoo import models, fields, api


class PosOrder(models.Model):

    _inherit = "pos.order"

    number_of_adults = fields.Integer(string="Number of Adults")
    number_of_children = fields.Integer(string="Number of Children")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        super()._onchange_partner_id()

        if self.partner_id \
                and not self.partner_id.is_company \
                and self.picking_type_code == 'outgoing':
            self.number_of_adults = self.partner_id.number_of_adults
            self.number_of_children = self.partner_id.number_of_children
