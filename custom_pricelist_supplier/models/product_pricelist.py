from odoo import models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    def _get_applicable_rules(self, products, date, **kwargs):
        """Put all the supplier based rules on the top to make sure that
        if that rule is applicable (considering the min qty and _is_applicable_for() method),
        it will be given priority over the other rules.


        """
        all_rules = super()._get_applicable_rules(products, date, **kwargs)
        return all_rules.sorted(lambda r: not r.apply_to_supplier)
