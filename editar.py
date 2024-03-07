
import pymysql
try:
	conexion = pymysql.connect(host='localhost',user='root',password='', db='peliculas')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "UPDATE peliculas SET titulo = %s WHERE id = %s;"
			nuevo_titulo = "El padrino"
			id_editar = 2
			cursor.execute(consulta, (nuevo_titulo, id_editar))

		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar con la base de datos: ", e)