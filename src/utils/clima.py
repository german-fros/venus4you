from datetime import datetime, date, time
import requests

from config.config import CIDADES_COORDS


def obter_lat_lon_cidade(cidade: str):
    cidade_norm = cidade.strip().upper()
    coords = CIDADES_COORDS.get(cidade_norm)

    if coords is None:
        # puedes devolver None y tratarlo arriba o lanzar excepción
        raise ValueError(f"Cidade não cadastrada na base simulada: {cidade}")

    return coords  # (lat, lon)


def obter_clima_para_evento(cidade: str, data: date, horario: time):
    base_url = "https://api.open-meteo.com/v1/forecast"

    try:
        lat, lon = obter_lat_lon_cidade(cidade)
    except ValueError as e:
        # en Streamlit pondrías st.warning(str(e)) y retornarias None
        print(e)
        return None

    data_hora = datetime.combine(data, horario)
    data_str = data_hora.date().isoformat()  # yyyy-mm-dd

    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation_probability,precipitation",
        "timezone": "America/Sao_Paulo",
        "start_date": data_str,
        "end_date": data_str,
    }

    resp = requests.get(base_url, params=params, timeout=10)
    resp.raise_for_status()
    data_json = resp.json()

    hourly = data_json.get("hourly", {})
    times = hourly.get("time")
    temps = hourly.get("temperature_2m")
    pops = hourly.get("precipitation_probability")
    precs = hourly.get("precipitation")

    if not times:
        return None

    dt_times = [datetime.fromisoformat(t) for t in times]

    target = data_hora.replace(minute=0, second=0, microsecond=0)

    idx = min(range(len(dt_times)), key=lambda i: abs(dt_times[i] - target))

    return {
        "time": dt_times[idx],
        "temperature": temps[idx],
        "precipitation_probability": pops[idx] if pops else None,
        "precipitation": precs[idx] if precs else None,
    }
