import io
import time
import pycurl

import stem.process

from stem.util import term

SOCKS_PORT = 7000

file = open("exclude", "r")
EXCLUDE = file.read()

def progress(download_t, download_d, upload_t, upload_d):
    f.write(str(time.time())+","+str(download_t)+","+str(download_d)+"\n")
def query(url):
  """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

  output = io.BytesIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)
  query.setopt(pycurl.NOPROGRESS, False)
  query.setopt(pycurl.XFERINFOFUNCTION, progress)
  try:
    query.perform()
    return output.getvalue()
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)


# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    #'ExcludeNodes' : str(EXCLUDE)
    #'StrictNodes' : '0',
  },
  init_msg_handler = print_bootstrap_lines,
)
f=open("data/la.txt", "w")
print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))
start_time = time.time()
print(term.format(query("http://xpznyhql2uczf3v6lj3wqcnbjr65avqfzrrem7oif5umfnayej6oyiqd.onion/download"), term.Color.BLUE))
print(time.time() - start_time)
tor_process.kill()  # stops tor
f.close()
file.close()

