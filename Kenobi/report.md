## Vulnerability Exploited: 
   1. mod-file in Proftpd 1.3.5 which allows an unauthorised user to move files in a server from one directory to the other.
   2. samba smbd allows guest user to view files in smb server as a normal user.

## Enumeration:
   * Run nmap scan  `sudo nmap -sC -sV -sS <Machine IP>|tee nmap.txt`  to view open ports,versions of services and run the default scripts.
   

## Gaining Access:
   1. Command `smbclient -R smb://<Machine IP>/anonymous` helps to view the shares on the smbserver.    
   2. Download the file **log.txt**.
   3. **log.txt** tells the version of Proftpd running on port 21,it also gives the location of private key of ssh for user kenobi.
   4. From the nmap scan in step 1,we can see rpcbind is running on port 111.
   5. We will run a NFS(Network File system) command `sudo showmount -e <Machine IP>` to see the exported folder in the network which we found is _var_.
   6. Now we will exploit proftpd mod-file vulnerability by copying _id_rsa_ in **.ssh** folder in kenobi user home directory to a separatec folder in mount folder var. 
   7. Now Mount this folder __var__ in your own file sytem in a separate directory.
   8. By changing the file permission of _id_rsa_ to 600(read and write by owner), connect to ssh server **Openssh** on port 22 as user 
   *Kenobi*.
   9. BOOM!! Got **Shell**.

## Priviledge Escalation:
   1. Run the command `find / -perm -u=s -type f 2>/dev/null` to find the programs with SUID bit on.
   2. We find a strange program named **menu** in the list of SUID programs.
   3. Using command `strings /usr/bin/menu` , we notice that _ifconfig_, _curl_ and _uname -r_ are present in binary of **menu** program,
   4. Run the command `cp usr/bin/sh /home/kenobi/ifconfig` to create a shell executable named *ifconfig* in *home* directory.
   5. Edit the **PATH** environment variable using the command `export PATH =/home/kenobi:$PATH`.
   6. Run the menu program and select ifconfig as a choice.
   7. BOOM!!!! We are **Root**
