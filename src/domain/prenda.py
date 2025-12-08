from config.config import CATEGORIAS_PRENDAS, FORMALIDADE_PRENDAS, PARTE_DO_CORPO_PRENDAS
import uuid

class Prenda():
    def __init__(self, categoria, imagem, cor="Não especificado", formalidade="Não especificado"):
        if categoria.upper() not in CATEGORIAS_PRENDAS:
            raise ValueError(f"Categoria incorreta: {categoria}!")
        
        if formalidade and formalidade.upper() not in FORMALIDADE_PRENDAS:
            raise ValueError(f"Tipo de formalidade incorreta: {formalidade}!")
        
        self.id = uuid.uuid1()
        self.categoria = categoria
        self.imagem = imagem
        self.cor = cor
        self.formalidade = formalidade
        self.parte_do_corpo = PARTE_DO_CORPO_PRENDAS[categoria]

    
    def __repr__(self):
        return f"Cor: {self.cor}\nFormalidade: {self.formalidade}"