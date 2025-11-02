from odoo import api, fields, models


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"

    apply_to_supplier = fields.Boolean(
        string="Apply to Supplier",
        help="When checked, indicates that this rule applies to a supplier",
    )
    supplier_id = fields.Many2one(
        "res.partner",
        string="Supplier",
        domain="[('supplier_rank', '>', 0)]",
        help="Select the supplier to whom this rule applies",
    )

    @api.onchange("apply_to_supplier")
    def _onchange_apply_to_supplier(self):
        if not self.apply_to_supplier and self.supplier_id:
            self.supplier_id = False

    def _is_applicable_for(self, product, qty_in_product_uom):
        res = super()._is_applicable_for(product, qty_in_product_uom)
        if (
            res
            and self.apply_to_supplier
            and self.supplier_id not in product.seller_ids.partner_id
        ):
            res = False

        return res
