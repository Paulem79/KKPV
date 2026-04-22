import math
from main import formatted
from commons import Data, Mention
import operator

# USED CODE
# Source - https://stackoverflow.com/a/268285
# Posted by unbeknown, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-22, License - CC BY-SA 4.0
'''
import operator
stats = {'a': 1000, 'b': 3000, 'c': 100}
max(stats.iteritems(), key=operator.itemgetter(1))[0]
'''


def ppvoisin_index(datas: list[Data], data: Data, k: int) -> list[tuple[int, float]]:
    max_moyenne = max(d.moyenne for d in datas)
    max_absence = max(d.absence for d in datas)
    min_moyenne = min(d.moyenne for d in datas)
    min_absence = min(d.absence for d in datas)

    dist_datas: list[float] = [dist(data, d, max_moyenne, max_absence, min_moyenne, min_absence) for d in datas]
    tuple_datas: list[tuple[int, float]] = []
    for i, dist_data in enumerate(dist_datas):
        tuple_datas.append((i, dist_data))

    closest = sorted(tuple_datas, key=lambda d: d[1])  # Trier par distance depuis le tuple
    return closest[:k]

def dist(data1: Data, data2: Data, max_moyenne: float, max_absence: float, min_moyenne: float,
         min_absence: float):
    x1 = (data1.moyenne - min_moyenne) / (max_moyenne - min_moyenne)
    x2 = (data2.moyenne - min_moyenne) / (max_moyenne - min_moyenne)
    y1 = (data1.absence - min_absence) / (max_absence - min_absence)
    y2 = (data2.absence - min_absence) / (max_absence - min_absence)

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def weight_formula(x: float): # Paraît bien dans desmos, peut être changé au besoin https://www.desmos.com/calculator/xi3tsn1dgi
    return (math.log(x) / 3)**3

def amplify_weight(distance: float): # Récompenser les plus proches
    return 1 - weight_formula(distance) # En dessous de 1 de distance = bonus à la note de 1

def predict_mention(closest: list[Data], closest_els_tuples: list[tuple[int, float]]): # On pourrait ajouter la dist pour encore améliorer la précision, plus c'est loin, moins ça compte sur la weight
    mentions = [close.mention for close in closest]
    weights: dict[Mention, float] = {}

    for mention in mentions:
        if mention not in weights:
            weights[mention] = 0

        distance = closest_els_tuples[mentions.index(mention)][1]
        weights[mention] += amplify_weight(distance)

    print(weights)

    predicted = max(weights.items(), key=operator.itemgetter(1))[0]
    return predicted

data = Data(Mention.ENCOURAGEMENTS, 12, 5) # 12 de moyenne, 5 1/2j d'abs

closest_els_tuples = ppvoisin_index(formatted, data, 30)
closest_els = [formatted[el_tuple[0]] for el_tuple in closest_els_tuples]

print(closest_els)
print(predict_mention(closest_els, closest_els_tuples))