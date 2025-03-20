import random
import json
import argparse

VERSION = "1.1.0"

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


def main():

    print(f"Number of sites: {sites}")
    print(f"Number of PCs per site: {pc_endpoints}")
    print(f"Number of printers: {printers}")
    print(f"Number of phones: {telephones}")
    print(f"Number of cameras: {cameras}")
    print(f"Prefered camera vendor: {random.choice(camera_vendor)}")
    print(f"Desired camera traits: {random.sample(camera_traits, 2)}")
    print(f"Desired network vendor: {random.choice(network_equipment_vendor)}")
    print(f"Network budget: {network_equipment_budget}")

def argparser():
    global sites
    global pc_endpoints
    global printers
    global telephones
    global cameras
    global network_budget
    parser.add_argument("--config", "-c", type=argparse.FileType('r', encoding='UTF-8'))
    #parser.add_argument("")

    if args.config:
        try:
            config = json.load(args.config)
            parser.set_defaults(**config)
        except Exception as e:
            print(e)

    return parser.parse_args()
if __name__ == "__main__":
    main()
