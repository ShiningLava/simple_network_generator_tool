import random
import json
import argparse

VERSION = "1.1.0"

with open('config.json', 'r') as g:
    config = json.load(g)

sites = 
pc_endpoints = 
printers = 
telephones = 
cameras = 
network_budget = 

def main():

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
