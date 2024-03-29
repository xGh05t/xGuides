# Anonymous Port Scanning: Nmap + Tor + ProxyChains-ng
By: xG//05t <br>
Purpose: Fun & Research <br>
NOTES: <br>
This guide demonstrates a scanning technique using Nmap through the TOR network via Proxychains. <br>
It prevents the source IP from being disclosed to the target. <br>
All standard default ports are used. However, the ports can be changed via config files to suit needs. <br>
The example target used for this guide is scanme.nmap.org <br>

===================================================
## TOR Browser Ports: 9150/9151
## ProxyChains/TOR Service Port: 9050
-----------------------------------------------------
### INSTALL Packages/Binaries
```sh
# Debian
sudo apt update; sudo apt install tor nmap proxychains-ng
# RedHat
sudo dnf check-update; sudo dnf update; dnf install tor nmap proxychains-ng
# Arch
sudo pacman -Syyu; sudo pacman -S tor nmap proxychains-ng
```
-----------------------------------------------------
## SET-UP Config Files
#### The sed commands below specifies SOCKS version 5 vs version 4 (Default)
#### This config file is also where to change the default port if needed

## Config file for proxychains-ng
```sh
sudo sed -i 's/socks4..127/socks5 127/' /etc/proxychains4.conf
```
-----------------------------------------------------

## START TOR Service
```sh
# Start service and check status
# SysV Init system (Older Method)
sudo services tor start
sudo services tor status

##############

# Systemd system (Newer Method)
sudo systemctl start tor
sudo systemctl status tor
```

-----------------------------------------------------
## Check that localhost is listening on specified TOR Port
```sh
# Example: 127.0.0.1:9050	0.0.0.0:*	LISTEN  <PID>\tor
sudo netstat -antp | grep -i tor

##############
## THE COMMAND
### Notes:
-sT : TCP Full Connect
-Pn : Treat all hosts as online -- skip host discovery
 If settings are correct, execute.

sudo proxychains4 nmap -sT -Pn scanme.nmap.org 2>/dev/null
```

# BONUS: To ensure that the IP address won't be disclosed to the target
```sh
sudo iptables -A OUTPUT --dest scanme.nmap.org -j DROP

# Check iptables entry
sudo iptables -nvL
```

**********************
 ## EXTRA
 Not needed to for execution
 Anonymous DNS resolution tool vs dig or nslookup. 
**********************
## To prevent DNS leaks, use tor-resolve command to resolve a hostname to an IP address
### Example
tor-resolve scanme.nmap.org
