#Autor:  
#Matricula:
#
A = set([1,2,3,4,5]) 
B = set([3,4,5,6,7]) 
C = {}

#
#
def pertenencia():
    A = set([1,2,3,4,5]) 
    1 in A
    1 not in A 
    10 in A 
    10 not in A 
    
#
#
def transformarConj():
    A = (1,2,3)
    conjuntoA = set (A) 
    print("The set is:", conjuntoA)
    B={1,2,3,4,5}
    conjuntoB = set (B)
    print("The set B is : ", conjuntoB)
    C='Hola mundo'
    conjuntoC = set (C)
    print("The set C is :", conjuntoC)

#
#
def quitar():
    A = set([0,1,2,3,4,5]) 
    A.discard(2)
    print("The set after to delete: ", A)

#
def clearSet():
    A = set([0,1,2,3,4,5]) 
    A.clear() 
    print("The set clear: ", A)


#
def copiar():
    A = set([1,2,3,4,5]) 
    B=A.copy() 
    print("Set A = ", A, " compare set B = ", B)

#
def agregar():
    B.add(987) 
    print("The new set B = ", B) 

#
def union():
    A = set([1,2,3,4,5]) 
    B = set([3,4,5,6,7]) 
    print("The union = ", A|B) 
    print("The union = ", A.union(B))
#
#
def intereseccion():
    A = set([1,2,3,4,5]) 
    B = set([3,4,5,6,7]) 
    print("The intersection = ", A&B)
    print(A.intersection(B))

#
#
def diferencia():
    A = set([1,2,3,4,5]) 
    B = set([3,4,5,6,7]) 
    print("The diference = ", A-B)
    print("The intersection = ", A.difference(B))

#
#
def simetrica():
    A = set([1,2,3,4,5]) 
    B = set([3,4,5,6,7]) 
    C = {}
    print("The symmetric_difference = ", A^B)
    
    print("The symmetric_difference = ",A.symmetric_difference(B))
    print("The symmetric_difference = ",B.symmetric_difference(A))
    print("The symmetric_difference = ",A.symmetric_difference(C))
    print("The symmetric_difference = ",B.symmetric_difference(C))

#
#
def subconjunto():
    B = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    A = set([1,2,3,4,5]) 
    print("The subset = ",A.issubset(B)) 
    print("The subset = ",B.issubset(A))

#
#
def superconjunto():
    B = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    A = set([1,2,3,4,5])
    print("The superset = ",B.issuperset(A))
    print("The supersrt = ",A.issuperset(B)) 


