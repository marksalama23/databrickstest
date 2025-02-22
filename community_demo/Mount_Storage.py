storage_account_name = dbutils.widgets.get("storage_account_name")
container_name = dbutils.widgets.get("container_name")
mount_point = dbutils.widgets.get("mount_point")

configs = {
    "fs.azure.account.auth.type": "OAuth",
    "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
    "fs.azure.account.oauth2.client.id": "fba6beb7-2b89-46dd-95a5-f30505b8ffc2",
    "fs.azure.account.oauth2.client.secret": "vkl8Q~46SI4iI2AQ3--Seeler81QSE0vcRbm5cYH",
    "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/<tenant_id>/oauth2/token"
}

dbutils.fs.mount(
    source=f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/",
    mount_point=mount_point,
    extra_configs=configs
)

print(f"Mounted {container_name} to {mount_point}")
