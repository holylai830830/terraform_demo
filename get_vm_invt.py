import ssl
import mysql.connector
from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect

# Replace with your vCenter Server credentials and connection details
VCENTER_HOST = 'testlab-vcsa.testlab.systex.hk'
VCENTER_USER = 'holy.lai@vsphere.local'
VCENTER_PASSWORD = 'Systex20140101'
VCENTER_PORT = 443

# Replace with your MySQL database connection details
MYSQL_HOST = '192.168.137.66'
MYSQL_USER = 'cmdb'
MYSQL_PASSWORD = 'cmdb'
MYSQL_DATABASE = 'cmdb'

def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for item in container.view:
        if item.name == name:
            obj = item
            break
    return obj

def main():
    # Disable SSL verification (not recommended for production)
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_NONE

    # Connect to vCenter Server
    connection = SmartConnect(host=VCENTER_HOST, user=VCENTER_USER, pwd=VCENTER_PASSWORD, port=VCENTER_PORT, sslContext=context)
    content = connection.RetrieveContent()

    # Get all VMs
    vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vms = vm_view.view

    # Gather VM inventory data
    inventory = []
    for vm in vms:
        vm_data = {
            'name': vm.name,
            'power_state': vm.runtime.powerState,
            'guest_os': vm.config.guestFullName,
            'num_cpu': vm.config.hardware.numCPU,
            'memory_mb': vm.config.hardware.memoryMB,
        }
        inventory.append(vm_data)

    # Disconnect from vCenter Server
    Disconnect(connection)

    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = db_connection.cursor()

    # Insert inventory data into vmware_cmdb table
    insert_query = '''
        INSERT INTO vmware_cmdb (name, power_state, guest_os, num_cpu, memory_mb)
        VALUES (%(name)s, %(power_state)s, %(guest_os)s, %(num_cpu)s, %(memory_mb)s)
    '''
    for item in inventory:
        cursor.execute(insert_query, item)
        db_connection.commit()

    # Close MySQL database connection
    cursor.close()
    db_connection.close()

if __name__ == '__main__':
    main()
