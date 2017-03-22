import base64
import csv
import os
import paramiko
import re
import subprocess
import sys
import time
import urllib
from pysphere import VIServer

OVFTOOL_OPTIONS = ['--diskMode=thin', '--powerOffTarget', '--skipManifestCheck', '--acceptAllEulas', '--overwrite', '--powerOffTarget', '--noSSLVerify']
OVFTOOL_PATH = '/usr/bin/ovftool'

def check_keys(dict, *required_keys):
    for key in required_keys:
        if key not in dict or dict[key] is None or not dict[key].strip():
            print "\"%s\" not defined or is empty!" % key
            sys.exit(1)

def deploy_ova(ova_url, vcenter_options={}, vm_options={}, ovftool_path=OVFTOOL_PATH, ovftool_options=OVFTOOL_OPTIONS, retries=3):
    if ova_url is None or not ova_url.strip():
        print "\"OVA_URL\" not defined or is empty!"
        sys.exit(1)
    check_keys(vcenter_options, "host", "username", "password", "datacenter", "cluster", "datastore", "folder")
    check_keys(vm_options, "fqdn", "ip", "dns1", "gateway", "netmask", "network_label")
    if 'name' not in vm_options.keys() or not vm_options['name']:
        vm_options['name'] = vm_options['fqdn'].strip()
    ovftool_options.append('--name=%s' % vm_options['name'].strip())
    ovftool_options.append('--vmFolder=%s' % vcenter_options['folder'].strip())
    ovftool_options.append('--datastore=%s' % vcenter_options['datastore'].strip())
    ovftool_options.append('--network=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--prop:vami.hostname=%s' % vm_options['fqdn'].strip())
    ovftool_options.append('--prop:vami.ip0.vision=%s' % vm_options['ip'].strip())
    ovftool_options.append('--prop:vami.DNS.vision=%s' % vm_options['dns1'].strip())
    if 'dns2' in vm_options.keys() and vm_options['dns2'].strip():
        ovftool_options.append('--prop:vami.DNS2.vision=%s' % vm_options['dns2'].strip())
    ovftool_options.append('--prop:vami.gateway.vision=%s' % vm_options['gateway'].strip())
    ovftool_options.append('--prop:vami.netmask0.vision=%s' % vm_options['netmask'].strip())
    vi_path = 'vi://%s:%s@%s/%s/host/%s' % (urllib.quote(vcenter_options['username'].strip()), urllib.quote(vcenter_options['password'].strip()), vcenter_options['host'].strip(), vcenter_options['datacenter'].strip(), vcenter_options['cluster'].strip())
    command = [ovftool_path] + ovftool_options + [ova_url.strip(), vi_path]
    print 'Executing "' + re.sub(r'(^.+\s+vi://.+?:)(.+?)(@.+$)', r'\1******\3', ' '.join(command)) + '" ...'
    sys.stdout.flush()
    rc = 1
    for i in range(retries):
        print 'Attempt %d of %d' % (i+1, retries)
        sys.stdout.flush()
        rc = subprocess.call(command, stderr=subprocess.STDOUT)
        sys.stdout.flush()
        if rc == 0:
            break
        time.sleep(60)
    return rc

