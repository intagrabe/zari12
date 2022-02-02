#2.uzdevums

""" a1=int(input("ievadi pirmo skaitli: "))
a2=int(input("ievadi otro skaitli: "))
n=int(input("ievadi kopējo skaitļu daudzumu: "))
sar=[]
sar.append(a1)
sar.append(a2)
for i in range (1, n-1):
  summa=sar[i-1] + sar[i]
  pedejais=summa%10
  sar.append(pedejais)
  
  print(pedejais)
rez=sar[n-1]
print(f"pēdējais cipars n elementam ir {rez}") """


#Uz papīra lapas tika uzrakstīts naturāls skaitlis, kura visi cipari bija lielāki par 0. Skaitlim bija ne vairāk kā 100 cipari. Pēc tam zem šī skaitļa stabiņā tika uzrakstīti skaitļi, kā redzams paraugā šeit: Beigās visi skaitļi tika saskaitīti.
#Piemērs, ievaddati 7231493, izvaddati 7496561.

skaitlis=int(input("ievadi naturālu skaitli, kura visi cipari ir lielāki par 0, ne vairāk kā 100 cipari kopā: "))
sar=[]
sar.append(skaitlis)
kopa=0
for i in range(len(sar),0,-1):
  sar= sar[:1]
  print(nonem)
  sar.append(nonem)
  print(nonem)





"""skaitlis=int(input("ievadi naturālu skaitli, kura visi cipari ir lielāki par 0, ne vairāk kā 100 cipari kopā: "))
sar=[]
sar.append(skaitlis)
kopa=0
for i in range(len(sar),0,-1):
  a=skaitlis%10**i
  sar.append(a)
  print(a)
for i in sar:
  kopa+=i
  print(sar)
print(kopa)
print(skaitlis)"""