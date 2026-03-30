resource "azurerm_resource_group" "main" {
  name     = "blood-donor-rg"
  location = "westeurope"
}

resource "azurerm_container_registry" "acr" {
  name                = "blooddonoracr78452"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = true
}
