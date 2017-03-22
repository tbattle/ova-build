import argparse
import requests
#from requests.packages.urllib3.exceptions import InsecurePlatformWarning, InsecureRequestWarning, ConnectionError
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
import support_tools

def coprhd_verification():
    my_error_list = []
    # Wait for port to open
    my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=22, wait_time=300, check_interval=15)
    if my_return_value == True:
        # Verify Login Page
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=80, wait_time=120, check_interval=15)
        if my_return_value == True:
            my_api_call = requests.request('GET', url='https://' + args.myVM_FQDN, verify=False, allow_redirects=True)
            print(my_api_call)
            if my_api_call.status_code == 200:
                pass
            else:
                my_error_list.append(my_api_call.status_code)
                print(my_api_call.status_code)
        else:
            print('CoprHD Login Page failed to start')
            my_error_list.append('CoprHD Login Page Error')
        print('Error List: %s' % my_error_list)
    else:
        print('An error has occurred during deployment')
        print('Unable to connect to %s' % args.myVM_FQDN)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
    args = parser.parse_args()

    coprhd_verification()
