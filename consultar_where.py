
import pymysql
try:
	conexion = pymysql.connect(host='localhost',user='root',password='', db='peliculas')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT * FROM peliculas WHERE anio > %s;"
			cursor.execute(consulta, (2000))

			peliculas = cursor.fetchall()

			for pelicula in peliculas:
				print(pelicula)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar con la base de datos: ", e)