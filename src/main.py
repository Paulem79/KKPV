import csv
from commons import Data, Mention


formatted: list[Data] = []

with open('../mentions-anonymised.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for i, row in enumerate(
            spamreader):  # J'ai appris qu'on pouvait mettre directement i dans la boucle for, grâce à enumerate
        if i == 0:  # Me permettant ainsi d'ignorer la première ligne d'en tête
            continue

        formatted.append(Data(Mention(row[0]), float(row[3]), int(row[1])))