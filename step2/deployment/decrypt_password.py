import base64

try:
    print()
    my_password_string = input('Password to decrypt: ')
    my_password_byte = my_password_string.encode()
    my_password_decrypted_byte = base64.b64decode(my_password_byte)
    my_password_decrypted_string = my_password_decrypted_byte.decode('utf-8')
    print()
    print('my_password_string = %s' % my_password_string)
    print('my_password_byte = %s' % my_password_byte)
    print('my_password_decrypted_byte = %s' % my_password_decrypted_byte)
    print('my_password_decrypted_string = %s' % my_password_decrypted_string)
except Exception as e:
    print(e)
