from odoo import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"

    signatory = fields.Many2one(
        comodel_name="res.partner",
        string="Signatory"
    )
    is_military = fields.Boolean(string='Is Military')
