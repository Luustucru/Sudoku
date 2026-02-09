'''
------------------------------------------------------------------------------------------------------------------------------
Liste des choses à faire:

- Modifier la partie bloc de singletons_nus 

-------------------------------------------------------------------------------------------------------------------------------
Pour les techniques à coder faut aller sur https://sudoku.com/fr/regles-du-sudoku/
On va prendre les memes noms que dessus.

Les methodes sont:
- Derniere case libre - Finie mais a verifier
- Derniere case restante  - Finie mais a verifier 
- Dernier chiffre possible (marche comme Derniere case libre)  - Finie mais a verifier
- Singletons nus - PL travaille dessus
- Paires nues
- Triplets nus
- Singletons caches
- Paires cachees 
- Triplets cachees
- Paires pointantes
- Triplets pointants
- X-wing
- Y-Wing
- Swordfish


Dans la suite les lignes sont les lignes des listes S1,S2...
Les colonnes sont les colonnes des listes S1,S2...
Et les blocs sont numérotés comme ca :

0  |  1  |  2
--------------
3  |  4  |  5
--------------
6  |  7  |  8
   

Aussi, pour ne pas avoir a raffraichir la grille des possibles entre chaque methode effectuee, 
il faudrait que la methode la mette a jour si quelque chose a ete modifie

-------------------------------------------------------------------------------------------------------------------------------
IMPORTANT !!!
Il faut changer les methodes pour faire les memes que sur le site
Comme ca tout est visible et clair
-------------------------------------------------------------------------------------------------------------------------------
'''


# Liste des Sudokus

S1=[[1,2,3,4,5,6,7,8,9],# Sudoku entier de base
    [9,1,2,3,4,5,6,7,8],
    [8,9,1,2,3,4,5,6,7],
    [7,8,9,1,2,3,4,5,6],
    [6,7,8,9,1,2,3,4,5],
    [5,6,7,8,9,1,2,3,4],
    [4,5,6,7,8,9,1,2,3],
    [3,4,5,6,7,8,9,1,2],
    [2,3,4,5,6,7,8,9,1]]

S2=[[8,1,3,9,2,5,7,4,6],# Sudoku entier normal 
    [9,5,6,8,4,7,3,1,2],
    [4,7,2,3,6,1,8,9,5],
    [6,2,4,7,1,9,5,3,8],
    [7,9,5,6,3,8,4,2,1],
    [3,8,1,4,5,2,9,6,7],
    [2,3,8,1,7,4,6,5,9],
    [5,4,9,2,8,6,1,7,3],
    [1,6,7,5,9,3,2,8,4]]

S3=[[0,0,0,9,2,5,7,4,6], # Sudoku S2 mais avec le bloc 1 en moins
    [0,0,0,8,4,7,3,1,2],
    [0,0,0,3,6,1,8,9,5],
    [6,2,4,7,1,9,5,3,8],
    [7,9,5,6,3,8,4,2,1],
    [3,8,1,4,5,2,9,6,7],
    [2,3,8,1,7,4,6,5,9],
    [5,4,9,2,8,6,1,7,3],
    [1,6,7,5,9,3,2,8,4]]

S4=[[2,1,3,5,9,7,0,6,0], # Grille de niveau primaire
    [7,0,6,0,8,1,3,2,5],
    [0,5,4,3,0,6,9,1,7],
    [9,4,2,6,0,8,7,0,0],
    [6,3,0,1,7,0,0,4,2],
    [1,7,8,2,3,4,5,9,6],
    [5,6,1,8,0,3,0,7,9],
    [3,0,9,7,6,2,1,5,0],
    [0,2,7,0,7,5,6,8,3]]

S5=[[0,0,0,0,5,7,0,4,0], # Grille niveau facile
    [2,0,4,6,0,8,9,0,0],
    [5,8,9,2,0,4,0,7,1],
    [0,0,7,3,6,5,1,0,0],
    [6,0,2,1,0,9,4,0,7],
    [0,0,3,7,4,2,8,0,0],
    [9,3,0,8,0,1,5,2,4],
    [0,0,8,5,0,3,7,0,6],
    [0,1,0,4,2,0,0,0,0]]

S6=[[2,5,3,0,0,6,0,1,0], # Grille niveau facile
    [9,0,0,5,0,7,2,0,0],
    [0,0,4,1,2,0,0,0,6],
    [7,0,0,0,0,0,9,4,0],
    [6,0,0,0,0,0,0,0,5],
    [0,8,1,0,0,0,0,0,2],
    [1,0,0,0,6,5,8,0,0],
    [0,0,8,7,0,4,0,0,1],
    [0,6,0,8,0,0,3,7,9]]

