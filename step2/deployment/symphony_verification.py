import argparse
import support_tools

def symphony_verification():
    my_error_list = []
    # Wait for port to open
    my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=22, wait_time=300, check_interval=15)
    if my_return_value == True:
        # Verify Hostname Change before Rabbit MQ Configuration
        my_return_value = support_tools.send_ssh_command(host=args.myVM_FQDN, port=22, username='root', password='V1rtu@1c3!', command='hostname', return_output=True)
        if my_return_value.strip() == args.myVM_FQDN:
            print('Hostname verified: %s' % args.myVM_FQDN)
        else:
            print('Possible configuration error')
            print('%s does not match %s' % (my_return_value.strip(), args.myVM_FQDN))
            my_error_list.append('Hostname Rename Error')
        # Verify Consul Service
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=8500, wait_time=900, check_interval=15)
        if my_return_value == True:
            print('Consul verified')
        else:
            print('Consul failed to start')
            my_error_list.append('Consul Error')
        # Verify RabbitMQ
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=15672, wait_time=900, check_interval=15)
        if my_return_value == True:
            print('RabbitMQ verified')
        else:
            print('RabbitMQ failed to start')
            my_error_list.append('RabbitMQ Error')
        # Verify Configuration Insight
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=12000, wait_time=900, check_interval=15)
        if my_return_value == True:
            print('Configuration Insight verified')
        else:
            print('Configuration Insight failed to start')
            my_error_list.append('Configuration Insight Error')
        # Verify Log Collection
        my_return_value = support_tools.wait_for_port(host=args.myVM_FQDN, port=8082, wait_time=900, check_interval=15)
        if my_return_value == True:
            print('Log Collection verified')
        else:
            print('Log Collection failed to start')
            my_error_list.append('Log Collection Error')
        print('Error List: %s' % my_error_list)
    else:
        print('An error has occurred during deployment')
        print('Unable to connect to %s' % args.myVM_FQDN)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--myVM_FQDN', help='myVM_FQDN', required=True)
    args = parser.parse_args()

    symphony_verification()
