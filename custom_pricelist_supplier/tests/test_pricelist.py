from odoo.tests.common import TransactionCase
from odoo.tools.float_utils import float_compare


class TestCustomPricelistSupplier(TransactionCase):
    def setUp(self):
        super().setUp()
        env = self.env

        # Products
        self.product_a = env.ref("custom_pricelist_supplier.product_product_a")
        self.product_b = env.ref("custom_pricelist_supplier.product_product_b")
        self.product_c = env.ref("custom_pricelist_supplier.product_product_c")
        self.product_product_d1 = env.ref(
            "custom_pricelist_supplier.product_product_d1"
        )
        self.product_product_d2 = env.ref(
            "custom_pricelist_supplier.product_product_d2"
        )
        self.product_product_e = env.ref("custom_pricelist_supplier.product_product_e")

        # Pricelist
        self.pricelist = env.ref("custom_pricelist_supplier.pricelist_customer_a")

    def match_product_price(self, product, expected_price):
        price = self.pricelist._get_product_price(product, quantity=1.0)
        msg = "Wrong sale price: %s. should be %s instead of %s" % (
            product.name,
            expected_price,
            price,
        )
        self.assertEqual(
            float_compare(price, expected_price, precision_digits=2), 0, msg
        )

    def test_selection_of_product_pricelist_rule(self):
        context = {}
        context.update({"pricelist": self.pricelist.id, "quantity": 1})

        # Product A
        product = self.product_a
        self.match_product_price(product, 500)

        # Product B
        product = self.product_b
        self.match_product_price(product, 520)

        # Product C
        product = self.product_c
        self.match_product_price(product, 600)

        # Product D1
        product = self.product_product_d1
        self.match_product_price(product, 510)

        # Product D2
        product = self.product_product_d2
        self.match_product_price(product, 510)

        # Product E
        product = self.product_product_e
        self.match_product_price(product, 530)
