import pymysql
try:
	conexion = pymysql.connect(host='localhost',user='root',password='', db='peliculas')
	try:
		with conexion.cursor() as cursor:
			cursor.execute("SELECT * FROM peliculas;")
			peliculas = cursor.fetchall()

			for pelicula in peliculas:
				print(pelicula)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)