import argparse
import support_tools

def rackhd_disable_auth():
    my_error_list = []
    # Wait for port to open
    my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=22, wait_time=600, check_interval=15)
    if my_return_value == True:
        my_return_value = support_tools.file_copy_put(host=args.myVM_FQDN, port=22, username='vagrant', password='vagrant', source_file='rackhd-disable-auth-remote.py', destination_file='/opt/monorail/rackhd-disable-auth-remote.py')
        my_return_value = support_tools.send_ssh_command(host=args.myVM_FQDN, port=22, username='vagrant', password='vagrant', command='cd /opt/monorail;sudo python rackhd-disable-auth-remote.py', return_output=True)
        print(my_return_value)
        my_return_value = support_tools.send_ssh_command(host=args.myVM_FQDN, port=22, username='vagrant', password='vagrant', command='sudo reboot', return_output=False)
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=22, wait_time=120, check_interval=15)
    else:
        print('Unable to connect to %s' % args.myVM_FQDN)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
    args = parser.parse_args()

    rackhd_disable_auth()
