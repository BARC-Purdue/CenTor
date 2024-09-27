import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt




def textToCSV(filename):
  read_file = pd.read_csv(filename + ".txt")
  if len(read_file.columns) == 3:
    read_file.insert(loc=0, column="ID", value=10)
  read_file.columns = ['Thread ID', 'Time Stamp', 'Total to be downloaded', 'Downloaded']
  read_file.to_csv(filename + ".csv", index=None)
  return read_file

def preprocessData(dataFrame, decimals=3, deltaT = 0.001):
  ID = dataFrame['Thread ID'].unique()
  print("Thread ID: \n", ID)
  data = {}
  xnew = {}
  DD = []
  TT = []
  for i in range(len(ID)):
    df = dataFrame[dataFrame["Thread ID"] == ID[i]]
    df.pop('Thread ID')
    array = df.values
    array -= [array[0,0], 0, 0] 
    tt = np.round(array[-1,0], decimals=decimals) - deltaT
    TT.append(tt)
    DD.append(max(array[:, 1]))
    xnew["ID" + str(i)] = np.arange(0, TT[i], deltaT)
    data["ID" + str(i)] = array 
  TD = sum(DD)
  print("file sizes", DD)
  print("Total to be downloaded: ", TD)
  print("Total time: ", TT)
  print("\n")
  for i in range(len(ID)):
    data["ID" + str(i)] = data["ID" + str(i)] / [1, 1, TD]
  return xnew, data, TT

def interpolate_func(xnew, data):
  ynew = {}
  l = max(len(xnew["ID" + str(i)]) for i in range(len(xnew)))
  for i in range(len(xnew)):
    x = data["ID" + str(i)][:,0]
    y = data["ID" + str(i)][:,-1]
    f = interpolate.interp1d(x, y)
    y = f(xnew["ID" + str(i)])
    ynew["ynew" + str(i)] = np.pad(y, (0, l-len(y)), 'constant', constant_values=(0, y[-1]))
  return ynew

def result(ynew, TT, deltaT=0.001):
  out = sum(y for y in ynew.values())
  inp = np.arange(0, max(TT), deltaT)
  return inp, out

def generate_output(filenames, decimals=3, deltaT=0.001):
  OUT = []
  for fname in filenames:
    x, data, total_time = preprocessData(dataFrame=textToCSV(fname), decimals=decimals, deltaT=deltaT)
    y = interpolate_func(xnew=x, data=data)
    xData, yData = result(y, total_time, deltaT=deltaT)
    OUT.append(yData)
  return OUT, total_time


# ----------------------------------------------


fnames = ["5Tor", "3Tor", "2Tor", "5Tor*", "3Tor*", "2Tor*", "sTor"]


y, TT = generate_output(filenames=fnames, decimals=4, deltaT=10e-4)

maxT = max([len(i) for i in y])
maxT = int(np.ceil(maxT/10000)*10000)
xInp = np.arange(0, maxT*0.001, 0.001)
yOut = []

for i in range(len(fnames)):
    yOut.append(np.pad(y[i], (0, maxT-len(y[i])), 'constant', constant_values=(0, 1)))

plt.figure(figsize=(8, 4))

plt.plot(xInp, yOut[0], linestyle = 'dashed')
plt.plot(xInp, yOut[1], linestyle = 'dashed')
plt.plot(xInp, yOut[2], linestyle = 'dashed')
plt.plot(xInp, yOut[3])
plt.plot(xInp, yOut[4])
plt.plot(xInp, yOut[5])
plt.plot(xInp, yOut[6], linestyle = 'dashdot')


plt.legend(fnames, loc='lower right', fontsize=14)
plt.grid()
plt.xlabel("Download Time (s)", fontsize=14)
plt.ylabel("Cumulative Fraction", fontsize=14)
plt.xlim([0, 40])
plt.ylim([0, 1.1])



