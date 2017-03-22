#!/usr/bin/python
import argparse
import sys
import time
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
parser.add_argument('--mySNAPSHOT_NAME', help='mySNAPSHOT_NAME', required=False, default=time.strftime('%Y-%m-%d_%H%M%S'))
args = parser.parse_args()

machine_info = utils.get_machine_info('machine_info.csv', 'VM_FQDN', args.myVM_FQDN)

if machine_info:
    rc = utils.vm_create_snapshot(machine_info['VM_FQDN'], args.mySNAPSHOT_NAME, machine_info['VCENTER_HOSTNAME'], machine_info['VCENTER_USERNAME'], machine_info['VCENTER_PASSWORD'])
else:
    print "\"%s\" not found in machine_info.csv!" % args.myVM_FQDN
    rc = 1
    
sys.exit(rc)
