# To use PowerShell Sessions

# First: Create Session
$dcsesh = New-PSSession -Computer SANDBOXDC

# Last: Execute commands through Session
Invoke-Command -Session $dcsesh -ScriptBlock {ipconfig}
Copy-Item "C:\Users\Public\whoami.exe" -Destination "C:\Users\Public\" -ToSession $dcsesh

## Call evil binaries
Invoke-Command -Session $dcsesh -ScriptBlock {C:\Users\Public\whoami.exe}