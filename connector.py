import socket
import random
import time

print ('Starting--------')
time.sleep(10)

ports =[21,22,8080]
while True:
    soc=socket.socket()
   # time.sleep(2)
    port=ports[random.randint(0,2)]
    soc.connect(('localhost',port))
    soc.close()
