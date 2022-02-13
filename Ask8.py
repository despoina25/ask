import random
T=[[],[],[],[],[],[],[],[]]
for i in range(8):
    for j in range(8):
        T[i].append(0)
R=[[8,8],[7,7],[7,8]]


for session in range (3):
    p1=0
    p2=0
    for game in range(100):
        for i in range(8):
            for j in range(8):
                T[i][j]=0
        #Παίκτης 1:π΄ύργος
        while(True):
            r1 = random.randint(0, R[session][0]-1)
            c1 = random.randint(0, R[session][1]-1)
            if(T[r1][c1]==0):
                break
        #Εμφανίζει("rook row:",r1,"col:",c1)
        T[r1][c1]="R"
        #Παίτης 2:αξιωματικός
        while(True):
            r2 = random.randint(0, R[session][0]-1)
            c2 = random.randint(0, R[session][1]-1)
            if(T[r2][c2]==0):
                break
        #Εμφανίζει("bishop row:",r2,"col:",c2)
        T[r2][c2]="B"
        hit1=0
        for i in range(7):
            if(T[r1][i]=="B" or T[i][c1]=="B"):
                hit1=1
        hit2=0
        j=1
        while(r2-j>=0 and c2-j>=0):
            if(T[r2-j][c2-j]=="R"):
                hit2=1
            j+=1
        j=1
        while(r2-j>=0 and c2+j<=7):
            if(T[r2-j][c2+j]=="R"):
                hit2=1
            j+=1
        j=1
        while(r2+j<=7 and c2-j>=0):
            if(T[r2+j][c2-j]=="R"):
                hit2=1
            j+=1
        j=1
        while(r2+j<=7 and c2+j<=7):
            if(T[r2+j][c2+j]=="R"):
                hit2=1
            j+=1


        if(hit1==1):
            print("Παιχνίδι:",game+1,"κέρδισε ο πύργος")
            p1+=1
        elif(hit2==1):
            print("Παιχνίδι:",game+1,"κέρδισε ο αξιωματικός")
            p2+=1
        else:
            print("Παiχνίδι:",game+1,"ισοπαλία")

    print("Παιχνίδι:",session+1,"Μέγεθος σκακιέρας:",R[session][0],"X",R[session][1])
    print("Παίκτης 1:0 πύργος κέρδισε: ",p1,"φορές")
    print("Παίκτης 2:0 αξιωματικός κέρδισε: ",p2,"φορές")
    print("Το παιχνίδι ήρθε σε ισοπαλία: ",100-p1-p2,"φορές")