def deploy_ova_coprhd(ova_url, vcenter_options={}, vm_options={}, ovftool_path=OVFTOOL_PATH, ovftool_options=OVFTOOL_OPTIONS, retries=3):
    if ova_url is None or not ova_url.strip():
        print "\"OVA_URL\" not defined or is empty!"
        sys.exit(1)
    check_keys(vcenter_options, "host", "username", "password", "datacenter", "cluster", "datastore", "folder")
    check_keys(vm_options, "fqdn", "ip", "dns1", "gateway", "netmask", "network_label", "vip", "dom")
    if 'name' not in vm_options.keys() or not vm_options['name']:
        vm_options['name'] = vm_options['fqdn'].strip()
    ovftool_options.append('--name=%s' % vm_options['name'].strip())
    ovftool_options.append('--vmFolder=%s' % vcenter_options['folder'].strip())
    ovftool_options.append('--datastore=%s' % vcenter_options['datastore'].strip())
    ovftool_options.append('--net:Bridged=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--network=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--prop:network.hostname.SetupVM=%s' % vm_options['fqdn'].strip())
    ovftool_options.append('--prop:network.ipv40.SetupVM=%s' % vm_options['ip'].strip())
    ovftool_options.append('--prop:network.ipv4dns.SetupVM=%s' % vm_options['dns1'].strip())
    ovftool_options.append('--prop:network.ipv4gateway.SetupVM=%s' % vm_options['gateway'].strip())
    ovftool_options.append('--prop:network.ipv4netmask0.SetupVM=%s' % vm_options['netmask'].strip())
    ovftool_options.append('--prop:network.vip.SetupVM=%s' % vm_options['vip'].strip())
    ovftool_options.append('--prop:network.DOM.SetupVM=%s' % vm_options['dom'].strip())
    vi_path = 'vi://%s:%s@%s/%s/host/%s' % (urllib.quote(vcenter_options['username'].strip()), urllib.quote(vcenter_options['password'].strip()), vcenter_options['host'].strip(), vcenter_options['datacenter'].strip(), vcenter_options['cluster'].strip())
    command = [ovftool_path] + ovftool_options + [ova_url.strip(), vi_path]
    print 'Executing "' + re.sub(r'(^.+\s+vi://.+?:)(.+?)(@.+$)', r'\1******\3', ' '.join(command)) + '" ...'
    sys.stdout.flush()
    rc = 1
    for i in range(retries):
        print 'Attempt %d of %d' % (i+1, retries)
        sys.stdout.flush()
        rc = subprocess.call(command, stderr=subprocess.STDOUT)
        sys.stdout.flush()
        if rc == 0:
            break
        time.sleep(60)
    return rc

def deploy_ova_rackhd(ova_url, vcenter_options={}, vm_options={}, ovftool_path=OVFTOOL_PATH, ovftool_options=OVFTOOL_OPTIONS, retries=3):
    if ova_url is None or not ova_url.strip():
        print "\"OVA_URL\" not defined or is empty!"
        sys.exit(1)
    check_keys(vcenter_options, "host", "username", "password", "datacenter", "cluster", "datastore", "folder")
    check_keys(vm_options, "fqdn", "ip", "dns1", "gateway", "netmask", "network_label")
    if 'name' not in vm_options.keys() or not vm_options['name']:
        vm_options['name'] = vm_options['fqdn'].strip()
    ovftool_options.append('--name=%s' % vm_options['name'].strip())
    ovftool_options.append('--vmFolder=%s' % vcenter_options['folder'].strip())
    ovftool_options.append('--datastore=%s' % vcenter_options['datastore'].strip())
    ovftool_options.append('--net:ADMIN=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--net:BMC=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--net:CONTROL=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--net:PDU=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--network=%s' % vm_options['network_label'].strip())
    ovftool_options.append('--prop:adminIP=%s' % vm_options['ip'].strip())
    ovftool_options.append('--prop:adminDNS=%s' % vm_options['dns1'].strip())
    ovftool_options.append('--prop:adminGateway=%s' % vm_options['gateway'].strip())
    ovftool_options.append('--prop:adminNetmask=%s' % vm_options['netmask'].strip())
    vi_path = 'vi://%s:%s@%s/%s/host/%s' % (urllib.quote(vcenter_options['username'].strip()), urllib.quote(vcenter_options['password'].strip()), vcenter_options['host'].strip(), vcenter_options['datacenter'].strip(), vcenter_options['cluster'].strip())
    command = [ovftool_path] + ovftool_options + [ova_url.strip(), vi_path]
    print 'Executing "' + re.sub(r'(^.+\s+vi://.+?:)(.+?)(@.+$)', r'\1******\3', ' '.join(command)) + '" ...'
    sys.stdout.flush()
    rc = 1
    for i in range(retries):
        print 'Attempt %d of %d' % (i+1, retries)
        sys.stdout.flush()
        rc = subprocess.call(command, stderr=subprocess.STDOUT)
        sys.stdout.flush()
        if rc == 0:
            break
        time.sleep(60)
    return rc

