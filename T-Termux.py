import os
import time
import sys

os.system("clear")

logo = """\033[32m
████████╗░░░░░░████████╗███████╗██████╗░███╗░░░███╗██╗░░░██╗██╗░░██╗░░░
╚══██╔══╝░░░░░░╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║░░░██║╚██╗██╔╝░░░
░░░██║░░░█████╗░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║░░░██║░╚███╔╝░░░░
░░░██║░░░╚════╝░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░░██║░██╔██╗░░░░
░░░██║░░░░░░░░░░░░██║░░░███████╗██║░░██║██║░╚═╝░██║╚██████╔╝██╔╝╚██╗██╗
░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝"""

print (logo)

time.sleep(1.0)

print ()

logo1 = """\033[32m+--------------------------------------+
| This Tool Install All Basic Packages |
+--------------------------------------+
| Coded By Matheesha  | version : 1.0  |
+--------------------------------------+"""

print (logo1)

time.sleep(1.0)

def tprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

print ()

tprint('''\033[32m
[01] python          [20] python2
[02] python-dev      [21] golang
[03] python3         [22] php
[04] java            [23] git
[05] perl            [24] bash
[06] nano            [25] curl
[07] openssl         [26] openssh
[08] wget            [27] clang
[09] nmap            [28] w3m
[10] hydra           [29] ruby
[11] macchanger      [30] host
[12] dnsutils        [31] coreutils
[13] fish            [32] zip
[14] tor             [33] hydra
[15] figlet          [34] cowsay
[16] tar             [35] unzip
[17] vim             [36] ruby
[18] wcalc           [37] bmon
[19] unrar           [38] proot''')

tprint('''\033[32m
[+] This Command for access Storage in Termux''')

print ()

tprint("[+] Allow the Button For Access the Storage in Termux")

os.system ("termux-setup-storage")

print ()

choice = input("\033[32m[+] You Want to Install All Packages [y/n] :: ")

if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update")

else:
	print ()
	print ("\033[32m[+] Wrong Input")
	print ()
	sys.exit()

print ("\033[32m")

os.system ("apt upgrade -y")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install php -y")
os.system ("apt install python-dev -y")
os.system ("apt install python3 -y")
os.system ("apt install java -y")
os.system ("apt install git -y")
os.system ("apt install perl -y")
os.system ("apt install bash")
os.system ("apt install nano -y")
os.system ("apt install curl -y")
os.system ("apt install openssl -y")
os.system ("apt install openssh -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt install nmap -y")
os.system ("apt install w3m -y")
os.system ("apt install hydra -y")
os.system ("apt install ruby -y")
os.system ("apt install macchanger -y")
os.system ("apt install host -y")
os.system ("apt install dnsutils -y")
os.system ("apt install coreutils -y")
os.system ("apt install fish -y")
os.system ("apt install zip -y")
os.system ("apt install hydra -y")
os.system ("apt install figlet -y")
os.system ("apt install cowsay -y")
os.system ("apt install unzip -y")
os.system ("apt install vim -y")
os.system ("apt install ruby -y")
os.system ("apt install wcalc -y")
os.system ("apt install bmon -y")
os.system ("apt install unrar -y")
os.system ("apt install proot -y")
os.system ("apt install golang -y")

tprint ("\033[32m[+] Sucsussfully Installing Packages")

print ()

tprint ("\033[32m[+] Thank For Using")

time.sleep(3.0)

os.system("clear")

sys.exit()
