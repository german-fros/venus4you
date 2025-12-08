from datetime import datetime
import uuid

from config.config import CIDADES_RS_EVENTO, FORMALIDADE_PRENDAS
from src.utils.clima import obter_clima_para_evento


class Evento():
    def __init__(self, nome, formalidade, data, horario, estado, cidade):
        if cidade.upper() not in CIDADES_RS_EVENTO:
            raise ValueError(f"Cidade inválida: {cidade}!")
        
        if formalidade.upper() not in FORMALIDADE_PRENDAS:
            raise ValueError(f"Tipo de formalidade incorreta: {formalidade}!")
        
        if datetime.combine(data, horario) < datetime.today():
            raise ValueError(f"A data e o horario selecionados são inválidos!")
        
        self.id = uuid.uuid1()
        self.nome = nome
        self.formalidade = formalidade
        self.data = data
        self.horario = horario
        self.estado = estado
        self.cidade = cidade

    
    def __repr__(self):
        return f"{self.nome.upper()} \n{self.formalidade.capitalize()}\nData: {self.data}\nHora: {self.horario}\n{self.cidade.upper()}/{self.estado}"
    

    