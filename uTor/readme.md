# Multi-path Routing (uTor) for Bento

## Introduction

Large performance variance is one of the main obstacles that throttles further expansion of Tor (which is the most popular anonymous communication system). Bandwidth-intensive applications, such as video streaming, latency-sensitive applications, such as web browsing, for the scarce resources further impede Tor's growth. In this work, we propose a different approach by exploring new capabilities of Tor to support bulk data transfers without degrading the performance of interactive traffic. We achieve this by building a python function for Bento[1], which runs completely over Tor. In other words, we do not alter anything in the Tor architecture. We also run experiments over the real Tor network to demonstrate that uTor for Bento performs better than the traditional Tor network, for clients downloading large data (or streaming interactive data). 

## Assumption 

Here, we assume that both client and the Hidden (Onion) Service agree to use uTor. 

## Related Work 

We draw inspiration from the work [3], which aims to solve the performance paradox caused by bulk traffic by constructing an anonymous tunnel consisting of ```m``` circuits where ```m``` is a client-specific parameter. Contrary from this work, we do not modify anything in the Tor code. Also, based on their[3] results, we conclude that many bandwidth resources are under-utilized. However, the fact that under the current Tor design a large number of low-bandwidth relays are indeed idle, but they should not be used by interactive users for the purpose of performance shows potential to support bulk applications. If we can make use of these low-quality resources to transfer bulk traffic, the relay utilization will be increased and the traffic on high-bandwidth relays will be reduced, so that interactive users will also benefit from it.

Tang and Goldberg propose a new circuit scheduler which prioritizes interactive traffic over bulk traffic based on the exponentially weighted moving average (EWMA) of relayed cells [7]. However, experiments on simulator show that EWMA-based scheduler highly depends on network and load, so it is not clear if performance will always improve [6]. 

## Anonymity v/s Latency Tradeoff

By preferring low bandwidth relays (about seven-eighth), we are definitely reducing the set of relays for the client to construct circuits. This does not imply that we are completely compromising on the anonimity, as almost all countries have low-bandwidth relays[4]. In other words, with this approach, we are not completely eliminating a particular country/region or relays (just preferring low bandwidth relays). 


## Approach

The idea here is to parallely retrieve data from the Hidden (Onion) Service using multiple circuits and then sequentially organize them for the client. We achieve this using the Python Stem library for Tor. Note, the architecture works for both normal webpages as well as Onion Services. 



## Experimentation
0. Firts we run the `fingerprints.py` script which generates an `exclude` file listing top one-eighth fast relays which we later exclude on both client and server side. We selaunch Tor with `StrictNodes=0` so as to not completely eliminate these resources. [Refer](https://2019.www.torproject.org/docs/tor-manual.html.en) 
1. We then start by launching the Onion Service using a customized ```torrc```, i.e. we provide the tor configuration at run-time in the python script ```utor_launch_service.py```. We do this so as to prefer the usage of low-bandwidth Tor relays in the circuit construction. 
2. We use the similar approach on the uTor client side. 
3. The client script (`uTor.py`) then retrieves data from different circuits or paths from the Onion Service using ```threads```. 
4. We then organize the data on the client side by forcing ```threads``` to execute sequentially (scheduling). 
5. We enforce "new-circuit creation" using ```MaxCircuitDirtiness NUM```[2] in the ```torrc``` which keeps a circuit "alive" for ```NUM``` seconds. 
6. Additionally `uTor` can be run as a function with Bento. 


## References

1. Bento 
2. Tor Manual (https://2019.www.torproject.org/docs/tor-manual.html.en)
3. Yang, Lei, and Fengjun Li. "mtor: A multipath tor routing beyond bandwidth throttling." 2015 IEEE Conference on Communications and Network Security (CNS). IEEE, 2015. (https://ieeexplore-ieee-org.ezproxy.lib.purdue.edu/stamp/stamp.jsp?tp=&arnumber=7346860)
4. https://metrics.torproject.org/bubbles.html#country-exits-only
5. Biryukov, Alex, Ivan Pustogarov, and Ralf-Philipp Weinmann. "Trawling for tor hidden services: Detection, measurement, deanonymization." 2013 IEEE Symposium on Security and Privacy. IEEE, 2013.
6. R. Jansen and N. Hopper, “Shadow: Running Tor in a Box for Accurate and Efficient Experimentation,” in Proceedings of the Network and Distributed System Security Symposium - NDSS’12, February 2012.
7. C. Tang and I. Goldberg, “An improved algorithm for Tor circuit scheduling,” in Proceedings of the 2010 ACM Conference on Computer and Communications Security (CCS 2010), October 2010.
