resource "azurerm_network_interface" "" {
  name                = ""
  location            = ""
  resource_group_name = ""

  ip_configuration {
    name                          = "internal"
    subnet_id                     = ""
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = ""
  location            = ""
  resource_group_name = ""
  size                = "Standard_DS2_v2"
  admin_username      = ""
  network_interface_ids = []
  admin_ssh_key {
    username   = "adminuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBHQl2/7NshD07tXitiV1vjwJkvAGdlbJubrsHM591rfeAl/0l1kzQDaEV3H4VY5MOp0CGu60SHa79fgF32mcU3c1Ry+bursKf+fDO7jywkezqALlhL+rhNCSjPPV8jF6mYhH1pT0w/SYh5Worqb9LH3DjkSEBL+AusN94Mn6W4xX4xedCeyV2Ooh1FfdTjXFzTMagVT6gVclBifpOF9pDF/7dhcf8G2H2P9CF0sLANazEYVImsIUEPROcBkRTgk2wesOoNzKST8zD/DSfZfzLt5BERmkdRaW9Mqh4ZN6FnP/JiWhRr0GqmSaqZiDsd+KuuT+sszIS3h0z0J37KRjj"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
