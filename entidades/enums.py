# entidades/enums.py
from enum import Enum

class Semana(Enum):
    SEGUNDA = "Segunda-Feira"
    TERCA = "Terça-Feira"
    QUARTA = "Quarta-Feira"
    QUINTA = "Quinta-Feira"
    SEXTA = "Sexta-Feira"

class Modalidades(Enum):
    VOLEI = "Vôlei"
    BASQUETE = "Basquete"
    FUTSAL = "Futsal"
    HANDEBOL = "Handebol"