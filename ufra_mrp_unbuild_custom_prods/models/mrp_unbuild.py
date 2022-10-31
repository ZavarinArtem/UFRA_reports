from odoo import api, fields, models, _


class MrpUnbuild(models.Model):
    _inherit = "mrp.unbuild"

    custom_product_line_ids = fields.One2many('mrp.unbuild.custom.product.line', 'unbuild_id', auto_join=True)

    def unlink(self):
        for unbuild in self.filtered(lambda s: s.custom_product_line_ids):
            unbuild.custom_product_line_ids.unlink()
        return super(MrpUnbuild, self).unlink()

    def fill_by_bom(self):
        self.ensure_one()
        if self.custom_product_line_ids:
            wizard = self.env['mrp.clear.custom.products.wizard'].create({
                'unbuild_id': self.id,
            })
            return {
                'name': _("Clear custom products"),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'mrp.clear.custom.products.wizard',
                'res_id': wizard.id,
                'target': 'new',
                'context': {**self.env.context, 'active_ids': self.ids, },
            }
        else:
            self.fill_by_bom_finalize()

    def fill_by_bom_finalize(self):
        if self.custom_product_line_ids:
            self.custom_product_line_ids.unlink()

        if self.bom_id:
            vals = []
            for bom_line in self.bom_id.bom_line_ids:
                vals.append({
                    'unbuild_id': self.id,
                    'product_id': bom_line.product_id.id,
                    'product_uom_id': bom_line.product_uom_id.id,
                    'product_qty': bom_line.product_qty,
                    'bom_line_id': bom_line.id,
                })
            custom_product_line_ids = self.env['mrp.unbuild.custom.product.line'].sudo().create(vals)
            self.custom_product_line_ids = [(6, 0, custom_product_line_ids.ids)]

    def _generate_produce_moves(self):
        moves = self.env['stock.move']
        for unbuild in self:
            if unbuild.custom_product_line_ids:
                for line in unbuild.custom_product_line_ids:
                    moves += unbuild._generate_move_from_bom_line(line.product_id, line.product_uom_id, line.product_qty,
                                                              bom_line_id=line.bom_line_id.id or 1)
            else:
                moves += super()._generate_produce_moves()

        return moves


class MrpUnbuildCustomProductLine(models.Model):

    _name = 'mrp.unbuild.custom.product.line'

    unbuild_id = fields.Many2one('mrp.unbuild', 'Unbuild Order', required=True, index=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True, required=True, index=True,
                                 default=lambda s: s.env.company, )

    product_id = fields.Many2one('product.product', 'Product', ondelete="cascade", check_company=True,
                                 domain="[('type', '!=', 'service'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    product_uom_id = fields.Many2one('uom.uom', 'Unit of Measure', required=True,
                                     domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')
    product_qty = fields.Float('Quantity', digits=(16, 3))
    bom_line_id = fields.Many2one('mrp.bom.line', 'BoM Line', check_company=True)

    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('unbuild_id'):
                vals['company_id'] = self.env['mrp.unbuild'].browse(vals['unbuild_id']).company_id.id

        return super().create(vals_list)

    @api.onchange('product_id', 'product_uom_id')
    def _onchange_product_id(self):
        if self.product_id:
            if not self.product_uom_id or self.product_uom_id.category_id != self.product_id.uom_id.category_id:
                self.product_uom_id = self.product_id.uom_id.id
