import sys
import stem.control
from stem.descriptor.remote import DescriptorDownloader
from stem.version import Version
import os
import ipinfo

f_obs = open("obs.txt", "w")
f_avg = open("avg.txt", "w")
f_bur = open("bur.txt", "w")
downloader = DescriptorDownloader()
with stem.control.Controller.from_port() as controller:
  controller.authenticate()
  relay_fingerprints=""
  relay_bandwidth = []
  relay_compare = []
  print("CHECKING THE IP!")
  for desc in downloader.get_server_descriptors():
  	f_avg.write(str(desc.average_bandwidth)+ "\n")
  	f_bur.write(str(desc.burst_bandwidth)+ "\n")
  	f_obs.write(str(desc.observed_bandwidth)+ "\n")
f_avg.close()
f_obs.close()
f_bur.close()
os.system("sudo killall tor")