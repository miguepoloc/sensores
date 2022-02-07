# Código para método get
import requests
response = requests.get('http://127.0.0.1:8000/api/temperatura/')
respuesta = response.json()
print(respuesta)
