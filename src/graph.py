import matplotlib.pyplot as plt
from commons import mentions_colors, Mention
from main import formatted


# Je crois que c'est obligé pour ne pas garder le même graphique, sans cette ligne j'avais des soucis d'affichage
plt.clf()

def get_mention_xy(mention: Mention):
    filtered = list(filter(lambda data: data.mention == mention, formatted))

    # absences
    x = [data.absence for data in filtered]

    # moyennes
    y = [data.moyenne for data in filtered]

    # ajouter au graphique avec la couleur correspondante dans mentions dcp
    plt.scatter(x, y, c=mentions_colors[mention], label=mention)


for mention in mentions_colors.keys():
    print(mention)
    get_mention_xy(mention)

plt.legend()
plt.title('Décision du destin des élèves')
plt.xlabel('absences')
plt.ylabel('moyenne')

plt.show()
