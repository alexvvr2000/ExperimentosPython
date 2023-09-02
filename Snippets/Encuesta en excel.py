import pandas as pd
from random import choice, randint, choices
from os import remove
from os.path import exists

data = {}
gente_total = 30

opciones1 = ["Mucho", "poco", "No lo se"]
opciones2 = ["Si", "Nunca"]
opciones3 = opciones2
opciones4 = opciones2
opciones5 = ["Si", "lo dudo", "muy poco"]

for i in range(1, 6):

    key = i
    data[key] = {}

    for j in range(0, gente_total):

        if i == 1:
            data[key][j] = (choices(opciones1,k=1,weights=[8,10,3]))[0]
        elif i == 2:
            data[key][j] = (choices(opciones2,k=1, weights=[10,5]))[0]
        elif i == 3:
            data[key][j] = (choices(opciones3,k=1, weights=[7,5]))[0]
        elif i == 4:
            data[key][j] = (choices(opciones4,k=1))[0]
        elif i == 5:
            data[key][j] = (choices(opciones5,k=1, weights=[8,10,5]))[0]

file = "p.xlsx"

if(exists(file)):
    remove(file)

frame = pd.DataFrame(data)
frame.to_excel(file)