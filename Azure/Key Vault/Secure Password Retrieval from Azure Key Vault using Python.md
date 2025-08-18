# Azure Key Vault Access Setup Guide for Python Applications

> 🔐 **Goal:** Register an Azure AD application, grant it RBAC to read secrets from **Azure Key Vault**, and retrieve them from a **Python** script.

---

## ✅ Prerequisites
- Azure subscription access to:
  - Create **App registrations** in Microsoft Entra ID (Azure AD)
  - Assign **RBAC** roles on the target **Key Vault**
- Key Vault already created (you know its name)

---

## 🧭 Steps

### 1) 👤 Register the application
1. Open **Azure Portal** → **Microsoft Entra ID** → **App registrations** → **+ New registration**  
2. Name it: **App-Azure-Key-Vault-Reader** → **Register**

### 2) 🗝️ Create a Client Secret
1. In your new app, go to **Manage** → **Certificates & secrets** → **+ New client secret**  
2. Description: **App-Azure-Key-Vault-Reader-Client-Secret** → **Add**  
3. **Copy the `Value` now** (you’ll use it as the client secret in Python).  
   > ⚠️ You won’t be able to see it again after leaving the page.

### 3) 🔑 Grant Key Vault access (RBAC)
1. Open your **Key Vault** → **Access control (IAM)** → **+ Add** → **Add role assignment**  
2. Role: **Key Vault Secrets User** → **Next**  
3. **+ Select members** → choose **App-Azure-Key-Vault-Reader** → **Select**  
4. **Review + assign**

> 💡 **Why this role?** *Key Vault Secrets User* allows **get/list** secrets via RBAC (recommended over legacy access policies).

---

## 🧩 Values you’ll need for Python
- **TENANT_ID** (Directory ID)  
- **CLIENT_ID** (Application ID)  
- **CLIENT_SECRET** (from step 2)  
- **KEY_VAULT_NAME** (e.g., `kv-prod-001`)

Optionally export them as environment variables:

```bash
# macOS/Linux
export AZURE_TENANT_ID="<tenant-guid>"
export AZURE_CLIENT_ID="<app-client-id>"
export AZURE_CLIENT_SECRET="<client-secret>"
export KEY_VAULT_NAME="<your-kv-name>"
```

```powershell
# Windows PowerShell
$env:AZURE_TENANT_ID="<tenant-guid>"
$env:AZURE_CLIENT_ID="<app-client-id>"
$env:AZURE_CLIENT_SECRET="<client-secret>"
$env:KEY_VAULT_NAME="<your-kv-name>"
```

---

## 🧪 Test from Python

```bash
pip install azure-identity azure-keyvault-secrets
```

```python
import os
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

tenant_id = os.getenv("AZURE_TENANT_ID")
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
kv_name = os.getenv("KEY_VAULT_NAME")  # e.g., "kv-prod-001"

vault_url = f"https://{kv_name}.vault.azure.net/"

# Authenticate using the App Registration + Client Secret
credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
client = SecretClient(vault_url=vault_url, credential=credential)

# Replace with your secret name
secret_name = "my-db-password"
secret = client.get_secret(secret_name)
print(f"{secret_name} = {secret.value}")
```

> 🧷 **Tip:** If you need to list secrets, ensure the app has **list** permission via the RBAC role.  
> The `Key Vault Secrets User` role covers **get** and **list** for secrets.

---

## 🛠️ Troubleshooting

- 🔒 **“Access policies not available”**  
  Your Key Vault is configured for **RBAC** (recommended). Assign roles in **Access control (IAM)**, not in *Access policies*.

- 🚫 **`AuthenticationFailed` or `Forbidden`**  
  - Check **Tenant ID / Client ID / Client Secret**  
  - Confirm the role **Key Vault Secrets User** is **assigned** to the app’s Service Principal **on the Key Vault** (not just on the resource group/subscription, unless intentional).

- ⏳ **Role propagation delay**  
  Sometimes the role assignment takes a few minutes to become effective.

---

## 🧹 Security & Maintenance
- 🔁 **Rotate** the Client Secret periodically (and register the new version).  
- 🔐 Consider **Managed Identity** (if running in Azure) to avoid storing secrets in plain text.  
- 🧾 Use **Key Vault access logs** for auditing.

---

## ✅ Checklist (mark when complete)
- [ ] App registered (**App-Azure-Key-Vault-Reader**)  
- [ ] Client Secret created and **Value** stored securely  
- [ ] Role **Key Vault Secrets User** assigned to the app in the Key Vault  
- [ ] Environment variables configured  
- [ ] Secret retrieval tested successfully from Python

1. Create application [App registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade and select **+ New Registration**
2. Add a name for the application **App-Azure-Key-Vault-Reader** and select **Register**.
3. In the application, go to **Manage** -> **Certificate & secrets" and select **+ New client secret**.
4. Add a description **App-Azure-Key-Vault-Reader-Client-Secret** and select **Add**.
5. Save the column **Value**, it would be used as client secret in the python script.
6. Go to your **Key vault**, select **Access control (IAM)** and select **+ Add** -> **Add role assignment**
7. Select **Key Vault Secrets User** and select **Next**.
8. Select **+ Select members**, add the application **App-Azure-Key-Vault-Reader** and then click **Select**.
9. **Select Review + assign**
