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

class vars_joined_for_yml_output:
    def __init__(self, sites, pc_endpoints, printers, telephones, cameras):
        self.sites = sites
        self.pc_endpoints = pc_endpoints
        self.printers = printers
        self.telephones = telephones
        self.cameras = cameras

    def vars_together(self):
        print(f"sites: {self.sites}\npc_endpoints: {self.pc_endpoints}\nprinters: {printers}\ntelephones: {telephones}\ncameras: {cameras}")

all_vars = vars_joined_for_yml_output(sites, pc_endpoints, printers, telephones, cameras)
all_vars.vars_together()

def create_vm_config(*args):
    ## create yaml entry custom for each device

    ## determine last_octet of IP address starting with .10, capping at arg
    device_number = args[0]
    devices_created = args[1]
    last_octet_cap = device_number
    starting_last_octet_value = 10
    last_octet_counter = args[2]
    device_type = args[3]
    last_octet = starting_last_octet_value + last_octet_counter
    print(f"{device_type} {devices_created} last octet = {last_octet}\n")


def add_printers_to_config(printers):
    devices_created = 1
    last_octet_counter = 0
    device_type = "printer"
    print(f"printers: {printers}")

    ## append new machine to yaml config for each device
    while devices_created <= printers:
        print(f"creating {device_type} {devices_created}")

        ## arguments given to create_vm_config() must be in this order
        create_vm_config(printers, devices_created, last_octet_counter, device_type)
        devices_created += 1
        last_octet_counter += 1

def add_telephones_to_config(telephones):
    devices_created = 1
    last_octet_counter = 0
    device_type = "telephone"
    print(f"{device_type}: {telephones}")

    ## append new machine to yaml config for each device
    while devices_created <= telephones:
        print(f"creating {device_type} {devices_created}")

        ## arguments given to create_vm_config() must be in this order
        create_vm_config(telephones, devices_created, last_octet_counter, device_type)
        devices_created += 1
        last_octet_counter += 1

def add_pc_endpoints_to_config(pc_endpoints):
    ##
    print(f"pc_endpoints: {pc_endpoints}")

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

## output yaml file (final output preview)
## ludus_config should be changed to include the index number of the VM being created
## ie ludus_config_1, or ludus_config_7
## index number should effect vn_name, hostname, ip_last_octet

## This outputs single apostrophe instead of desired double quotes
## Unsure if this will affect the result when using config.yml for LUDUS
vm_name = "{{ range_id }}-ad-dc-win2022-server-x64"
hostname = "{{ range_id }}-DC01-2022"
ludus_config = f"""
ludus:
  - vm_name: \"{vm_name}\"
    hostname: \"{hostname}\"
    template: win2022-server-x64-template
    vlan: 10
    ip_last_octet: 11
    ram_gb: 8
    cpus: 4
    windows:
      sysprep: false
    domain:
      fqdn: ludus.domain
      role: primary-dc
"""

## print the preview of the config.yml file
print(yaml.dump(yaml.safe_load(ludus_config)))

## save the output to config.yml file
ludus = yaml.safe_load(ludus_config)
with open('config.yml', 'w') as file:
  yaml.dump(ludus, file)

def main():
    #add_sites_to_config(sites)
    add_printers_to_config(printers)
    add_telephones_to_config(telephones)
    add_pc_endpoints_to_config(pc_endpoints)
    add_cameras_to_config(cameras)
    #add_vms_to_config()
    output_to_yaml()

if __name__ == "__main__":
    main()
