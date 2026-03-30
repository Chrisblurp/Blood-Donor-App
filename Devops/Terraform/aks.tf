
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "blood-donor-aks"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  dns_prefix          = "blooddonoraks"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "standard_b2ls_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin = "azure"
  }
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.aks.kube_config_raw
  sensitive = true
}
