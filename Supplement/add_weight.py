import random
import sys


for nom_fichier in (sys.argv[1:]):

    f = open(nom_fichier,"r")
    lines = f.readlines()
    f.close()

    f = open(nom_fichier,"w")
    for line in lines:
        rand= str(random.random())
        line = line.rstrip("\n")+" "+rand+"\n"
        f.write(line)
    f.close()
