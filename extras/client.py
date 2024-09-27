import io
import time
import threading
import pycurl
import sys
import stem.control
import random 
import os

EXIT_FINGERPRINT = 'B0430D21D6609459D141078C0D7758B5CA753B6F'

SOCKS_PORT = 9050
CONNECTION_TIMEOUT = 2  # timeout before we give up on a circuit

def query(url, range):
  """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """
  #time.sleep(1) 
  #print(range)
  output = StringIO.StringIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.CONNECTTIMEOUT, CONNECTION_TIMEOUT)
  query.setopt(pycurl.RANGE, range)
  query.setopt(pycurl.WRITEFUNCTION, output.write)
  #query.setopt(pycurl.RANGE, range)
  f = open("log", "wt")
  try:
    query.perform()
    buffer = output.getvalue()
    #print(buffer)
    f.write(buffer)
    if "416 Requested Range Not Satisfiable" in buffer:
      print("Download Complete")
      #for thread in enumerate(threads):
        #thread.join()
      print(time.time() - start_time_whole)
      #tor_process.kill()  # stops tor
      os._exit(1)
    del buffer
  except pycurl.error as exc:
    raise ValueError("Unable to reach %s (%s)" % (url, exc))
    del output

def scan(controller, path, ctr_old, ctr_new):
  """
  Fetch check.torproject.org through the given path of relays, providing back
  the time it took.
  """
  range = str(ctr_old)+"-"+str(ctr_new)
  circuit_id = controller.new_circuit(path, await_build = True)

  def attach_stream(stream):
    if stream.status == 'NEW':
      controller.attach_stream(stream.id, circuit_id)

  controller.add_event_listener(attach_stream, stem.control.EventType.STREAM)

  try:
    controller.set_conf('__LeaveStreamsUnattached', '1')  # leave stream management to us
    start_time = time.time()

    #check_page = query('https://www.du.edu/', range)
    x = threading.Thread(target=query, args=('https://www.cs.purdue.edu/homes/arora105/output', range,))
    threads.append(x)
    x.start()
    #check_page = query('http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page')
    #print(check_page)
    #if 'Congratulations. This browser is configured to use Tor.' not in check_page:
      #raise ValueError("Request didn't have the right content")
    return time.time() - start_time
  finally:
    controller.remove_event_listener(attach_stream)
    controller.reset_conf('__LeaveStreamsUnattached')

ctr_old = 0
ctr_new = 10
threads = list()
flag = 0
count = 0
count2 = 0



with stem.control.Controller.from_port() as controller:
  controller.authenticate()
  relay_fingerprints=[]
  #relay_fingerprints = [desc.fingerprint for desc in controller.get_network_statuses()]
  for desc in controller.get_network_statuses():
    #print(desc.nickname)
    #if(int(desc.bandwidth) < 3000):
    relay_fingerprints.append(desc.fingerprint)
    count = count + 1
  print("total:" + str(count))
  #time.sleep(5)
  #relay_fingerprints.reverse()
  random.shuffle(relay_fingerprints)
  start_time_whole = time.time()
  for fingerprint in relay_fingerprints:
    count2 = count2 + 1
    try:
      num = random.randint(1, count)
      time_taken = scan(controller, [fingerprint, relay_fingerprints[num] , EXIT_FINGERPRINT], ctr_old, ctr_new)
      print('%s => %0.2f seconds' % (fingerprint, time_taken))
      ctr_old = ctr_new+1
      ctr_new = ctr_old + 1500000
        #print(desc.nickname)
    except Exception as exc:
      print('%s => %s' % (fingerprint, exc))

for thread in enumerate(threads):
  thread.join()

