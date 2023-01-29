import random
import time

def buborek(array,arrayLength):#Buborék elrendezés
    start=time.time()
    jHason=0
    iHason=0
    for i in range(0,arrayLength):
        print(f'{i+1}. {array}')
        iHason+=1
        for j in range(arrayLength-1,i,-1):
            jHason+=1
            if array[j-1]>array[j]:
                seged=array[j-1]
                array[j-1]=array[j]
                array[j]=seged
    end=time.time()
    print(f'{array} - Összhasonlítás=> {jHason+iHason} - {(end-start)*10**3}')

def PreOrder():
    print("Közép,Bal részfa, Jobb részfa")

binaryTreeListOne=[]
binaryTreeListTwo=[]
seged=[]

bTLO=4
bTLT=6

for i in range(bTLO):
    binaryTreeListOne.append(random.randint(0,1000))

for i in range(bTLT):
    binaryTreeListTwo.append(random.randint(0,1000))

print('Bináris keresőfa\n\tPRE-ORDER ("KBJ")=>Csúcs, Bal részfa, Jobb részfa\n\tIN-ORDER ("BKJ")=> Bal részfa, Csúcs, Jobb részfa\n\tPOST-ORDER ("BJK")=> Bal részfa, Jobb részfa, Csúcs',end='\n\n')
print(binaryTreeListOne,end='\t')
print(binaryTreeListTwo)
seged.extend(binaryTreeListTwo)
seged.extend(binaryTreeListOne)
arange=buborek(seged,bTLO+bTLT)