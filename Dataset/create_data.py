import random
import sys

def run(nom_fichier, n):
    data= {}

    for follower in range(1,n+1):
        follows= []


        for followee in range(1,n+1):
            if not(random.randint(0,2)):
                follows.append(followee)


        follows.sort()
        data[follower] = follows

    f = open(nom_fichier,"w")
    for follower in data:
        for followee in data[follower]:
            line = str(follower)+" "+str(followee)+"\n"
            f.write(line)
            line=""
    f.close()


if len(sys.argv)==3:
    nom_fichier= sys.argv[1]
    n= int(sys.argv[2])

    print(str(sys.argv))
    print("nom",nom_fichier)
    print("n",n)

    run(nom_fichier, n)
