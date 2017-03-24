import os
import pytest
import requests
import requests.packages.urllib3
import support_tools

my_symphony_fqdn = (os.environ['my_symphony_fqdn'])
my_rackhd_fqdn = (os.environ['my_rackhd_fqdn'])
my_coprhd_fqdn = (os.environ['my_coprhd_fqdn'])

def test_consul():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_symphony_fqdn, port=8500, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='http://' + my_symphony_fqdn + ':8500', allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_symphony_fqdn + ':8500')
    print('')

    assert my_pass_value == True

def test_configuration_insight():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_symphony_fqdn, port=12000, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='http://' + my_symphony_fqdn + ':12000', allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_symphony_fqdn + ':12000')
    print('')

    assert my_pass_value == True

def test_log_collection():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_symphony_fqdn, port=8082, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='http://' + my_symphony_fqdn + ':8082', allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_symphony_fqdn + ':8082')
    print('')

    assert my_pass_value == True

def test_rabbitmq():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_symphony_fqdn, port=15672, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='http://' + my_symphony_fqdn + ':15672', allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_symphony_fqdn + ':15672')
    print('')

    assert my_pass_value == True
	
def test_rcm_fitness():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_symphony_fqdn, port=19080, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='http://' + my_symphony_fqdn + ':19080', allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_symphony_fqdn + ':19080')
    print('')

    assert my_pass_value == True

def test_rackhd():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_rackhd_fqdn, port=8080, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='http://' + my_rackhd_fqdn + ':8080/api/2.0/config', allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_rackhd_fqdn + ':8080/api/2.0/config')
    print('')

    assert my_pass_value == True

def test_coprhd():
    my_pass_value = True
    my_return_value = support_tools.wait_for_port(host=my_coprhd_fqdn, port=80, wait_time=120, check_interval=15)
    if my_return_value == True:
        my_api_call = requests.request('GET', url='https://' + my_coprhd_fqdn, allow_redirects=True)
        print(my_api_call)
        if my_api_call.status_code == 200:
            my_pass_value = True
        else:
            my_pass_value = False
            print(my_api_call.status_code)
    else:
        my_pass_value = False

    print('')
    print('http://' + my_coprhd_fqdn)
    print('')

    assert my_pass_value == True