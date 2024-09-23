```
HOME		     Jump1 (Nix)          Jump2 (Nix)         Target1 (Win)      Target2 (Nix)           
 192.168.11.15      100.64.36.17        >192.0.2.80         192.168.34.10      192.168.34.100
..............      ..............      172.17.10.80<       ..............      .............. 
--------------      --------------      --------------      --------------      --------------
|            |      |            |      |            |      |            |      |            |
|            ------->2222        |      |            |      |            |      |            |
|        2201>====================------>22          |      |            |      |            |
|        1110>========================================------>445         |      |            |
|        1111<========================================-------------------<1111  |            |
|        2202>=======================================------->22(SOCAT-Tun)|     |            |
|        2203>==================================================================>22          |
|            |      |            |      |            |      |            |      |            |
|            |      |            |      |            |      |            |      |            |
--------------      --------------      --------------      --------------      --------------
```

## Command Syntax:
To permit root login if needed
```sh
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' 's/#GatewayPorts No/GatewayPorts yes/' /etc/ssh/sshd_config && systemctl start sshd && systemctl status sshd
```

### SSH Pastables for track above
```sh
ssh -MS /tmp/JUMP1 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 2222 user@100.64.36.17 -L 2201:192.0.2.80:22
ssh -MS /tmp/JUMP2 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 2201 user@127.0.0.1 -L 1110:192.168.34.10:445 -R 1111:127.0.0.1:1111 -L 2202:192.168.34.10:22
Create Socat or sshuttle bind on port 22
ssh -MS /tmp/TARGET1 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 2202 user@127.0.0.1 -L 2203:192.168.34.100:22
ssh -MS /tmp/TARGET2 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 2203 user@127.0.0.1
```

### SocketFile Usage
```sh
ssh -S <socket.file> .     (or user@ip if . does not work)
```

### How to use SecureCopy with Socket.File
```sh
scp -o "ControlPath=<socket.file>" -P <Port#> .:<RemoteFile> <LocalFile>     (or user@ip if . does not work)
scp -o "ControlPath=<socket.file>" -P <Port#> <LocalFile> .:<RemoteFile>     (or user@ip if . does not work)
```
