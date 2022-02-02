'''#2.uzd
import mod
n= []
n.append(int(input("ievadi 1. skaitli: ")))
n.append(int(input("ievadi 2. skaitli: ")))
x=int(input("kuru virknes n elementu vēlies noskaidrot?: "))

rez= mod.elem(n,x)
print(f"virknes {x}. elements ir:", n[x-1])

print(" ")'''


#3.uzd
skaitlis= str(input("ievadi skaitli: "))
summ=int(skaitlis)
count=0

while(summ>0):
    count=count+1
    summ=summ//10
if (count>100):
  print("parak liels skaitlis:",count,"didžiti. ievadi skaitli zem 100 didžitiem" )

s=0
for i in range(len(skaitlis)):
  a=(skaitlis[i:])
  print(a)

#viss strādā, vienīgi neizdodas uzrakstīt koda daļu, kur šos skaitļus saskaita. Nesaprotu, kuru jāizmanto, int vai str.