import argparse
import support_tools

def ssd_set():
    # Wait for port to open
    my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=22, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_return_value = support_tools.file_copy_put(host=args.myVM_FQDN, port=22, username='root', password='V1rtu@1c3!', source_file='ssd_amqp-post-1.0.jar', destination_file='ssd_amqp-post-1.0.jar')
        my_return_value = support_tools.file_copy_put(host=args.myVM_FQDN, port=22, username='root', password='V1rtu@1c3!', source_file='ssd_system_definition.json', destination_file='ssd_system_definition.json')
        my_return_value = support_tools.file_copy_put(host=args.myVM_FQDN, port=22, username='root', password='V1rtu@1c3!', source_file='ssd_collect_component_versions.json', destination_file='ssd_collect_component_versions.json')
        my_return_value = support_tools.send_ssh_command(host=args.myVM_FQDN, port=22, username='root', password='V1rtu@1c3!', command='java -jar ssd_amqp-post-1.0.jar ssd_system_definition.json', return_output=True)
        print(my_return_value)
        my_return_value = support_tools.send_ssh_command(host=args.myVM_FQDN, port=22, username='root', password='V1rtu@1c3!', command='java -jar ssd_amqp-post-1.0.jar ssd_collect_component_versions.json', return_output=True)
        print(my_return_value)
    else:
        print('Unable to connect to %s' % args.myVM_FQDN)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
    args = parser.parse_args()

    ssd_set()