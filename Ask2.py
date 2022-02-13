import random
T=[[],[],[]]
for i in range(3):
    for j in range(3):
        T[i].append(0)
p=[]
for i in range(3):
  p.append(0)
totalsteps=0
for game in range(100):
    for i in range(3):
        p[i]=0
        for j in range(3):
            T[i][j]=0
    steps=0
    while(True):
        while(True):
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            item = random.randint(1, 3)
            #Εμφανίζει("row:",r,"col:",c,"item:",item)
            if(T[r][c]<item and p[item-1]<9):
                break
        T[r][c]=item
        p[item-1]+=1
        steps+=1
        #ελέγχει για νίκη
        if(T[0][0]!=0 and T[0][0]==T[0][1] and T[0][1]==T[0][2]):
            break
        elif (T[1][0]!=0 and T[1][0]==T[1][1] and T[1][1]==T[1][2]):
            break
        elif (T[2][0]!=0 and T[2][0]==T[2][1] and T[2][1]==T[2][2]):
            break
        elif (T[0][0]!=0 and T[0][0]==T[1][0] and T[1][0]==T[2][0]):
            break
        elif (T[0][1]!=0 and T[0][1]==T[1][1] and T[1][1]==T[2][1]):
            break
        elif (T[0][2]!=0 and T[0][2]==T[1][2] and T[1][2]==T[2][2]):
            break
        elif (T[0][2]!=0 and T[0][2]==T[1][1] and T[1][1]==T[2][0]):
            break
        elif (T[0][0]!=0 and T[0][0]==T[1][1] and T[1][1]==T[2][2]):
            break
    totalsteps+=steps
    print("Παιχνίδι:",game+1,'Το παιχνίδι τελείωσε σε :',steps,'βήματα')
    for i in range(3):
        print(T[i])
avgsteps=totalsteps/100.0
print("Μέσος όρος βημάτων:",avgsteps)
