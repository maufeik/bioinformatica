import random

def cadena_random(largo_cadena):
 DNA=['A', 'T', 'C', 'G']
 cadena_rng=random.choices(DNA, k=largo_cadena)
 return cadena_rng

def conteo_de_cadena(secuencia):   
    conteo = {'A':0, 'T':0, 'C':0, 'G':0}                 
    for letra in secuencia:                      
        if(letra in conteo):
                conteo[letra]+=1         
    return conteo

def validar_cadena(secuencia):
 dna=('ATCG')
 for letra in secuencia:
    if letra in dna:
       return conteo_de_cadena(secuencia)
    else:
       print('Cadena invalida')
       break

def complemetar_cadena(cadena):
    cadena_nueva=[]
    for letra in cadena:
      if letra=='A':
        cadena_nueva.append('T')
      if letra=='T':
        cadena_nueva.append('A')
      if letra=='C':
        cadena_nueva.append('G')
      if letra=='G':
        cadena_nueva.append('C')
    return cadena_nueva

secuencia=cadena_random(40)
print(secuencia)
 
print(validar_cadena(secuencia))

print(complemetar_cadena(secuencia))
        
        
                  