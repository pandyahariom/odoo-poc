Custom Pricelist Supplier
=========================

This module extends the functionality of the sale pricelist to support supplier-based pricing rules.
Allows users to define and apply prices based on the Supplier, in addition to existing criteria
like product, template or category.

Odoo Version
------------
This module is designed and is compatible with Odoo 19.0.


How to use
----------
1. Once the module is installed, navigate to the Pricelists menu under Sales.
2. Create or edit a pricelist.
3. For each price list item, the new "Apply to Supplier" checkbox is available in the form view.
4. Selecting this checkbox make "Supplier" field visible in the form view.
5. We can configure any supplier for the price list item.
6. Once configured, at the time of selecting the pricelist rules, the rules with supplier will have higher priority over the rules without supplier.
7. If rule with supplier satisfies the other conditions like min qty product, category etc. and the supplier defined in the rule is also present in the vendor list of product, then that rule will be selected and the price will be applied accordingly.
8. If no rule with supplier found or none of supplier based rules satisfies the other conditions, then the pricelist rule without supplier will be checked and the price will be applied accordingly (native Odoo behaviour).

Dependencies
------------
    * This module depends on the 'sale_management' and 'purchase' modules of Odoo.
    * Dependency on purchase as purchase is the one which will bring the option of setting the vendor list in product. Moreover, the 'purchase' already depends on 'account' module and the 'account' is introducing the field 'supplier_rank' which is used in this module.
    * Dependency on sale_management to use the feature on SOs.


Dev Notes - Implementation
--------------------------
* I have inherited following two methods to achieve the functionality.
    - _get_applicable_rules() - method of product.pricelist model
    - _is_applicable_for() - method of product.pricelist.item model

 1. _get_applicable_rules():
    * This method is overridden to sort all applicable rules by giving priority to supplier based rules.
        - calling super() to get the native behaviour (filter based on date-range, rule type etc.).

        - We can not filter based on if the supplier is in the product.product.seller_ids in this method 
        as call can reach here with multiple products (let say Product A and Product B) and there can be a possibility of Product A have that supplier in his vendor list but Product B won't.

        - Further assume that the rule is applied to 'category' and both products are in same category.

        - For this setup the rule is applicable to Product A for sure but we must not apply this rule to Product B (as it don't have that supplier in its vendor list).
        
        - Hence to properly handle this situation I am only passing the sorted list from here giving the priority to supplier based rules.

2.  _is_applicable_for():
    * This method is overridden to add the extra condition for supplier based rules.
        - Calling super to get the native behaviour.

        - If the supplier based rule is eligible after super() call, then we are checking one more condition to make sure that the product is in the vendor list of the supplier.

        - If the condition is satisfied, then returning True else False.
        
        - The above setup won't impact the non-supplier based rules and it will still follow the native behaviour.


 