import io
import pycurl
import time
import stem.process
from stem.util import term
import threading
import os
import sys

def mtor(): 

  SOCKS_PORT = 7000
  
  ctr_old = 0
  # change me
  ctr_new = 2001778
  threads = list()
  name = 0
  global ctr
  ctr = 0
  def progress(download_t, download_d, upload_t, upload_d):
    f3.write(str(threading.current_thread().ident)+","+str(time.time())+","+str(download_t)+","+str(download_d)+"\n")
  def query(url,range, name):
    """
    Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
    """
    output = io.BytesIO()
    global ctr
    query = pycurl.Curl()
    query.setopt(pycurl.URL, url)
    query.setopt(pycurl.PROXY, 'localhost')
    query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
    query.setopt(pycurl.RANGE, range)
    query.setopt(pycurl.WRITEFUNCTION, output.write)
    query.setopt(pycurl.NOPROGRESS, False)
    query.setopt(pycurl.XFERINFOFUNCTION, progress)
    try:
      query.perform()
      buffer = output.getvalue()
      while ctr != name:
        continue
      print("ctr:"+str(ctr))
      ctr = ctr + 1
      #print(buffer)
      if b"416 Requested Range Not Satisfiable" in buffer:
        print("Download Complete")
        print(time.time() - start_time)
        f.close()
        f2.close()
        tor_process.kill()
        os._exit(1)
      else:
        print(buffer)
        #f2.write(str(buffer))
        #change me as per the number of threads
        if(ctr==5):
          print("Download Complete")
          print(time.time() - start_time)
          f2.write("total time"+ str(time.time() - start_time))
          f2.write("\n timestamp"+ str(time.time()))
          f.close()
          f2.close()
          time.sleep(20)
          tor_process.kill()
          os._exit(1)
      del buffer
    except pycurl.error as exc:
      raise ValueError("Unable to reach %s (%s)" % (url, exc))
      del output

    except pycurl.error as exc:
      return "Unable to reach %s (%s)" % (url, exc)


  def print_bootstrap_lines(line):
    if "Bootstrapped " in line:
      #print(term.format(line, term.Color.BLUE))
      pass

  f = open("exclude", "r")
  #change me
  f2 = open("file5", "w")
  # change me as per the experiments
  f3 = open("data/5tor.txt", "w")
  FINGERPRINTS = f.read()

  #print(term.format("Starting Tor:\n", term.Attr.BOLD))

  tor_process = stem.process.launch_tor_with_config(
    config = {
      'SocksPort': str(SOCKS_PORT),
      'MaxCircuitDirtiness': str(1),
      'ExcludeNodes': str(FINGERPRINTS),
    },
    init_msg_handler = print_bootstrap_lines,
  )

  c=0
  start_time = time.time()
  # change me as per the number of threads/circuit
  while(c<5):
    range = str(ctr_old)+"-"+str(ctr_new)
    x = threading.Thread(target=query, args=('http://xpznyhql2uczf3v6lj3wqcnbjr65avqfzrrem7oif5umfnayej6oyiqd.onion/download', range, name))
    #x = threading.Thread(target=query, args=('https://stem.torproject.org/tutorials/the_little_relay_that_could.html', range, name,))
    threads.append(x)
    x.start()
    time.sleep(2)
    ctr_old = ctr_new + 1
    # change me
    ctr_new = ctr_old + 2001778
    name = name + 1
    c=c+1
mtor()
