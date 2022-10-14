from odoo import models
from babel.dates import format_date


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_name_for_printing(self):
        name_parts = self.name.split('/')
        return format_date(getattr(self, 'scheduled_date'), 'dd MMMM YYYY', locale='uk_UA') \
               + '/' + name_parts[len(name_parts) - 1]

    def _get_driver_passport(self, driver_id):
        return driver_id.id_numbers.search([('partner_id', '=', driver_id.id), ('category_id.name', '=', 'passport'), ('status', '=', 'open')])


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_name_for_printing(self):
        return format_date(getattr(self, 'date_order'), 'dd MMMM YYYY', locale='uk_UA') + self.name

    def _get_driver_passport(self, driver_id):
        return driver_id.id_numbers.search([('partner_id', '=', driver_id.id), ('category_id.name', '=', 'passport'), ('status', '=', 'open')])


class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _get_name_for_printing(self):
        name_parts = self.name.split('/')
        return format_date(getattr(self, 'date_order'), 'dd MMMM YYYY', locale='uk_UA') \
               + '/' + name_parts[len(name_parts) - 1]

    def _get_driver_passport(self, driver_id):
        return driver_id.id_numbers.search([('partner_id', '=', driver_id.id), ('category_id.name', '=', 'passport'), ('status', '=', 'open')])
