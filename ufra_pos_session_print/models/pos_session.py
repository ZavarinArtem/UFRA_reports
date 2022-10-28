
from odoo import models, _


class PosSession(models.Model):

    _inherit = 'pos.session'

    def _print_session_docs(self):
        try:
            self.ensure_one()
        except ValueError:
            return None

        order_ids = self.order_ids
        codes = list(dict.fromkeys(order_ids.mapped('picking_type_code')))
        partners = order_ids.mapped('partner_id')
        if len(codes) > 1 or len(partners) > 1:
            return {
                'name': _('Print Options'),
                'view_mode': 'form',
                'res_model': 'pos.print.options.wizard',
                'view_id': self.env.ref('ufra_pos_session_print.pos_print_options_wizard_form').id,
                'type': 'ir.actions.act_window',
                'context': {
                    'session_id': self.id,
                },
                'target': 'new'
            }
        else:
            return self._get_print_all_docs_action()

    def get_print_all_docs_action(self, domain=None):
       
        if domain is None:
            orders = self.order_ids.ids
        else:
            domain = ['AND'] + domain + [('session_id', '=', self.id,)]
            orders = self.env['pos.order'].search(domain).ids

        data = {
            'orders': orders,
        }
        action = self.env.ref('ufra_pos_session_print.pos_session_print_all_docs_action').report_action(self, data=data)
        return action
