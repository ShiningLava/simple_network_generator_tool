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

yaml_initiator = {'ludus': []}
## set defaults for config file
with open('config.yml', 'w') as file:
    yaml.safe_dump(yaml_initiator, file)

class Windows:

    def __init__(self):
        ## possible tasks: sysprep, install_additional_tools, office_version, office_arch
        tasks = []
    def add_tasks(self, task):
        self.tasks.append(task)

class Domain:

    ## will add option for other domains in the future
    fqdn = 'ludus.domain'
    role = 'primary-dc'
    #def __init__(self):
        #self.role = []
    #def add_role(self, role):
        #self.role.append(role)

class Testing:

    ## This is unfinished
    ## Needs functionality to return nothing if false
    ## and "testing:" dictionary with [snapshot: bool and block_internet: bool] if true

    def __init__(self, val):
         self.val = val
    def __bool__(self):
         return self.val != 0

def print_configs_to_config(vm_dict):
    #yaml_initiator = {'ludus': []}

    ## set defaults for config file
    #with open('config.yml', 'w') as file:
        #yaml.safe_dump(yaml_initiator, file)

    ## print yaml_output for testing
    #print(yaml_output)

    ## load current config.yml file
    with open('config.yml', 'r') as file:
        yaml_current = yaml.safe_load(file)
        yaml_current['ludus'].append(vm_dict)
        #yaml_current += yaml.safe_dump(yaml_output)

    ## append yaml_output for each VM to config.yml
    if yaml_current:
        with open('config.yml', 'w') as file:
            yaml.safe_dump(yaml_current, file)
        
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
    cpus = 2
    ram_gb = 4

    ## ludus_config should be changed to include the index number of the VM being created
    ## ie ludus_config_1, or ludus_config_7
    ## index number should effect vn_name, hostname, ip_last_octet

    ## This outputs single apostrophe instead of desired double quotes
    ## Unsure if this will affect the result when using config.yml for LUDUS
    vm_name_filler = "{{ range_id }}"
    vm_name = f"{vlan}-{last_octet}-{vm_name_filler}-ad-dc-win2022-server-x64"
    hostname_filler = "{{ range_id }}"
    hostname = f"{vlan}-{last_octet}-{hostname_filler}-DC01-2022"
    template = "win2022-server-x64-template"

    ## Order of yamp_output entry should be vm_name, hostname, template, vlan, ip_last_octet,
    ## ram_gb, cpus, windows, domain, linux, testing

    yaml_output = {}
    yaml_output.setdefault('ludus', [])
    #print(yaml_output)


    ## Need to append this dict to vm_dict
    dc = Domain()
    domain_dict = {}
    domain_dict.update({'fqdn': dc.fqdn})

    #dc.add_role('primary-dc')
    #yaml_output.append(f"{dc.roles}")
    domain_dict.update({'role': dc.role})
    print(domain_dict)

    ## Add windows tasks
    win = Windows()
    win_dict = {}
    win_dict.update({'sysprep': False})

    ## Create vm_dict and add keys and values to it to it
    vm_dict = {}
    vm_dict.update({'vm_name': vm_name})
    vm_dict.update({'hostname': hostname})
    vm_dict.update({'template': template})
    vm_dict.update({'vlan': vlan})
    vm_dict.update({'ip_last_octet': last_octet})
    vm_dict.update({'domain': domain_dict})
    vm_dict.update({'cpus': cpus})
    vm_dict.update({'ram_gb': ram_gb})
    vm_dict.update({'windows': win_dict})

    #print_configs_to_config(yaml_output)
    print_configs_to_config(vm_dict)
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