def exec_command(ssh, command):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    while not ssh_stdout.channel.exit_status_ready():
        sys.stdout.write(ssh_stdout.read(100))
        sys.stdout.flush()
    try:
        sys.stdout.write(ssh_stdout.read())
        sys.stdout.flush()
    except:
        pass
    rc = int(ssh_stdout.channel.recv_exit_status())
    return rc

def get_machine_info(csvfilename, key, value, decode_vcenter_password=True):
    with open(csvfilename) as csvfile:
        readCSV = csv.DictReader(csvfile, delimiter=',')
        for row in readCSV:
            if row[key].lower() == value.lower():
                if decode_vcenter_password and row['VCENTER_PASSWORD']:
                    row['VCENTER_PASSWORD'] = base64.b64decode(row['VCENTER_PASSWORD']).decode('utf-8')
                return row
    return None

def ssh_connect(hostname, username, password, timeout=60):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print 'Connecting to %s ...' % hostname.strip(),
    sys.stdout.flush()
    try:
        ssh.connect(hostname.strip(), username=username.strip(), password=password.strip(), timeout=timeout)
        print "OK"
    except paramiko.AuthenticationException, e:
        ssh.close()
        print "FAILED"
        print str(e).strip()
        sys.exit(1)
    except Exception, e:
        ssh.close()
        print "FAILED"
        print "Connection Failed: %s" % str(e).strip()
        sys.exit(1)
    sys.stdout.flush()
    return ssh
    
def vcenter_connect(host, username, password):
    print 'Connecting to vcenter "%s"...' % (host)
    sys.stdout.flush()
    server = VIServer()
    server.connect(host.strip(), username.strip(), password.strip())
    sys.stdout.flush()
    print 'Vcenter connected'
    sys.stdout.flush()
    return server

def vm_connect(vm_name, vcenter):
    print 'Connecting to VM "%s"...' % (vm_name.strip())
    sys.stdout.flush()
    try:
        vm = vcenter.get_vm_by_name(vm_name.strip())
    except Exception, e:
        print 'Failed to find or connect to VM "%s"!' % (vm_name.strip())
        print str(e).strip()
        sys.stdout.flush()
    print 'VM connected'
    sys.stdout.flush()
    return vm

def vm_create_snapshot(vm_name, snapshot_name, host, username, password):
    vcenter = vcenter_connect(host, username, password)
    vm = vm_connect(vm_name, vcenter)
    print 'Creating snapshot "%s"...' % snapshot_name.strip()
    sys.stdout.flush()
    vm.create_snapshot(snapshot_name.strip())
    sys.stdout.flush()
    print 'Snapshot created'
    sys.stdout.flush()
    return 0

def vm_power_off(vm_name, host, username, password, wait_for_tools=False, wait_for_tools_timeout=120):
    vcenter = vcenter_connect(host, username, password)
    vm = vm_connect(vm_name, vcenter)
    print 'Powering off VM...'
    sys.stdout.flush()
    vm.power_off()
    print 'VM powered off'
    sys.stdout.flush()

def vm_power_on(vm_name, host, username, password, wait_for_tools=False, wait_for_tools_timeout=120):
    vcenter = vcenter_connect(host, username, password)
    vm = vm_connect(vm_name, vcenter)
    print 'Powering on VM...'
    sys.stdout.flush()
    vm.power_on()
    print 'VM powered on'
    sys.stdout.flush()
    if wait_for_tools:
        print 'Waiting for VMware Tools to start ...'
        sys.stdout.flush()
        vm.wait_for_tools(timeout=wait_for_tools_timeout)
        sys.stdout.flush()
        print 'VMware Tools started'
        sys.stdout.flush()
    return 0

def vm_revert_snapshot(vm_name, host, username, password, snapshot_name=None):
    vcenter = vcenter_connect(host, username, password)
    vm = vm_connect(vm_name, vcenter)
    if snapshot_name is not None and snapshot_name.strip():
        print 'Reverting VM to snapshot "%s"...' % (snapshot_name.strip())
        sys.stdout.flush()
        vm.revert_to_named_snapshot(snapshot_name.strip())
        sys.stdout.flush()
    else:
        print 'Reverting VM to the current snapshot...'
        sys.stdout.flush()
        vm.revert_to_snapshot()
        sys.stdout.flush()
    print 'VM reverted'
    sys.stdout.flush()
    return 0
