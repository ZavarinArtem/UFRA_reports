from odoo import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"

    number_of_adults = fields.Integer("Number of Adults")
    number_of_children = fields.Integer("Number of Children")
