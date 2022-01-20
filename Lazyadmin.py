#Built by AKB on 1/19/2022
import easygui as easy
import socket 
import getpass as gp

Hostname = socket.gethostname()
local_ip = socket.gethostbyname(Hostname)
user = gp.getuser()


easy.msgbox( ("Machine Name ... " + Hostname  +'\nIP Address... ' + local_ip + '\nThe User Is... ' + user), title="LazyAdmin", ok_button="Close Window")
