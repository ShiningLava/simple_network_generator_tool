# simple_network_generator_tool

simple_network_generator_tool is a python script that will generate a semi_random config file for LUDUS, who should be able to read this file and create a network. 

## Setup

1. Clone the repository
2. Run the script
- `python3 /simple_network_generator/main.py`
3. Copy output.yml to the LUDUS host and use it to define the target range
`scp user@ludus_ip /simple_network_generator/main.py /path/to/ludus/host/ludus-range-config.yml`
4. Deploy the range on LUDUS host

## Troubleshooting
soon(tm)
