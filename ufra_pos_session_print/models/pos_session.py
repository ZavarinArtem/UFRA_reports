
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

            wizard = self.env['pos.print.options.wizard'].create({
                'session_id': self.id,
            })
            return {
                'name': _("Print Options"),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'pos.print.options.wizard',
                'res_id': wizard.id,
                'target': 'new',
                'context': {**self.env.context, 'active_ids': self.ids, 'active_model': 'pos.session'},
            }
        else:
            return self.get_print_all_docs_action()

    def get_print_all_docs_action(self, domain=None):
       
        if domain is None:
            order_ids = self.order_ids
        else:
            domain = ['&'] + domain + [('session_id', '=', self.id,)]
            order_ids = self.env['pos.order'].search(domain)
        orders = order_ids.ids
        products_dict = {}

        for order_id in order_ids:
            for line in order_id.lines:
                product = (line.full_product_name, line.product_uom_id)
                qty = products_dict.get(product, 0)
                products_dict[product] = qty + line.qty

        products = []
        for key in products_dict:
            products.append({
                'full_product_name': key[0],
                'product_uom_id': key[1].id,
                'qty': products_dict[key],
            })

        if len(orders):

            data = {
                'session_id': self.id,
                'orders': orders,
                'picking_type_code': order_ids[0].picking_type_code,
                'products': products,
            }
            action = self.env.ref('ufra_pos_session_print.pos_session_print_all_docs_action').report_action(self, data=data)
            return action
        else:
            return None
