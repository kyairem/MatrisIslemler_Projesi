import random
print(50*"*")
print("1. TOPLAMA\n2. CIKARMA\n3.CARPMA\n"+50*"*")
secim=int(input("Lutfen Secimizi Yapiniz:"))
liste=[1,2,3,4,5,6,7,8,9]
a=[[random.choice(liste),random.choice(liste),random.choice(liste)],[random.choice(liste),random.choice(liste),random.choice(liste)]]
b=[[random.choice(liste),random.choice(liste),random.choice(liste)],[random.choice(liste),random.choice(liste),random.choice(liste)]]
print("A matrisi:{}".format(a))
print("B matrisi:{}".format(b))
c=[[0,0,0],[0,0,0]]
for i in range(0,2):
    for j in range(0,3):
        if secim==1:
            c[i][j]=a[i][j]+b[i][j]
        elif secim==2:
            c[i][j]=a[i][j]-b[i][j]
        elif secim==3:
            c[i][j] = a[i][j] * b[i][j]
        else:
            print("........... YANLIS SECIM YAPTINIZ ...........")
print("YAPMIS OLDUGUNUZ SECİM SONUCU OLUSAN MATRİS:",end=" ")
for i in c:
    print(i,end=" ")