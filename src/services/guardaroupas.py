from src.domain.prenda import Prenda
from typing import Iterable

import pandas as pd


class Guardaroupas():
    def __init__(self, prendas:pd.DataFrame):
        self.prendas = [Prenda(**row) for row in prendas.to_dict(orient="records")]


    def __len__(self):
        return len(self.prendas)
    

    def __repr__(self):
        return self.prendas