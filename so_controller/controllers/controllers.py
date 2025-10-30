from odoo import http
from odoo.http import request
from urllib.parse import urlencode


class SoController(http.Controller):
    @http.route("/so_controller/so_list", auth="public")
    def sale_order_list(self, **kw):
        SOs = request.env["sale.order"].sudo().search([])
        message = kw.get("message", "")
        return request.render(
            "so_controller.so_list_template", {"sale_orders": SOs, "message": message}
        )

    @http.route(
        "/so_controller/delete_so/<int:order_id>",
        type="http",
        auth="user",
        methods=["POST"],
        csrf=False,
    )
    def delete_sale_order(self, order_id, **kwargs):
        order = request.env["sale.order"].browse(order_id)
        try:
            order_name = order.name
            order.unlink()
        except Exception as e:
            return request.redirect(
                "/so_controller/so_list?" + urlencode({"message": str(e)}),
            )
        return request.redirect(
            "/so_controller/so_list?"
            + urlencode(
                {"message": "Sale Order %s deleted successfully." % order_name}
            ),
        )
