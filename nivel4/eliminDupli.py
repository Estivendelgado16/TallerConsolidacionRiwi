frutas = ["Apple","Orange","Strawberry"]

newElem = input("Ingrese nuevo elemento: ")




listNew = []

for elem in frutas:
    if elem not in listNew:
        listNew.append(elem)

print(listNew)
 