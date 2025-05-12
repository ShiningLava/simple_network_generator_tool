import yaml
import random
#import json
#import argparse

#VERSION = "1.1.0"

#with open('config.json', 'r') as g:
#    config = json.load(g)

sites = random.randrange(1, 3)
pc_endpoints = random.randrange(3, 25)
printers = sites + (random.randrange(1, 3))
telephones = (2 * sites) + (pc_endpoints // random.randrange(2, 5))
cameras = sites * random.randrange(4, 15)
camera_vendor = ["Lorex", "Ring", "SimpliSafe", "Ubiquiti"]
camera_traits = ["customer rating", "outside", "inside", "bullet", "cloud managed", "locally managed"]
network_equipment_budget = sites * random.randrange(3500, 7500)
network_equipment_vendor = ["cisco", "juniper", "palo alto", "ubiquiti"]

## may need to change this to specific devices
## ie printers_created, or phones_created, etc
vms_created = 0
vms_to_be_created = 0

## other variables from NCS:
## sites = 
## pc_endpoints = 
## printers = 
## telephones = 
## cameras = 

#def add_sites_to_config(sites):
    ## each site will add:
    ## at least one router
    ## at least one printer
    ## at least three pc_endpoints
    ## at least two telephones
    ## at least four cameras

def add_printers_to_config(printers):
    ##
    print(f"printers: {printers}")

def add_telephones_to_config(telephones):
    ##
    print(f"telephones: {telephones}")

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
    

## this might need to be changed to less than or equal to
while vms_created < vms_to_be_created:
    ## This should add a new entry into the final yaml for each VM specified
    ## ie If vms_to_be_created is 10, this should create 10 VMs in config.yaml
    add_vm_to_config()

    ## increment the vms_created counter until the desired number of VMs are defined
    vms_created += 1

    ## may need to change to great than or equal to vm_number
    if vms_created == vms_to_be_created:
        break

## output yaml file (final output preview)
## ludus_config should be changed to include the index number of the VM being created
## ie ludus_config_1, or ludus_config_7
## index number should effect vn_name, hostname, ip_last_octet
ludus_config = """
ludus:
  - vm_name: "{{ range_id }}-ad-dc-win2022-server-x64"
    hostname: "{{ range_id }}-DC01-2022"
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

if __name__ == "__main__":
    main()
