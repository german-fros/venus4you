from config.config import CATEGORIAS_PRENDAS, FORMALIDADE_PRENDAS
import uuid

class Prenda():
    def __init__(self, categoria, imagem, material=None, cor=None, formalidade=None):
        if categoria.upper() not in CATEGORIAS_PRENDAS:
            raise ValueError(f"Categoria incorreta: {categoria}!")
        
        if formalidade and formalidade.upper() not in FORMALIDADE_PRENDAS:
            raise ValueError(f"Tipo de formalidade incorreta: {formalidade}!")
        
        self.id = uuid.uuid1()
        self.categoria = categoria
        self.imagem = imagem
        self.material = material
        self.cor = cor
        self.formalidade = formalidade

    
    def __repr__(self):
        return f"{self.categoria} | {self.material} | {self.cor} | {self.formalidade}"