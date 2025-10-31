from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def custom_method(self):
        return "Simple custom Method says - Hello"
