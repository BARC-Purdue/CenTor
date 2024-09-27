# https://colab.research.google.com/drive/1GnkIJ5XpNOxO-gVcWZ6gTgIiimobirBt?usp=sharing
# plot to calculate probability of compromise

from scipy.stats import binom
from scipy.special import comb
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# f_gbw, f_xbw = 0.0263, 0.0447

def P_compromised(g, f_gbw, network=1):
  m = g
  P_a = lambda a: binom(g, f_gbw).pmf(a)
  def P_comp_given_a(a, f_xbw=1):
    if m >= g:
      return f_xbw*(1-comb(g-a, g))
    return f_xbw*(1 - comb(g-a, m)/comb(g, m))

  P_comp_B = sum(P_a(a)*P_comp_given_a(a, f_xbw=0.2) for a in range(g+1))
  if network==1:
    return P_comp_B
  elif network==2: 
    P_comp_A_given_B_comp = sum(P_a(a)*P_comp_given_a(a) for a in range(g+1))
    return P_comp_B * P_comp_A_given_B_comp
  else:
    raise Exception("Invalid network input..")

p = defaultdict(list)
q = defaultdict(list)
f_gbw = np.linspace(0, 1.0, 50)
for g in range(1, 6):
  for f_g in f_gbw:
    p[g].append(P_compromised(g, f_g, network=2))
    q[g].append(P_compromised(g, f_g))


color = { 1: "indigo", 2: "blue", 3: "limegreen", 4: "gold", 5: "orangered"}
plt.figure(figsize=(10, 10))
for g in p.keys():
    plt.plot(f_gbw, p[g], c=color[g], label=f"{g}Tor*")
    plt.plot(f_gbw, q[g], "--", c=color[g], label=f"{g}Tor")
plt.legend(loc=4, fontsize=12)
plt.xlabel("Faction of Adversary Guard Bandwidth", fontsize=14)
plt.ylabel("Probability of Compromise", fontsize=14)
plt.xlim([0,1])
plt.ylim([0,0.21])
plt.show()