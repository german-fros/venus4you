import random

def montar_look(prendas_por_parte):
        # temp_evento = clima_evento['temperature']
        # prob_chuva =clima_evento['precipitation_probability']

        look = []

        for parte in prendas_por_parte.keys():
            prenda = random.choice(prendas_por_parte[parte])

            look.append(prenda)

        return look