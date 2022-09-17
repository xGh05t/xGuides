# Creates a Wget Powershell Script 
# By: xG//05t 
# Purpose: Fun/Research

$webclient = New-Object System.Net.WebClient 
$url = "http://IPAddress/RemoteFileName" 
$file = "new-FileName.exe" 
$webclient.DownloadFile($url,$file) 
