# Client file for setting up an Onion Service on CenTor

# This script is run by an Onion Service operator who wants to deploy his/her Onion Service 
# on CenTor. The script enables easy file transfer from the Onion Service operator's system to 
# a Bento Server.  

import socket

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csFT.connect((socket.gethostname(), 9001))

num = input("How many files would you like to send?: ")
csFT.send(num.encode())

folder = input("Enter the folder name for your Onion Service: ")
csFT.send(folder.encode())

directory = input("Enter path for file (_/_/): ")

#Send file
for i in range(0, int(num)):
    name = input("Enter file " + str(i+1)+ " name: ")
    csFT.send(name.encode())
    print(' * Sending files')
    with open(directory+name, 'rb') as fs: 
        while True:
            data = fs.read(1)
            csFT.send(data)
            if not data:
                print('Breaking from sending data')
                break
        csFT.send(b'~') 
        fs.close()

print(' * Sent files')     
