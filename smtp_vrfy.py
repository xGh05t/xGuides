#!/usr/bin/env python3
#By: xG//05t 
#Purpose: Fun & Research

# This script enumerates a user on a remote SMTP server 
import socket
import sys
import re

def user_vrfy(host):
    print('[*] Establishing Connection, Please Wait...')

    # Create a Socket and connect
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, 25))
        banner = client.recv(1024).decode()
        
        print('\n[*] SUCCESS. Service Ready')
        print(banner)
        
        while True:
            print('\n================================')
            print('Type "quit" to exit program')
            # Ask for a username to search for
            username = input('\nUsername to query: ')
            
            if username == 'quit':
                print('Goodbye! =)')
                sys.exit(0)
            else:
                # VRFY a user
                client.send(f'VRFY {username} \r\n'.encode())
                result = client.recv(1024).decode()
                
                match = re.search('252', result)
                if match:
                    print(f'[*] The {username} email address exists on SMTP server.')
                else:
                    print(f'[*] SORRY! The {username} email address does not exist on SMTP server.')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: smtp_vrfy.py <IP/Host>")
        sys.exit(0)
    else:
        user_vrfy(sys.argv[1])
