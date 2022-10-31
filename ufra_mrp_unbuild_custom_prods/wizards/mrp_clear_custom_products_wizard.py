
from odoo import models, fields


class MrpClearCustomProductsWizard(models.TransientModel):

    _name = 'mrp.clear.custom.products.wizard'

    unbuild_id = fields.Many2one('mrp.unbuild')

    def confirm(self):
        self.unbuild_id.fill_by_bom_finalize()
