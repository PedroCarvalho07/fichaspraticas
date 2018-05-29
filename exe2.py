import random

file = open("teste.txt", "r") 
lista = [] 
linhas = file.readlines()

def sort(lista):
    if len(lista) > 1:
        mid = int(len(lista)/2)
        left = lista[:mid]
        right = lista[mid:]
        # Split
        sort(left)
        sort(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

for i in linhas:
    i = int(i.split("\n")[0])
    lista.append(i)

sort(lista)   
print(lista)


for i in range(len(lista)-1, -1, -1):
    print(lista[i], end= " ,")
   

file.close()







