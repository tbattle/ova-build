import argparse
import requests
import requests.packages.urllib3
import support_tools

def rackhd_verification():
    my_error_list = []
    # Wait for port to open
    my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=22, wait_time=300, check_interval=15)
    if my_return_value == True:
        # Print config.json
        my_return_value = support_tools.send_ssh_command(host=args.myVM_FQDN, port=22, username='vagrant', password='vagrant', command='cat /opt/monorail/config.json', return_output=True)
        print('cat /opt/monorail/config.json')
        print(my_return_value)
        # Verify Active API
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=8080, wait_time=120, check_interval=15)
        if my_return_value == True:
            my_api_call = requests.request('GET', url='http://' + args.myVM_FQDN + ':8080/api/2.0/config', allow_redirects=False)
            print(my_api_call)
            if my_api_call.status_code == 200:
                pass
            else:
                my_error_list.append(my_api_call.status_code)
                print(my_api_call.status_code)
        else:
            print('RackHD API failed to start')
            my_error_list.append('RackHD API Error')
        print('Error List: %s' % my_error_list)
    else:
        print('An error has occurred during deployment')
        print('Unable to connect to %s' % args.myVM_FQDN)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
    args = parser.parse_args()

    rackhd_verification()
