from typing import Iterable

from src.utils.montar_look import montar_look

class Look():
    def __init__(self, prendas_por_partes:dict):
        self.prendas = montar_look(prendas_por_partes)

    def __repr__(self):
        return f"{self.prendas}"
