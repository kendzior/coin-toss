#Rzucanie monetą
#Program "rzuci" monetą sto razy, a następnie podsumuje ile razy wypadł orzeł i reszka

print("\tRzut monetą")
print("\nZa chwilę rzucę monetą sto razy, a następnie powiem Ci ile razy wypadł orzeł i reszka")

import random

eagle = 0
head = 0
count = 0

while count < 100:
    
    toss = random.randint(1,2)

    if toss == 1:
        count += 1
        eagle += 1
    else:
        count += 1
        head += 1

print("\n\nCałkowita ilość orzełków to", eagle)
print("\n\nCałkowita ilość reszek to", head)

input("\n\nAby zakończyć program wciśnij Enter")



