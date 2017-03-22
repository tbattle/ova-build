#!/usr/bin/python
import argparse
import sys
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
args = parser.parse_args()

machine_info = utils.get_machine_info('machine_info.csv', 'VM_FQDN', args.myVM_FQDN)

if machine_info:
    rc = utils.vm_power_on(machine_info['VM_FQDN'], machine_info['VCENTER_HOSTNAME'], machine_info['VCENTER_USERNAME'], machine_info['VCENTER_PASSWORD'])
else:
    print "\"%s\" not found in machine_info.csv!" % args.myVM_FQDN
    rc = 1

sys.exit(rc)
