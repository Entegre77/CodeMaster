# Sample code with potential security vulnerabilities

import os

password = os.environ.get('PASSWORD')

if password == '12345':
    print('Access granted!')
else:
    print('Access denied!')
