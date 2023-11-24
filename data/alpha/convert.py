import numpy as np
import os

source="npy" # source directory
target="csv" # target directory

files=os.listdir(source) # list all files

# iterate through each file in the files list
for f in files:
    # load data from .npy file
    data=np.load(source+"/"+f)
    # save data to target directory, extracts filename without the last 3 characters (removing ".npy")
    # and appends the "csv" extension to the filename.
    np.savetxt(target+"/"+f[:-3]+"csv",data,delimiter=",")
