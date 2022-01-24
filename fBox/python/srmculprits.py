import numpy as np

import srmsvd

def srmculprits(u,s,vt,indegs,outdegs,rec_indegs, rec_outdegs):
    pcthresh = 1; #threshold value to identify suspicious users
    degthresh = 10; #minimum degree consideration
    print(indegs)
    print(indegs[0,0])
    print(indegs[0,1])
    print(indegs.size)
    newIndegs = []
    for i in range(0, indegs.size):
        newIndegs.append(indegs[0, i])
    print(newIndegs)
    q = np.unique(newIndegs, return_index=True)
    lq = len(q)
    print(q)



srmculprits(*srmsvd.srmsvd('',3))