import base64

try:
    print()
    my_password_string = input('Password to encrypt: ')
    my_password_byte = my_password_string.encode()
    my_password_encrypted_byte = base64.b64encode(my_password_byte)
    my_password_encrypted_string = my_password_encrypted_byte.decode('utf-8')
    print()
    print('my_password_string = %s' % my_password_string)
    print('my_password_byte = %s' % my_password_byte)
    print('my_password_encrypted_byte = %s' % my_password_encrypted_byte)
    print('my_password_encrypted_string = %s' % my_password_encrypted_string)
except Exception as e:
    print(e)
