import numpy as np
from scipy.sparse import csr_matrix

import srmsvd

def srmculprits(u,s,vt,indegs,outdegs,rec_indegs, rec_outdegs):
    print("vt", vt)
    pcthresh = 1; #threshold value to identify suspicious users
    degthresh = 10; #minimum degree consideration
    print("indegs", indegs)
    # print(indegs[0,0])
    # print(indegs[0,1])
    # print(indegs.size)
    newIndegs = []
    for i in range(0, indegs.size):
        newIndegs.append(indegs[0, i])
    # print(newIndegs)
    newIndegs = np.array(newIndegs)
    # print(newIndegs)

    _, indices = np.unique(newIndegs, return_index=True)
    q = newIndegs[np.sort(indices)]
    lq = len(q)
    trackpct_indegs = csr_matrix((lq, 2), dtype=float).toarray()
    # print(trackpct_indegs)
    for i in range(0,lq):
        deg = q[i]
        trackpct_indegs[i][0] = deg
        indices = np.argwhere((indegs == deg))
        print("indices",indices)
        vtsub = vt[indices]
        print("vtsub", vtsub)
    # print(q)
    # print(trackpct_indegs)

srmculprits(*srmsvd.srmsvd('',3))