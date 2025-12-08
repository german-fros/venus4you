import random

def montar_look(prendas_por_parte):
    look = []
    usar_vestido = False

    # Primer loop: elegir prendas normalmente
    for parte in sorted(prendas_por_parte.keys()):
        
        if usar_vestido and parte == "2I":
            continue

        prenda = random.choice(prendas_por_parte[parte])

        if prenda.categoria == "VESTIDOS":
            usar_vestido = True

        look.append(prenda)

    return look
