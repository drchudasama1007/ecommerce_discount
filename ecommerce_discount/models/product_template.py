from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # New Field discount_percentage in Product
    discount_percentage = fields.Float(
        string="Discount Percentage",
        default=0.0,
        help="Enter the discount percentage for this product (0-100%)."
    )
    discounted_price = fields.Float(
        string="Discounted Price",
        compute="_compute_discounted_price",
        store=True,
        readonly=True,
        help="The price after applying the discount."
    )

    @api.depends("list_price", "discount_percentage")
    def _compute_discounted_price(self):
        """
            The discount should be applied to the product’s original price to calculate
            the discounted price.
        """
        for product in self:
            if product.discount_percentage > 0:
                product.discounted_price = product.list_price * (1 - (product.discount_percentage / 100))
            else:
                product.discounted_price = product.list_price
