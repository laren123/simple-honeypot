import threading
import socket
import datetime

host='localhost'

def ftp_server():
    global ftp
    while True:
        data,ip=ftp.accept()
        print (f'Service: FTP IP: {ip[0]}')
        time=datetime.datetime.now()
        print (time)
        print ()

def ssh_server():
    global ssh
    while True:
        data,ip=ssh.accept()
        print (f'Service: SSH IP: {ip[0]}')
        time=datetime.datetime.now()
        print (time)
        print ()

def http_proxy():
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

ftp_=threading.Thread(target=ftp_server)
ssh_=threading.Thread(target=ssh_server)
http_=threading.Thread(target=http_proxy)

ftp_.start()
ssh_.start()
http_.start()

ftp_.join()
ssh_.join()
http_.join()

