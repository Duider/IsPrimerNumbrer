#Diferents ways of telling if a number is primer

'''def isPrimeNumber(num):
    
    if num % 2 != 0:
        if num % 3 !=0:
           if num % 5 !=0:
               if num % 5 !=0:
                 if num % 7 !=0:
                     return print("Es primo")
                 else:
                    return print("No es primo")
           else:
               return print("No es primo")
               
        else:
             return print("No es primo")
    else:
        return print("No es primo")

isPrimeNumber(907)
isPrimeNumber(820)
'''
'''
def isPrimeNumber(num):
    divs = [2,3,5,7]
    primo = True
    for div in divs:
        if num % div == 0:
            primo = False
    if primo == False:
        return print("No es primoo")
    else: 
        return print("Es primoo") 

isPrimeNumber(907)
isPrimeNumber(820)
'''
'''
def isPrimeNumber():
    divs = [2,3,5,7]
    primo = True
    num = int(input("Escribi un número: "))
    for div in divs:
        if num % div == 0:
            primo = False
    if primo == False:
        return print("No es primoo")
    else: 
        return print("Es primoo")

isPrimeNumber()

'''
def isPrimerNumber(num):
    cont=0
    i=2
    for i in range(2,int(num/2)+1):
        resto = num % i
        if resto ==0:
            cont+=1
            break
    if cont==0:
        return print("Es primoo")
    else: 
        return print("No es primoo")
    
isPrimerNumber(13)
