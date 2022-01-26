import docplex.mp.model as cpx

#lors de l'importation des données, check /n avec strip

datapath = "example.txt"
file = open(datapath, mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
data = []
for line in lines:
    line = line.strip('\n')
    line = line.split(' ')
    data.append(line)
    #print(my_list)

#Dico { clé : int --> valeur : continuous_vars }
yDico = {}
#Liste des sommets : int
yTab = []
#Liste des arrêtes : continuous_vars (à maximiser)
xTab = []

#Definition du modele
m = cpx.Model(name='Detection Fraudes')

#Pour toutes les données on va 
# - créer les variables à maximiser
# - ajouter les contraintes
for i in range (len(data)):
    
    #On rempli la liste des arretes 
    xTab.append(m.continuous_var(lb = 0, name='x_{0}_{1}'.format(data[i][0],data[i][1]) ) )
    
    for j in range (len(data[i])):

        #Si on n'a pas encore vu le sommet alors on l'ajoute au dico et à la liste des sommets
        if data[i][j] not in yDico:
            #On ajoute dans le dico
            yDico[data[i][j]]=m.continuous_var(lb = 0, name='y_{0}'.format(data[i][j]) )
            #On ajoute à la liste des sommets
            yTab.append(data[i][j])
        
        #Contraintes : Le degré de suspicion des arrêtes doit etre inférieur à leurs 2 sommets respectifs.
        m.add_constraint(xTab[i] <= yDico[data[i][j]])

#Contrainte : la somme des degré de suspicions des sommets doit être inférieur à 1
m.add_constraint(m.sum(yDico.values()) <= 1)

m.maximize(m.sum(xTab))
m.print_information()
m.solve()
m.print_solution(print_zeros=True)