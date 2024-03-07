
import pymysql
try:
	conexion = pymysql.connect(host='localhost',user='root',password='', db='peliculas')
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
			cursor.execute(consulta, ("Volver al futuro 1", 1985))
			cursor.execute(consulta, ("Ready Player One", 2018))
			cursor.execute(consulta, ("It", 2017))
			cursor.execute(consulta, ("Pulp Fiction", 1994))
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar con la base de datos: ", e)