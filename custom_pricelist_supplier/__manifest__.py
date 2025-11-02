{
    "name": "custom_pricelist_supplier",
    "summary": "Supplier based price lists for each customer",
    "description": """
    Extends pricelist functionality to support supplier-based pricing rules.
    Allows users to define and apply prices based on the Supplier, in addition to existing criteria
    like product, template or category.
    """,
    "author": "Hariom Pandya",
    "website": "https://www.example.com/",
    "category": "Sales/Sales",
    "version": "1.0",
    "depends": ["purchase", "sale_management"],
    "data": ["views/product_pricelist_item_views.xml"],
    "post_init_hook": "_post_init_hook",
    "demo": [
        "data/res_partner_demo.xml",
        "data/product_demo.xml",
        "data/pricelist_data.xml",
        "data/product_supplierinfo_demo.xml",
    ],
    "license": "LGPL-3",
}
