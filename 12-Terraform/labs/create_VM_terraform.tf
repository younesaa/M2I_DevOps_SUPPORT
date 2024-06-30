provider "azurerm" {
  features {}  
}

resource "azurerm_resource_group" "terraform-group-2" {
  name     = "terraform-machine-2_group"
  location = "North Europe"
}



resource "azurerm_virtual_network" "main" {
  name                = "terraform-network"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.terraform-group-2.location
  resource_group_name = azurerm_resource_group.terraform-group-2.name
}


resource "azurerm_subnet" "internal" {
  name                 = "internal"
  resource_group_name  = azurerm_resource_group.terraform-group-2.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_network_interface" "main" {
  name                = "terraform-nic"
  location            = azurerm_resource_group.terraform-group-2.location
  resource_group_name = azurerm_resource_group.terraform-group-2.name

  ip_configuration {
    name                          = "terraform-testconfiguration1"
    subnet_id                     = azurerm_subnet.internal.id
    private_ip_address_allocation = "Dynamic"
  }
}

# Create a public IP address
resource "azurerm_public_ip" "terraform-public-ip" {
  name                = "terraform-public-ip"
  location            = azurerm_resource_group.terraform-group-2.location
  resource_group_name = azurerm_resource_group.terraform-group-2.name
  allocation_method   = "Dynamic"
}

resource "azurerm_linux_virtual_machine" "main" {
  name                  = "terraform-vm"
  location              = azurerm_resource_group.terraform-group-2.location
  resource_group_name   = azurerm_resource_group.terraform-group-2.name
  network_interface_ids = [azurerm_network_interface.main.id]
  size               = "Standard_DS1_v2"
  admin_username      = "testadmin"
  admin_password      = "Password1234!"


  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  admin_ssh_key {
    username   = "testadmin"
    public_key = file("~/.ssh/id_rsa.pub")
  }
}