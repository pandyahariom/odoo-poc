from . import models


def _post_init_hook(env):
    group_user = env.ref("base.group_user").sudo()
    group_user._apply_group(env.ref("product.group_product_pricelist"))
