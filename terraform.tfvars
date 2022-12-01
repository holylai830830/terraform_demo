#===============================================================================
# VMware vSphere configuration
#===============================================================================
# vCenter IP or FQDN #
vsphere_vcenter = "testlab-vcsa.testlab.systex.hk"
# vSphere username used to deploy the infrastructure #
vsphere_user = "holy.lai@vsphere.local"
vsphere_password = "Systex20140101"
# Skip the verification of the vCenter SSL certificate (true/false) #
vsphere_unverified_ssl = "true"
# vSphere datacenter name where the infrastructure will be deployed #
vsphere_datacenter = "SYSTEX"
# vSphere cluster name where the infrastructure will be deployed #
vsphere_cluster = "SYSTEX Lab"


#===============================================================================
# Virtual machine parameters
#===============================================================================
# The name of the virtual machine #
vm_name = "rhel-tf-provision01"
# The datastore name used to store the files of the virtual machine #
vm_datastore = "Testlab-DS1"
# The vSphere network name used by the virtual machine #
vm_network = "VM Lab Network (subnet 192.168.128.0%2f17)"
# The netmask used to configure the network card of the virtual machine (example: 24) #
vm_netmask = "17"
# The network gateway used by the virtual machine #
vm_gateway = "192.168.128.1"
# The DNS server used by the virtual machine #
vm_dns = "8.8.8.8"

# The vSphere template the virtual machine is based on #
vm_template = "Template-RHEL84"
# Use linked clone (true/false)
vm_linked_clone = "false"
# The number of vCPU allocated to the virtual machine #
vm_cpu = "2"
# The amount of RAM allocated to the virtual machine #
vm_ram = "1024"
# The IP address of the virtual machine #
vm_ip = "192.168.137.65"
vm_domain = "systexlab"
#Vswitch uuid
vm_switch_uuid ="50 1c 33 84 d3 b3 b1 80-81 fb 19 65 fd 39 79 9f"