S7=[[2,0,0,0,0,9,0,0,0], # Gille un peu plus dure
    [0,9,0,5,0,0,0,6,0],
    [8,1,5,0,7,0,9,0,0],
    [1,0,0,0,6,7,0,9,0],
    [9,0,0,4,5,0,0,0,2],
    [0,3,0,0,0,0,0,0,8],
    [0,5,0,0,0,0,8,2,0],
    [4,0,0,0,0,0,0,1,6],
    [3,0,0,2,0,0,0,0,7]]

S8=[[1,2,3,4,5,6,7,8,0], # Gille de tests
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

class Sudoku:
    def __init__(self,sudoku):
        self.S=sudoku # La grille
        # Pour chaque place vide de la grille, on cherche les nombres possibles. On les met dans la liste self.P
        self.P =   [[[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]]]
    
    def affiche(self): # Affiche la grille de maniere lisible dans la console
        for k in range(2):
            for i in range(3):
                for j in range(2):
                    print(self.S[i+3*k][3*j], self.S[i+3*k][3*j+1], self.S[i+3*k][3*j+2], "| ",end='')
                print(self.S[i+3*k][6], self.S[i+3*k][7], self.S[i+3*k][8])
            print('-'*21)
        for i in range(3):
                for j in range(2):
                    print(self.S[i+6][3*j], self.S[i+6][3*j+1], self.S[i+6][3*j+2], "| ",end='')
                print(self.S[i+6][6], self.S[i+6][7], self.S[i+6][8])
        
    def ligne(self,n): # Renvoie la ligne n de la grille
        return self.S[n]
    
    def ligneP(self,n): # Renvoie la ligne n de la grille des possibles
        return self.P[n]
    
    def colonne(self,n): # Renvoie la colonne n de la grille
        colonne=[]
        for i in range(9):
            colonne.append(self.S[i][n])
        return colonne
    
    def colonneP(self,n): # Renvoie la colonne n de la grille des possibles
        colonne=[]
        for i in range(9):
            colonne.append(self.P[i][n])
        return colonne
   
    def bloc(self,n): # renvoie le bloc n de la grille
        y=n//3
        x=n%3
        bloc=[[],[],[]]
        for i in range(3):
            bloc[i].extend(self.S[3*y+i][3*x:3*x+3])
        return bloc
    
    def blocP(self,n): # renvoie le bloc n de la grille des possibles
        y=n//3
        x=n%3
        bloc=[[],[],[]]
        for i in range(3):
            bloc[i].extend(self.P[3*y+i][3*x:3*x+3])
        return bloc
    
    def numero_du_bloc(self,ligne,colonne):
        '''on entre la ligne et la colonne d'une case et il nous renvoie
        le numero de son bloc'''
        return ((ligne//3)*3+(colonne//3))
    
    def est_finie(self): # nous dit si la grille self.S est remplie
        for i in range(9):
            for j in range(9):
                if self.S[i][j]==0:
                    return False
        return True
    

# Les methodes


    def grille_des_possibles(self): # Remplit la grille des possibles pour chaque case vide
        self.P =   [[[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]],
                    [[],[],[],[],[],[],[],[],[]]]
        for i in range(9):
            for j in range(9):
                if self.S[i][j] == 0:
                    Nombres_impossibles=list(set(self.ligne(i)+self.colonne(j)+[nb for sublist in self.bloc(self.numero_du_bloc(i,j)) for nb in sublist]))
                    for k in range(10):
                        if k not in Nombres_impossibles :
                            self.P[i][j].append(k)
    
    def derniere_case_libre(self): # Correspond aussi a la methode Dernier chiffre possible
        """Si il n'y a qu'une possibilite dans une case, elle remplit la grille avec ce chiffre"""
        for i in range(9):
            for j in range(9):
                if len(self.P[i][j]) == 1:
                    self.S[i][j]=self.P[i][j].pop()

    def derniere_case_restante(self):
        """Cherche si un chiffre est possible que dans une seule case d'une ligne,
        d'une colonne ou d'un bloc."""
        for i in range(9):
            ligne=self.ligneP(i) # Cherche dans la ligne
            NbP={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # dico du nombre de fois qu'un nombre est possible dans la ligne
            LastP={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # dico de la derniere occurence de chaque nombre dans la ligne
            for j in range(9):
               for element in ligne[j]:
                    NbP[element]+=1
                    LastP[element]=j
            valeur = [k  for (k, val) in NbP.items() if val == 1] # Renvoie les chiffres possibles qu'une fois dans la ligne
            for nombre in valeur:
                self.S[i][LastP[nombre]]=nombre # Remplit la grille
                self.P[i][LastP[nombre]]=[] # Vide la case dans la grille des possibles
        for i in range(9):
            colonne=self.colonneP(i) # Cherche dans la colonne
            NbP={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # dico du nombre de fois qu'un nombre est possible dans la colonne
            LastP={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # dico de la derniere occurence de chaque nombre dans la colonne
            for j in range(9):
                for element in colonne[j]:
                    NbP[element]+=1
                    LastP[element]=j
            valeur = [k  for (k, val) in NbP.items() if val == 1] # Renvoie les chiffres possibles qu'une fois dans la colonne
            for nombre in valeur:
                self.S[LastP[nombre]][i]=nombre # Remplit la grille
                self.P[LastP[nombre]][i]=[] # Vide la case dans la grille des possibles
        for i in range(9):
            bloc=self.blocP(i) # Cherche dans le bloc
            NbP={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # dico du nombre de fois qu'un nombre est possible dans le bloc
            LastP={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} # dico de la derniere occurence de chaque nombre dans le bloc
            for j in range(3):
                for p in range(3):
                    for element in bloc[j][p]:
                        NbP[element]+=1
                        LastP[element]=(j,p)
            valeur = [k  for (k, val) in NbP.items() if val == 1] # Renvoie les chiffres possibles qu'une fois dans le bloc
            for nombre in valeur:
                self.S[3*(i//3)+LastP[nombre][0]][3*(i%3)+LastP[nombre][1]]=nombre # Remplit la grille
                self.S[3*(i//3)+LastP[nombre][0]][3*(i%3)+LastP[nombre][1]]=[]  # Vide la case dans la grille des possibles

    def singletons_nus(self): 
        for i in range(9): 
            Ligne=self.ligneP(i) # Analyse des lignes de self.P
            for j in range(9):
                for k in range(9):
                    if Ligne[j]==Ligne[k] and j!=k and len(Ligne[j])==2:
                        Paire=Ligne[j]
                        for nombre in Paire:
                            for a in range(9):
                                if nombre in Ligne[a] and a!=k and a!=j:
                                    self.P[i][a].remove(nombre)
            Colonne=self.colonneP(i) # Analyse des colonnes de self.P
            for j in range(9):
                for k in range(9):
                    if Colonne[j]==Colonne[k] and j!=k and len(Colonne[j])==2:
                        Paire=Colonne[j]
                        for nombre in Paire:
                            for a in range(9):
                                if nombre in Colonne[a]  and a!=k and a!=j:
                                    self.P[a][i].remove(nombre)
            Bloc=self.blocP(i) # À modifier
            for j in range(9):
                for k in range(9):
                    if Bloc[j//3][j%3]==Bloc[k//3][k%3] and (j//3!=k//3 and j%3!=k%3) and len(Bloc[j//3])==2:
                        Paire=Bloc[j//3][j%3]
                        for nombre in Paire:
                            for b in range(9):
                                if nombre in Bloc[b//3][b%3] and Bloc[b//3][b%3]!=Bloc[j//3][j%3] and Bloc[b//3][b%3]!=Bloc[k//3][k%3]:
                                    self.P[(i//3)*3+b//3][(i%3)*3+b%3].remove(nombre)



    def npt(self): # Il faut modifier celle la - On la supprime pas au cas ou mais il faudrait la copier/coller et la modifier
        for i in range(9): 
            Ligne=self.ligneP(i) # Analyse des lignes de self.P
            for j in range(9):
                for k in range(9):
                    if Ligne[j]==Ligne[k] and j!=k and (len(Ligne[j])==2 or len(Ligne[j])==3):
                        PairOrTriple=Ligne[j]
                        for nombre in PairOrTriple:
                            for a in range(9):
                                if nombre in Ligne[a] and Ligne[a]!=Ligne[k] and Ligne[a]!=Ligne[j]:
                                    self.P[i][a].remove(nombre)
            Colonne=self.colonneP(i) # Analyse des colonnes de self.P
            for j in range(9):
                for k in range(9):
                    if Colonne[j]==Colonne[k] and j!=k and (len(Colonne[j])==2 or len(Colonne[j])==3):
                        PairOrTriple=Colonne[j]
                        for nombre in PairOrTriple:
                            for a in range(9):
                                if nombre in Colonne[a]  and Colonne[a]!=Colonne[k] and Colonne[a]!=Colonne[j]:
                                    self.P[a][i].remove(nombre)
            Bloc=self.blocP(i) # Analyse des blocs de self.P
            for j in range(9):
                for k in range(3):
                    for p in range(3):
                        if Bloc[j//3][j%3]==Bloc[k][p] and j//3!=k and j%3!=p and (len(Bloc[j//3])==2 or len(Bloc[j%3])==3):
                            PairOrTriple=Bloc[j//3][j%3]
                            for nombre in PairOrTriple:
                                for b in range(3):
                                    for c in range(3):
                                        if nombre in Bloc[b][c] and Bloc[b][c]!=Bloc[j//3][j%3]:
                                            self.P[i][(i%3)*3+b].remove(nombre)
                            

                

                    
        
 
S1=Sudoku(S1)
S2=Sudoku(S2)
S3=Sudoku(S3)
S4=Sudoku(S4)
S5=Sudoku(S5)
S6=Sudoku(S6)
S7=Sudoku(S7)
S8=Sudoku(S8)


# Les tests


        






