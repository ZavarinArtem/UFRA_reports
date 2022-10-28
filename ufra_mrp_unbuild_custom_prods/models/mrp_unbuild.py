from odoo import api, fields, models


class MrpUnbuild(models.Model):
    _inherit = "mrp.unbuild"

    custom_product_line_ids = fields.One2many('mrp.unbuild.custom.product.line', 'unbuild_id', auto_join=True)

    def fill_by_bom(self):
        for rec in self:
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

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('unbuild_id'):
                vals['company_id'] = self.env['mrp.unbuild'].browse(vals['unbuild_id']).company_id.id

        return super().create(vals)

    @api.onchange('product_id', 'product_uom_id')
    def _onchange_product_id(self):
        if self.product_id:
            if not self.product_uom_id or self.product_uom_id.category_id != self.product_id.uom_id.category_id:
                self.product_uom_id = self.product_id.uom_id.id
