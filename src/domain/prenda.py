import uuid

from config.config import CATEGORIAS_PRENDAS, PARTE_DO_CORPO_PRENDAS

class Prenda():
    def __init__(self, categoria, imagem):
        if categoria.upper() not in CATEGORIAS_PRENDAS:
            raise ValueError(f"Categoria incorreta: {categoria}!")
        
        self.id = uuid.uuid1()
        self.categoria = categoria
        self.imagem = imagem
        self.parte_do_corpo = PARTE_DO_CORPO_PRENDAS[categoria]

    
    def __repr__(self):
        pass