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

    @api.model
    def _order_fields(self, ui_order):
        order_fields = super()._order_fields(ui_order)

        order_fields['number_of_adults'] = ui_order.get('number_of_adults')
        order_fields['number_of_children'] = ui_order.get('number_of_children')

        return order_fields

    def _export_for_ui(self, order):
        order = order.sudo()
        result = super()._export_for_ui(order)

        result.update({
            'number_of_adults': order.number_of_adults,
            'number_of_children': order.number_of_children,
        })

        return result
