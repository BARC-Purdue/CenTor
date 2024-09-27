import sys
import stem.control
from stem.descriptor.remote import DescriptorDownloader
from stem.version import Version
import os

downloader = DescriptorDownloader()
count = 0 
ctr = 1
count2 = 0
#os.system("sudo killall tor")
#os.system("tor")
with stem.control.Controller.from_port() as controller:
  controller.authenticate()
  relay_fingerprints=""
  relay_bandwidth = {}
  #relay_compare = []
  print("CHECKING THE NETWORK STATUS!")
  print("PICKING SUITABLE RELAYS!")
  for desc in downloader.get_server_descriptors():
    #if((desc.tor_version != Version('0.3.5.10') and desc.tor_version != Version('0.3.5.11') and desc.tor_version != Version('0.4.2.7') and desc.tor_version != Version('0.4.2.8') and desc.tor_version != $
    #if(int(desc.average_bandwidth) > int(1079000000)):
      #relay_fingerprints = relay_fingerprints + desc.fingerprint + ","
    relay_bandwidth[desc.fingerprint]=desc.observed_bandwidth
    count = count + 1
  print("DONE PICKING!")
  print("---------------------------STATS ON CURRENT RELAYS:--------------------------")
  print("total: " + str(count))
  print("min: " + str(min(relay_bandwidth.values())))
  print("len: " + str(len(relay_bandwidth)))
  print("avg: " + str(sum(relay_bandwidth.values()) / len(relay_bandwidth)))
  print("max: " + str(max(relay_bandwidth.values())))
  print("---------------------------STATS AFTER ELIMINATING RELAYS:--------------------------")
  fast = int((0.125)*count)
  for i in range(0,fast):
    #print("max: " + str(max(relay_bandwidth)))
    bandwidth = max(relay_bandwidth.values())
    keymax = max(relay_bandwidth, key = relay_bandwidth.get)
    del relay_bandwidth[keymax]
  print("min: " + str(min(relay_bandwidth.values())))
  print("len: " + str(len(relay_bandwidth)))
  print("avg: " + str(sum(relay_bandwidth.values()) / len(relay_bandwidth)))
  print("max: " + str(max(relay_bandwidth.values())))
  #print(str(relay_fingerprints))
  print("total: " + str(len(relay_bandwidth)))
f = open("exclude", "w")
for key, value in relay_bandwidth.items() :
  relay_fingerprints=relay_fingerprints + str(key) +","

f.write(str(relay_fingerprints))
f.close()
os.system("sudo killall tor")