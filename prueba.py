import random



def cadenaRng (largoCadena):
    adn = ["A", "T", "C", "G"]
    cadenaRandom = random.choices(adn, k=largoCadena)
    return cadenaRandom

def contSecuencia (secuencia):
    conteo={'A':0, 'T':0, 'C':0, 'G':0}
    for sec in secuencia:
        if sec in secuencia:
            conteo[sec]+=1
    return conteo

def validacionCadena(secuencia):
    adn=['A','T','C','G']

    for letra in secuencia:
        if letra not in adn: mensaje="Cadena incorrecta"
        else: mensaje="Cadena correcta"
    return print(mensaje)

def cadenaComplementaria (secuencia):
    cadenaComplementaria=[]

    for letra in secuencia:
        if letra == 'A':
            cadenaComplementaria.append('T')
        if letra == 'T':
            cadenaComplementaria.append('A')
        if letra == 'C':
            cadenaComplementaria.append('G')
        if letra == 'G':
            cadenaComplementaria.append('C')        

    return cadenaComplementaria

def invertirCadena (secuencia):
    return print(secuencia[::-1])

def invertirCadenaCompl (secuencia):
    cadenainvertida = secuencia[::-1]
    cadenaComplementaria=[]
    for letra in cadenainvertida:
        if letra == 'A':
            cadenaComplementaria.append('T')
        if letra == 'T':
            cadenaComplementaria.append('A')
        if letra == 'C':
            cadenaComplementaria.append('G')
        if letra == 'G':
            cadenaComplementaria.append('C')
    return cadenaComplementaria
        
def palindromo (secuencia):
    if secuencia == invertirCadena(secuencia):
        print('Si es palindromo')
    else: print('No lo es')

def calcularPorcentajeCG (secuencia):
    contC=0
    contG=0
    for letra in secuencia:
        if letra == 'C': contC+=1
        if letra == 'G': contG+=1    
    porcentajeG = (contG/len(secuencia))*100
    porcentajeC = (contC/len(secuencia))*100
    mensaje = 'El porcentaje de G es: '+str(porcentajeG) + '. El porcentaje de C es: '+str(porcentajeC)
    return mensaje
    
def porcentajeTotal (secuencia):
    contC=0
    contG=0
    contA=0
    contT=0
    for letra in secuencia:
        if letra == 'C': contC+=1
        if letra == 'G': contG+=1   
        if letra == 'A': contA+=1
        if letra == 'T': contT+=1         
    porcentajeG = (contG/len(secuencia))*100
    porcentajeC = (contC/len(secuencia))*100    
    porcentajeA = (contA/len(secuencia))*100
    porcentajeT = (contT/len(secuencia))*100
    mensaje = 'El porcentaje de G es: '+str(porcentajeG) + '. El porcentaje de C es: '+str(porcentajeC)+ '. El porcentaje de A es: '+str(porcentajeA)+ '. El porcentaje de T es: '+str(porcentajeT)
    return mensaje


secuencia= cadenaRng(4)
print(secuencia)
print(contSecuencia(secuencia))
validacionCadena(secuencia)
print(cadenaComplementaria(secuencia))
invertirCadena(secuencia)
palindromo(secuencia)
print(calcularPorcentajeCG(secuencia))
print(porcentajeTotal(secuencia))