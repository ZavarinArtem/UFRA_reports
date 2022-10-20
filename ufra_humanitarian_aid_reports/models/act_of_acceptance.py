from odoo import models
from babel.dates import format_date


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def get_ua_date(self, date_field, date_format):
        return format_date(getattr(self, date_field), date_format, locale='uk_UA')

    def _get_company_signatory(self):
        if self.company_id.partner_id.signatory.comment:
            return str(self.company_id.partner_id.signatory.comment).replace('<p>', '').replace('</p>', '').replace('<br>', '')
        else:
            return (self.company_id.partner_id.signatory.function or '') + ' ' \
                   + (self.company_id.partner_id.signatory.name or '')

    def _get_product_bom(self, product_id, tmpl_search=False):
        if not product_id:
            return None

        if tmpl_search:
            search_line = 'product_tmpl_id'
        else:
            search_line = 'product_id'

        bom = self.env['mrp.bom'].search([(search_line, '=', product_id.id), ('for_print', '=', True)]).sorted(key='create_date', reverse=True)
        if bom:
            return bom[0]
        else:
            bom = self.env['mrp.bom'].search(
                [(search_line, '=', product_id.id)]).sorted(key='create_date')
            if bom:
                return bom[0]
            elif not tmpl_search:
                return self._get_product_bom(product_id.product_tmpl_id, True)
            else:
                return None

    def _form_contact_signature(self, contact):

        name = str(contact.signatory.name or '')
        name_parts = name.split(' ')
        if len(name_parts) == 3:
            name = name_parts[0] + " " + name_parts[1][0] + ". " + name_parts[2][0] + "."

        return (contact.signatory.function or '') + "_____________" + name


class PosOrder(models.Model):
    _inherit = 'pos.order'

    def get_ua_date(self, date_field, date_format):
        return format_date(getattr(self, date_field), date_format, locale='uk_UA')

    def _get_company_signatory(self):
        if self.company_id.partner_id.signatory.comment:
            return str(self.company_id.partner_id.signatory.comment).replace('<p>', '').replace('</p>', '').replace('<br>', '')
        else:
            return (self.company_id.partner_id.signatory.function or '') + ' ' \
                   + (self.company_id.partner_id.signatory.name or '')

    def _get_product_bom(self, product_id, tmpl_search=False):
        if not product_id:
            return None

        if tmpl_search:
            search_line = 'product_tmpl_id'
        else:
            search_line = 'product_id'

        bom = self.env['mrp.bom'].search([(search_line, '=', product_id.id), ('for_print', '=', True)]).sorted(key='create_date', reverse=True)
        if bom:
            return bom[0]
        else:
            bom = self.env['mrp.bom'].search(
                [(search_line, '=', product_id.id)]).sorted(key='create_date')
            if bom:
                return bom[0]
            elif not tmpl_search:
                return self._get_product_bom(product_id.product_tmpl_id, True)
            else:
                return None

    def _form_contact_signature(self, contact):

        name = str(contact.signatory.name or '')
        name_parts = name.split(' ')
        if len(name_parts) == 3:
            name = name_parts[0] + " " + name_parts[1][0] + ". " + name_parts[2][0] + "."

        return (contact.signatory.function or '') + "_____________" + name
