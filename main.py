import mod
n= []
n.append(int(input("ievadi 1. skaitli: ")))
n.append(int(input("ievadi 2. skaitli: ")))
x=int(input("kuru virknes n elementu vēlies noskaidrot?: "))

rez= mod.elem(n,x)
print(f"virknes {x}. elements ir:", n[x-1])