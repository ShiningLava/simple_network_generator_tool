import yaml
import random

sites = random.randrange(1, 3)
pc_endpoints = random.randrange(3, 25)
printers = sites + (random.randrange(1, 3))
telephones = (2 * sites) + (pc_endpoints // random.randrange(2, 5))
cameras = sites * random.randrange(4, 15)
camera_vendor = ["Lorex", "Ring", "SimpliSafe", "Ubiquiti"]
camera_traits = ["customer rating", "outside", "inside", "bullet", "cloud managed", "locally managed"]
network_equipment_budget = sites * random.randrange(3500, 7500)
network_equipment_vendor = ["cisco", "juniper", "palo alto", "ubiquiti"]

class Windows:

    def __init__(self):
        ## possible tasks: sysprep, install_additional_tools, office_version, office_arch
        tasks = []
    def add_tasks(self, task):
        self.tasks.append(task)

class Domain:

    fqdn = 'ludus.domain'
    def __init__(self):
        self.roles = []
    def add_role(self, role):
        self.roles.append(role)

class Testing:

    ## This is unfinished
    ## Needs functionality to return nothing if false
    ## and "testing:" dictionary with [snapshot: bool and block_internet: bool] if true

    def __init__(self, val):
         self.val = val
    def __bool__(self):
         return self.val != 0

def create_vm_config(*args):
    ## create yaml entry custom for each device
    ## determine last_octet of IP address starting with .10, capping at arg
    device_number = args[0]
    devices_created = args[1]
    last_octet_counter = args[2]
    device_type = args[3]
    vlan = args[4]
    last_octet_cap = device_number
    starting_last_octet_value = 10
    last_octet = starting_last_octet_value + last_octet_counter
    yaml_output = []

    ## ludus_config should be changed to include the index number of the VM being created
    ## ie ludus_config_1, or ludus_config_7
    ## index number should effect vn_name, hostname, ip_last_octet

    ## This outputs single apostrophe instead of desired double quotes
    ## Unsure if this will affect the result when using config.yml for LUDUS
    vm_name = "{{ range_id }}-ad-dc-win2022-server-x64"
    hostname = "{{ range_id }}-DC01-2022"

    ## Order of yamp_output entry should be vm_name, hostname, template, vlan, ip_last_octet,
    ## ram_gb, cpus, windows, domain, linux, testing

    yaml_output.append(f"vm_name: {vm_name}")
    yaml_output.append(f"hostname: {hostname}")

    ## Template not yet defined
    #yaml_output.append(f"template")

    yaml_output.append(f"vlan: {vlan}")
    yaml_output.append(f"ip_last_octet: {last_octet}")
    yaml_output.append(f"ram_gb: 4")
    yaml_output.append(f"cpus: 2")


    ## Need to add domain attributes to a nested list in yaml_output for windows:
    dc = Domain()

    yaml_output.append(dc.fqdn)

    dc.add_role('primary-dc')
    yaml_output.append(f"{dc.roles}")

    x = Testing(0)
    if not x:
        yaml_output.append('x is false')
    else:
        yaml_output.append("testing")

    print(f"{yaml_output}\n")

    ## Need to implement an append to config file for yaml_output list
    ## Might need to add another list that contains all of the yaml_outputs for each VM

def add_printers_to_config(printers):
    devices_created = 1
    last_octet_counter = 0
    device_type = "printer"
    print(f"{device_type}: {printers}")
    vlan = 10

    ## append new machine to yaml config for each device
    while devices_created <= printers:
        print(f"creating {device_type} {devices_created}")

        ## arguments given to create_vm_config() must be in this order
        create_vm_config(printers, devices_created, last_octet_counter, device_type, vlan)
        devices_created += 1
        last_octet_counter += 1

def add_telephones_to_config(telephones):
    devices_created = 1
    last_octet_counter = 0
    device_type = "telephone"
    vlan = 20
    print(f"{device_type}: {telephones}")

    ## append new machine to yaml config for each device
    while devices_created <= telephones:
        print(f"creating {device_type} {devices_created}")

        ## arguments given to create_vm_config() must be in this order
        create_vm_config(telephones, devices_created, last_octet_counter, device_type, vlan)
        devices_created += 1
        last_octet_counter += 1

def add_pc_endpoints_to_config(pc_endpoints):
    devices_created = 1
    last_octet_counter = 0
    device_type = "pc endpoints"
    print(f"{device_type}: {pc_endpoints}")
    vlan = 100

    ## append new machine to yaml config for each device
    while devices_created <= pc_endpoints:
        print(f"creating {device_type} {devices_created}")

        ## arguments given to create_vm_config() must be in this order
        create_vm_config(pc_endpoints, devices_created, last_octet_counter, device_type, vlan)
        devices_created += 1
        last_octet_counter += 1

def add_cameras_to_config(cameras):
    ##
    print(f"cameras: {cameras}")

#def add_vms_to_config():
    ## this is the function to create a new config entry to be added to yaml config
    ## currently all device types will create the same VM template
    ## may change this in the future

def output_to_yaml():
    print(f"SAMPLE YAML OUTPUT")

    ## take the variables from the previous functions, concatenate them into a new variable
    ## dump the new variable to config.yml
    #full_config = 

    #with open('config.yml', 'w') as file:
      #yaml.dump(ludus, file)

def main():
    #add_sites_to_config(sites)
    add_printers_to_config(printers)
    add_telephones_to_config(telephones)
    add_pc_endpoints_to_config(pc_endpoints)
    add_cameras_to_config(cameras)

if __name__ == "__main__":
    main()
