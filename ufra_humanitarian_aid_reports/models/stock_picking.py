from odoo import models
from babel.dates import format_date


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def get_ua_date(self, date_field, date_format):
        return format_date(getattr(self, date_field), date_format, locale='uk_UA')
