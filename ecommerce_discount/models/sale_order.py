from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def create(self, vals):
        """
            Update the unit price with the discounted price when the product is added to the cart.
        """
        if vals.get('product_id'):
            product_id = self.env['product.product'].search([('id', '=', vals.get('product_id'))])
            if product_id and product_id.product_tmpl_id:
                if product_id.product_tmpl_id.discount_percentage > 0:
                    vals['price_unit'] = product_id.product_tmpl_id.discounted_price
        res = super(SaleOrderLine, self).create(vals)
        return res

    @api.model
    def write(self, vals):
        """
            Update the unit price with the discounted price when the product is added to the cart.
        """
        if vals.get('price_unit') and self.product_id:
            if self.product_id and self.product_id.product_tmpl_id:
                if self.product_id.product_tmpl_id.discount_percentage > 0:
                    vals['price_unit'] = self.product_id.product_tmpl_id.discounted_price
        res = super(SaleOrderLine, self).write(vals)
        return res
