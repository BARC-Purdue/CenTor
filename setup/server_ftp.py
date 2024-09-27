# Server file for setting up an Onion Service on CenTor

# This script is run by a Bento server who is willing to host an Onion Service 
# using CenTor. The script enables easy file transfer from the Onion Service operator's system to 
# a Bento Server. It sets up an Onion Service using Apache. 

# Assumption: 
# 1. we assume that a configuration file has already been allocated by Bento Server operator (<folder>.conf)
# 2. we assume that configuration files and onion service directory has already been 
# mentioned in the SGX manifest file by the Bento Server operator (<folder>.conf)

import socket
import os
import fileinput
import os
import shutil
from stem.control import Controller

# STEP 1: FILE TRANSFER

# Setting up the socket
ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind((socket.gethostname(), 9001))
ssFT.listen(1)
(conn, address) = ssFT.accept()
num = int(conn.recv(2))
folder = conn.recv(20)
folder = folder.decode()

# Setting up the webservice directory
os.system("mkdir /var/www/"+ folder)
#permission = ("chmod -R 755 " + folder)
#os.system(permission)

# Receiving the files
for i in range(0, num):
    text_file = conn.recv(20)
    text_file = text_file.decode()
    with open("/var/www/"+folder + "/" + text_file, "w") as fw:
        print("* Receiving")
        while True:
            data = conn.recv(1)
            data = data.decode()
            if data == '~':
                print('* Breaking from file write')
                break
            else:
                fw.write(data)
    fw.close()
print("* All files received")


# STEP 2: ONION SERVICE START



print('* Connecting to tor')

with Controller.from_port() as controller:
    controller.authenticate()

    # All hidden services have a directory on disk. Lets put ours in tor's data
    # directory.

    hidden_service_dir = os.path.join(controller.get_conf('DataDirectory', '/tmp'), folder)

    # Create a hidden service where visitors of port 80 get redirected to local

    print("* Creating our hidden service in %s" % hidden_service_dir)

    result = controller.create_hidden_service(hidden_service_dir, 80, target_port = 80)

    # The hostname is only available when we can read the hidden service
    # directory. This requires us to be running with the same user as tor.

    if result.hostname:
        print("* Our service is available at %s !" % result.hostname)
    else:
        print("* Unable to determine our service's hostname, probably due to being unable to read the hidden service directory")

# STEP 3: SETUP APACHE

# Setup the apache Configuration file
config_file = "sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/"+folder+".conf"
os.system(config_file)

# Edit the config file
with open("/etc/apache2/sites-available/"+folder+".conf", 'r') as file :
  filedata = file.read()

# Mention the target server name and document folder
filedata = filedata.replace("#ServerName www.example.com", "ServerName "+ result.hostname)
filedata = filedata.replace("/var/www/html", "/var/www/"+ folder)

with open("/etc/apache2/sites-available/"+folder+".conf", 'w') as file:
  file.write(filedata)

# Enable the configuration file
os.system("cd /etc/apache2/sites-available")
enable = "sudo a2ensite "+folder+".conf"
os.system(enable)

# Restart Apache
os.system("sudo systemctl restart apache2")
try:
  close = input(" * Press a key to shut!")
finally:
        # Shut down the hidden service and clean it off disk. Note that you *don't*
        # want to delete the hidden service directory if you'd like to have this
        # same *.onion address in the future.
  print(" * Shutting down our hidden service")
  os.system("rm -r " + hidden_service_dir)



