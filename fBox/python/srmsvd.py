
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds, eigs

def srmsvd(datapath, neigs):
    A = np.matrix([[1, 0, 0,-5], [5, 0, 2,2], [0, -1, 0,3], [0, 0, 3,0]], dtype=float)

    u, s, vt = svds(A, k=neigs, which='LM')
    indegs = np.sum(A, axis=0)
    outdegs = np.sum(A, axis=1)
    #print(s,vt)
    #print(A)
    #print(indegs.shape)
    #print(test)
    #print(outdegs)
    #print(outdegs)
    #rec_indegs = np.sum(pow(vt*s,2), axis=1)
    rec_indegs = []
    for i in range(0,len(s)):
        temp = 0
        for j in range(0,len(vt[0])):
            temp = pow(vt[i][j]*s[i],2)
        rec_indegs.append(temp)
    #rec_outdegs = np.sum(pow(u*s,2), axis=1)

    rec_outdegs = []
    for i in range(0,len(s)):
        temp = 0
        for j in range(0,len(u[0])):
            temp = pow(u[i][j]*s[i],2)
        rec_outdegs.append(temp)
    #print(rec_indegs)
    #print(rec_outdegs)
    return u,s,vt,indegs,outdegs,rec_indegs, rec_outdegs

srmsvd('', 3)