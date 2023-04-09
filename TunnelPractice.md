   HOME				      Jump1			        Jump2			      Target1              Target2           
 192.168.11.15		 100.64.36.17	   	 >192.0.2.80         192.168.34.10      192.168.34.100
..............      ..............      172.17.10.80<       ..............      .............. 
--------------      --------------      --------------      --------------      --------------
|            |      |            |      |            |      |            |      |            |
|            ------->2222        |      |            |      |            |      |            |
|        2201>====================------>22          |      |            |      |            |
|        1110>========================================------>445         |      |            |
|        1111<========================================------<1111        |      |            |
|        2202>=======================================------->22          |      |            |
|            |      |            |      |            |      |            |      |            |
|            |      |            |      |            |      |            |      |            |
--------------      --------------      --------------      --------------      --------------


Command Syntax:
=======================================================
OnHome Box
=======================================================
#To permit root login if needed
##sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && systemctl start sshd && systemctl status sshd

ssh -MS JUMP1 -p 2222 user@100.64.36.17 -L 2201:192.0.2.80:22
ssh -MS JUMP2 -p 2201 user@127.0.0.1 -L 1110:192.168.34.10:445 -R 1111:127.0.0.1:1111 -L 2202:192.168.34.10:22

ssh -MS TARGET1 -p 2202 user@127.0.0.1 


ssh -MS <socket.file> -p <Port#> user@ip
ssh -S <socket.file> .                                                      (or user@ip if . does not work)

#How to use SecureCopy with Socket.File
scp -o "ControlPath=<socket.file>" -P <Port#> .:<RemoteFile> <LocalFile>     (or user@ip if . does not work)
scp -o "ControlPath=<socket.file>" -P <Port#> <LocalFile> .:<RemoteFile>     (or user@ip if . does not work)
