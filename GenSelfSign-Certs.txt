###################################################################
#openssl command argument list/purpose:
	req tells openssl that we want to create a new certificate.

	-newkey tells openssl that we want to generate a new private key as well.

	rsa:2048 defines the encryption algorithm we want to use. This is similar to the --cipher-algo flag used by gpg. In this case, we're using the RSA algorithm with a 2048-bit key length.

	-nodes says to create the private key without a passphrase to protect it. This is similar to creating an SSH key without passphrase protection.

	-key lets us save the generated private key to an output file in Base64 format.

	-x509 ensures that our certificate is self-signed. The alternative is to use an existing certificate authority.

	-days specifies the number of days we want the certificate to be valid for. In our case, we'll choose to give our certificate 30 days of validity.

	-out saves the certificate to file, also in Base64 format.

###################################################################
#Now to create the magic:
#########################

#Generate a private key and self-signed certificate for SERVER:
$ openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

#Generate the Privacy Enhanced Mail (PEM) file by just appending the key and certificate files:
$ cat server.key server.crt > server.pem

#The files that contain the private key should be kept secret, thus adapt their permissions:
$ chmod 600 server.key server.pem

#Copy the trust certificate server.crt to the SSL client host
##################################################################
#Generate a private key and self-signed certificate for CLIENT:
$ openssl req -newkey rsa:2048 -nodes -keyout client.key -x509 -days 365 -out client.crt

#Generate the PEM file by just appending the key and certificate files:
$ cat client.key client.crt > client.pem

#The files that contain the private key should be kept secret, thus adapt their permissions:
$ chmod 600 client.key client.pem



#Copy client.crt to the server
###################################################################
#OpenSSL Server
$ socat OPENSSL-LISTEN:4433,fork,cert=server.pem,cafile=client.crt EXEC:/bin/bash
#OpenSSL Client
$ socat OPENSSL-CONNECT:localhost:4433,cert=client.pem,cafile=server.crt -
###################################################################



NOTE: If the openssl connection is not made or other issues persist use the verify=0 to ignore the client certificate.
#OpenSSL Server
$ socat OPENSSL-LISTEN:4433,fork,cert=server.pem,verify=0 EXEC:/bin/bash
#OpenSSL Client
$ socat OPENSSL-CONNECT:localhost:4433,verify=0 -
