import threading    #IMPORTS
import socket
import datetime

host='localhost'    #EDIT THIS TO CHANGE THE HOST

def ftp_server():   #FTP SERVER
    global ftp
    while True:
        data,ip=ftp.accept()
        print (f'Service: FTP IP: {ip[0]}')
        time=datetime.datetime.now()
        print (time)
        print ()

def ssh_server():   #SSH SERVER
    global ssh
    while True:
        data,ip=ssh.accept()
        print (f'Service: SSH IP: {ip[0]}')
        time=datetime.datetime.now()
        print (time)
        print ()

def http_proxy():   #HTTP PROXY SERVER
    global http
    while True:
        data,ip=http.accept()
        print (f'Service: HTTP proxy IP: {ip[0]}')
        time=datetime.datetime.now()
        print (time)
        print ()


print ('Starting..')

ftp=socket.socket()
ftp.bind((host,21))

ssh=socket.socket()
ssh.bind((host,22))

http=socket.socket()
http.bind((host,8080))

ftp.listen()
ssh.listen()
http.listen()

ftp_=threading.Thread(target=ftp_server)    #THREADING
ssh_=threading.Thread(target=ssh_server)
http_=threading.Thread(target=http_proxy)

ftp_.start()
ssh_.start()
http_.start()

ftp_.join()
ssh_.join()
http_.join()

