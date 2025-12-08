from datetime import datetime, date, time
import requests

def obter_clima_para_evento(cidade: str, estado: str, data: date, horario: time):
    base_url = "https://api.open-meteo.com/v1/forecast"

    lat, lon = obter_lat_lon_cidade(cidade, estado)

    data_hora = datetime.combine(data, horario)

    # Usamos la misma fecha como start y end (solo ese día)
    data_str = data_hora.date().isoformat()

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
    data = resp.json()

    hourly = data.get("hourly", {})
    times = hourly.get("time")
    temps = hourly.get("temperature_2m")
    pops = hourly.get("precipitation_probability")
    precs = hourly.get("precipitation")

    if not times:
        return None

    # Convertimos las horas de la API a datetime
    dt_times = [datetime.fromisoformat(t) for t in times]

    # Normalizamos el evento a hora exacta (Open-Meteo devuelve en horas cerradas)
    target = data_hora.replace(minute=0, second=0, microsecond=0)

    # Índice de la hora más cercana
    idx = min(range(len(dt_times)), key=lambda i: abs(dt_times[i] - target))

    return {
        "time": dt_times[idx],
        "temperature": temps[idx],
        "precipitation_probability": pops[idx] if pops else None,
        "precipitation": precs[idx] if precs else None,
    }


def obter_lat_lon_cidade(cidade: str, estado: str):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": f"{cidade} {estado}",
        "format": "json",
        "limit": 1,
        "addressdetails": 0,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    }
    
    resp = requests.get(url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    if not data:
        return None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])

    return lat, lon

