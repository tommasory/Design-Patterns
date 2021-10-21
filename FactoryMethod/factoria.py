from femenino import Femenino
from masculino import Masculino

class Factoria(object):
	"""Esta clase es nuestra factoria, como ya sabes
	Python define un constructor sin argumentos 
	por default para cada clase, por eso no hace falta 
	escribir uno"""

	def get_persona(self, nombre, genero, edad):
		"""Metodo que retorna objetos persona segun el genero"""

		#genero es el parametro usado por la factoria 
		#para elegir el obj a crear
		if genero == 'F': 
			return Femenino(nombre, edad, genero)
		elif genero == 'M':
			return Masculino(nombre, edad, genero)