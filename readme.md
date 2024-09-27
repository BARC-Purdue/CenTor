# CenTor: CDN for Tor

We seek to develop an infrastructure that will allow users to deploy scalable Onion Services by replicating their content across multiple Tor routers. Replicas can allow the Onion Service owner to then go offline and reduce hops by making the replicas go non-anonymous. Further, a client can make use of CenTor architecture and compose functions with it. A client can also choose a geographically closer replica to further reduce latency. 

## Experimentation
* Anonymity Metrics: We gather and generate (using scripts as explained below) to define the anonymity achieved by a client who chooses to use CenTor. This anonymity is defined using entropy of distribution of clients across locations/ASNs and countries in a region selected by a client.
* Latency: We showcase the latency difference by comparing file download times over Vanilla Tor (6-hop), CenTor without choosing a region (i.e a 3-hop reduction) and CenTor (a 3-hop reduction as well as geographically defined region/shadow)

### Scripts
#### For generating data (```\src\data```)
* ```users.py```: Proportionally divides IPs of ASNs as per the total number of users in a country. For instance, if an ASN has two-fifths of the total number of IPs in a country (as collected in ```\data\<country_asn.txt>```) having a total of 100 users (as collected in ```users.txt```), then that ASN would be allocated 40 users (generated in ```\data\generated\<country_final.txt>```).
* ```country.py```: Generates relays per country. 
* ```entry_node.py```: Generates entry nodes per country.
* ```exit_node.py```: Generates exit nodes per country.

#### For generating metrics (```\src\metrics```)
* ```country_entropy.py```: Calculates entropy of distribution of clients across countries in a shadow (region selected by a client). 
* ```asn_entropy.py```: Calculates entropy of distribution of clients across locations (i.e ASNs) in a shadow (region selected by a client). 
* ```relay_density.py```: Calculates density of Tor relays in a shadow (region selected by a client). 
* ```entry_density.py```: Calculates density of Tor entry relays in a shadow (region selected by a client). 
* ```exit_density.py```: Calculates density of Tor exit relays in a shadow (region selected by a client). 


### Data Files
#### Tor data
* ```users.txt```: This file contains the number of Tor users per country (collected on 23rd April'21 from [Tor Metrics](https://metrics.torproject.org/userstats-relay-country.html)). 
* ```entry.txt```: This file contains the number of Tor entry nodes per country. Data is gathered using ```entry_node.py```. 
* ```exit.txt```: This file contains the number of Tor exit nodes per country. Data is gathered using ```exit_node.py```. 
#### ASN data
* ```\data\<country_asn.txt>```: This file contains the number of IPs per ASNs in the respective country. Data is gathered using [ipinfo.io](https://ipinfo.io/countries).
* ```\data\generated\<country_final.txt>```: This file contains the number of IPs per ASNs proportional to the total number of users of the respective country. Data is gennerated using ```users.py```.
* ```relay_data.txt```: This file contains the number of Tor nodes per country. Data is gathered using ```country.py```. 

### Working with Bento
#### Server side:
- needs apache2 installed   
- make sure tor is running 
- start a bento server         
#### Client side
- make sure centor.func has the correct listening address and port (if client connecting from other than localhost set listening to 0.0.0.0)    
- upload the centor server as a bento function (centor.func) using bento-driver.py: `python3 bento-driver.py <bento addr> <port>`   
- make sure the client (client_ftp.py has the correct connection address   
- connect to function with client: `cd setup`, `python3 client_ftp.py`  
	- input: 1, test, test/, index.html  

 