import psycopg2
from datetime import datetime
now = datetime.now()

conexion1 = psycopg2.connect(database="prueba", user="pi", password="!nv3m4r")
cursor1 = conexion1.cursor()
sql = "insert into api_temperatura(temperatura, fecha) values (%s,%s)"
datos = (38.5, now)
cursor1.execute(sql, datos)
conexion1.commit()
conexion1.close()
