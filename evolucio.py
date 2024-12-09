import random
import string

objetivo="EVOLUCIO"
NProge=5
poblacion=[]
poblacio_score=[]
cont=[0]*len(objetivo)

for x in range(0, NProge):

    l=(random.choices(string.ascii_uppercase, k=len(objetivo)))
    cadena=''.join(l)
    poblacion.append(cadena)

for p in poblacion:
    resultat=0    
    for x in range(0, len(objetivo)):
        if(objetivo[x]==p[x]):
            resultat +=1

    lis=[p,resultat]
    poblacio_score.append(lis)

def funcord(e):
    return e[1]

poblacio_score.sort(reverse=True, key=funcord)
print(poblacio_score)
new=[]
for z in range(0, int(len(poblacio_score)/2)):
   new.append(poblacio_score[z][0])

index=random.randrange(0, len(poblacion))
p1=poblacion[index]
index=random.randrange(0, len(poblacion))
p2=poblacion[index]
descendiente=""
print(p1)
print(len(p1))
for x in range(0,len(p1)):
    if x%2==0:
        descendiente= descendiente + p1[x]
    else:
        descendiente = descendiente + p2[x]

print(p1,p2,descendiente)
