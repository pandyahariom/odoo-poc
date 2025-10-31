import requests

# API Endpoint: /json/2
# From O19 onwards Can get the doc of any model at : http://localhost:8069/doc
# Starting from O20 XML-RPC and JSON-RPC APIs at endpoints /xmlrpc, /xmlrpc/2 and /jsonrpc
# will be removed and are already depricated in O19.
# Reference : https://www.odoo.com/documentation/19.0/developer/reference/external_api.html
# Document also provides guideline regarding how to migrate Old APIs services: common, db and object

api_key = "7464e9d172ffbc53f86812b3d34f6e0504438760"
base_url = "http://localhost:8069/json/2"
headers = {
    "Authorization": f"Bearer {api_key}",
    # "X-Odoo-Database": "t",
}

# Create
input_dict = {
    "vals_list": [
        {
            "partner_id": 3,
            "partner_invoice_id": 3,
            "partner_shipping_id": 3,
            "user_id": 2,
            "team_id": 1,
            "company_id": 1,
        }
    ]
}

response = requests.post(
    f"{base_url}/sale.order/create",
    headers=headers,
    json=input_dict,
)
response.raise_for_status()
data = response.json()
print("Created Order:", data)

# Serach-Read
input_dict = {
    "domain": [["id", "in", [id for id in range(15)]], ["partner_id", "=", 3]],
    "fields": ["display_name", "id", "state", "partner_id"],
    "limit": 20,
}

response = requests.post(
    f"{base_url}/sale.order/search_read",
    headers=headers,
    json=input_dict,
)
response.raise_for_status()
data = response.json()
print("Found Orders:", data)


# Call to custom method - Assuming custom so_controller module is installed
response = requests.post(
    f"{base_url}/sale.order/custom_method",
    headers=headers,
    json={},
)
response.raise_for_status()
data = response.json()
print("Custom Method:", data)
