
from odoo import models, fields, api


class PosPrintOptionsWizard(models.TransientModel):

    _name = 'pos.print.options.wizard'
    _description = 'Options for Printing All Orders from PoS Session'

    @api.model
    def default_get(self, fields_list):
        result = super().default_get(fields_list)
        result['session_id'] = self._context.get('session_id', None)

    def get_codes(self):
        order_ids = self.session_id.order_ids
        return list(dict.fromkeys(order_ids.mapped('picking_type_code')))

    def get_partners(self):
        return self.session_id.order_ids.mapped('partner_id')

    def get_codes_len(self):
        return len(self.codes)

    def partners_len(self):
        return len(self.partners)

    session_id = fields.Many2one('pos.session')

    codes = fields.Selection(selection='get_codes')
    codes_len = fields.Integer(compute='get_codes_len')
    partners = fields.Many2many('res.partner')
    partners_len = fields.Integer(compute='get_partners_len')

    selected_code = fields.Selection(selection=get_codes)
    selected_partner = fields.Many2one('res.partner')

    def confirm(self):
        if self.selected_code and self.selected_partner:
            domain = [
                ('session_id', '=', self.session_id),
                ('picking_type_code', '=', self.selected_code),
                ('partner_id', '=', self.selected_partner),
            ]
            data = {
                'orders': self.env['pos.order'].search(domain),
            }
            action = self.env.ref('ufra_pos_session_print.pos_session_print_all_docs_action').report_action(self,
                                                                                                            data=data)
            return action
        else:
            return None


