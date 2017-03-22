#!/usr/bin/python
import argparse
import sys
import utils

parser = argparse.ArgumentParser()
parser.add_argument('--myOVA_URL', help='myOVA URL', required=True)
parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
args = parser.parse_args()

machine_info = utils.get_machine_info('machine_info.csv', 'VM_FQDN', args.myVM_FQDN)

if machine_info:
    vcenter_options = {"host": machine_info['VCENTER_HOSTNAME'], 
                       "username": machine_info['VCENTER_USERNAME'], 
                       "password": machine_info['VCENTER_PASSWORD'], 
                       "datacenter": machine_info['VCENTER_DATACENTER'], 
                       "cluster": machine_info['VCENTER_CLUSTER'], 
                       "datastore": machine_info['VCENTER_DATASTORE'],
                       "folder": machine_info['VCENTER_FOLDER']}
    vm_options = {"fqdn": machine_info['VM_FQDN'],
                  "ip": machine_info['VM_IP'],
                  "dns1": machine_info['VM_DNS1'],
                  "gateway": machine_info['VM_GATEWAY'],
                  "netmask": machine_info['VM_NETMASK'],
                  "network_label": machine_info['VM_NETWORK_LABEL'],
                  "name": machine_info['VM_FQDN']}
    rc = utils.deploy_ova_rackhd(args.myOVA_URL, vcenter_options, vm_options)
else:
    print "\"%s\" not found in machine_info.csv!" % args.myVM_FQDN
    rc = 1

sys.exit(rc)
