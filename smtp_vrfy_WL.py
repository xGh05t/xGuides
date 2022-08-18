#!/usr/bin/env python3
#By: xG//05t 
#Purpose: Fun & Research

# This script enumerates users on a remote SMTP server 
import socket
import sys
import re

def user_vrfy(host,userlist):
    print('[*] Establishing Connection, Please Wait...')
    userList = []
    # Create a Socket and connect
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, 25))
        banner = client.recv(1024).decode()
        
        print('\n[*] SUCCESS. Service Ready')
        print(banner)
        
        # VRFY a user
        with open(userlist, 'r') as file:
        # VRFY a user
            for user in file:
                client.send(f'VRFY {user} \r\n'.encode())
                result = client.recv(1024).decode()
                
                match = re.search('252', result)
                if match:
                    userList.append(user.strip())
        
        print(f'[*]Users email that exist on SMTP server')
        print(userList)
        print('\n[*] COMPLETE!')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: smtp_vrfy.py <IP/Host> <User_WordList>')
        sys.exit(0)
    else:
        user_vrfy(sys.argv[1],sys.argv[2])
