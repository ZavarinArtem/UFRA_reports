
from odoo import models, fields, api


class PosPrintOptionsWizard(models.TransientModel):

    _name = 'pos.print.options.wizard'
    _description = 'Options for Printing All Orders from PoS Session'

    session_id = fields.Many2one('pos.session')

    selected_code = fields.Selection(selection='get_codes')
    code_set = fields.Boolean('Code set', default=False)

    session_partners_ids = fields.Many2many('res.partner')
    selected_partner = fields.Many2one('res.partner')
    partner_set = fields.Boolean('Partner Set', default=False)

    def get_codes(self):
        codes = []
        code_field = self.env['ir.model.fields'].search([
            ('model_id.model', '=', 'stock.picking.type'),
            ('name', '=', 'code')
        ])
        for selection_id in code_field.selection_ids:
            codes.append((selection_id.value, selection_id.name))
        return codes

    #
    # def get_partners_len(self):
    #     self.get_partners()
    #     return len(self.partners)

    @api.model_create_single
    def create(self, vals):
        if vals.get('session_id'):

            session_id = self.env['pos.session'].browse(vals['session_id'])
            session_partners_ids = session_id.order_ids.mapped('partner_id')
            if len(session_partners_ids) == 1:
                vals['selected_partner'] = session_partners_ids[0].id
                vals['partner_set'] = True

            vals['session_partners_ids'] = [(6, 0, session_partners_ids.ids)]

            session_codes = list(dict.fromkeys(session_id.order_ids.mapped('picking_type_code')))
            if len(session_codes) == 1:
                vals['selected_code'] = session_codes[0]
                vals['code_set'] = True
        return super(PosPrintOptionsWizard, self).create(vals)

    def action_done(self):
        if self.selected_code and self.selected_partner:
            domain = [
                ('picking_type_code', '=', self.selected_code),
                ('partner_id', '=', self.selected_partner.id),
            ]
            return self.session_id.get_print_all_docs_action(domain)
        else:
            return None
