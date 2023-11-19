import numpy as np
import os

source="npy"
target="csv"

files=os.listdir(source)

for f in files:
    data=np.load(source+"/"+f)
    np.savetxt(target+"/"+f[:-3]+"csv",data,delimiter=",")
