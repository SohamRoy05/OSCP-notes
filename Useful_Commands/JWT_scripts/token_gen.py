import jwt


json_data={"_id":"61ea9b797be466045e943ca5","name":"theadmin","email":"test@test.com","iat":1642780590}
payload="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MWVhOWI3OTdiZTQ2NjA0NWU5NDNjYTUiLCJuYW1lIjoidGVzdGVkIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNjQyNzgwNTkwfQ.HzcrBovGTyPYl_9wzcJ7BnxiBmGvpHklyB0ELyvBsuo"
secret="gXr67TtoQL8TShUc8XYsK2HvsBYfyQSFCFZe4MQp7gRpFuMkKjcM72CNQN4fMfbZEKx4i7YiWuNAkmuTcdEriCMm9vPAYkhpwPTiuVwVhvwE"

token=jwt.encode(payload=json_data,algorithm='HS256',key=secret)
#token=jwt.decode(payload=en_token,algorithms=['HS256'],key=secret,ver)

print(token)