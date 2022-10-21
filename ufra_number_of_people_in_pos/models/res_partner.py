from odoo import models, fields


class ResPartner(models.Model):

    _inherit = "res.partner"

    number_of_adults = fields.Integer(string="Number of Adults", default=1)
    number_of_children = fields.Integer(string="Number of Children", default=0)
