#!/usr/bin/env python
# -*- coding: utf-8 -*-

menu = """
1 - Registrar un nuevo moroso en potencia.
2 - Hacer una compra
3 - Hacer una compra (guiada)
4 - Devolver dinero
5 - Añadir dinero al bote
6 - Status
"""

menuError = """
Eso no es una opción válida.
Prueba otra vez.
"""

nuevoMoroso = """
¿Cómo se llama la nueva persona?
""" 

def nuevoMorosoSuccess(nombre):
	text = nombre + """
	se ha añadido a la lista de personas.
	"""

hacerCompra1 = """
Introduce los datos de la compra:
<Artículos>; <Precio>; <Comprador>; <Pagador>; <Gasto>.
"""

#Aquí irian los datos de la compra guiada

devolverDinero = """
¡Por fin vas a pagar lo que debes!
Indica tu deuda a pagar de la siguiente manera:
<Pagador>, <Cantidad>, <Cobrador>.
"""

meterEnBote = """
¿Quién eres y cuanto vas a añadir al bote?
"""

	