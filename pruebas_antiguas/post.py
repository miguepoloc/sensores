#Método post
import requests

params = {
    "temperatura": 19,
    "fecha": "",
    "unidad": "°C",
    "flag": 4,
    "latitud": "11.229602",
    "longitud": "-74.163671"
}
r = requests.post('http://127.0.0.1:8000/api/temperatura/', data=params)
print(r.text)
