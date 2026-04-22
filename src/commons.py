from enum import StrEnum
from typing import NamedTuple
from matplotlib.typing import ColorType


class Mention(StrEnum):
    FELICITATIONS = "Félicitations",
    COMPLIMENTS = "Compliments",
    ENCOURAGEMENTS = "Encouragements",
    MISE_EN_GARDE = "Mise en garde pour l'assiduité",
    PAS_DE_MENTION = "Pas de mention"

class Data(
    NamedTuple):  # J'organise déjà dans un type pour faciliter le travail avec les données dans les prochains exercices
    mention: Mention
    moyenne: float
    absence: int

mentions_colors: dict[Mention, ColorType] = {
    Mention.PAS_DE_MENTION: "gray",
    Mention.MISE_EN_GARDE: "black",
    Mention.ENCOURAGEMENTS: "red",
    Mention.COMPLIMENTS: "green",
    Mention.FELICITATIONS: "blue"
}