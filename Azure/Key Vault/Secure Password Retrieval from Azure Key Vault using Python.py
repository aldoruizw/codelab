import requests
import json

tenant_id = 'tenant_id'
client_id = 'client_id'
client_secret = 'client_secret'
vault_name = 'vault_name'
secret_name = 'secret_name'

# Get OAuth token
url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://vault.azure.net/.default"
}
token = requests.post(url, data=payload).json()["access_token"]

# Get secret
kv_url = f"https://{vault_name}.vault.azure.net/secrets/{secret_name}?api-version=7.4"
headers = {"Authorization": f"Bearer {token}"}
secret_value = requests.get(kv_url, headers=headers).json()["value"]

print("Secret is:", secret_value)

# import requests
# import json
# import sys

# # ========= FILL THESE IN =========
# tenant_id = 'tenant_id'
# client_id = 'client_id'
# client_secret = 'client_secret'
# vault_name = 'vault_name'
# secret_name = 'secret_name'
# # =================================

# # Azure AD token URL
# url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# # First try with 'scope'
# payload_scope = {
#     "grant_type": "client_credentials",
#     "client_id": client_id,
#     "client_secret": client_secret,
#     "scope": "https://vault.azure.net/.default"
# }

# # Then fallback with 'resource'
# payload_resource = {
#     "grant_type": "client_credentials",
#     "client_id": client_id,
#     "client_secret": client_secret,
#     "resource": "https://vault.azure.net"
# }

# def get_token():
#     # Try scope-based
#     resp = requests.post(url, data=payload_scope)
#     try:
#         resp_json = resp.json()
#     except Exception:
#         print("Error parsing token response:", resp.text)
#         sys.exit(1)

#     if "access_token" in resp_json:
#         return resp_json["access_token"]

#     print("Scope-based auth failed:", resp_json)

#     # Try resource-based
#     resp = requests.post(url, data=payload_resource)
#     resp_json = resp.json()
#     if "access_token" in resp_json:
#         return resp_json["access_token"]

#     print("Resource-based auth failed:", resp_json)
#     sys.exit(1)

# # Get the token
# token = get_token()

# # Use token to fetch secret
# kv_url = f"https://{vault_name}.vault.azure.net/secrets/{secret_name}?api-version=7.4"
# headers = {"Authorization": f"Bearer {token}"}
# response = requests.get(kv_url, headers=headers)

# if response.status_code == 200:
#     secret_value = response.json()["value"]
#     print("✅ Secret value:", secret_value)
# else:
#     print("❌ Failed to get secret:", response.status_code, response.text)
