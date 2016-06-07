#!/usr/bin/env python
# -*- coding: utf-8 -*-

menu = """
1 - Registrar un nuevo moroso en potencia.
2 - Hacer una compra
3 - Hacer una compra (guiada) *EN DESARROLLO*
4 - Devolver dinero
5 - Añadir dinero al bote *EN DESARROLLO*
6 - Status
7 - Guardar y salir
"""

menuError = """
Eso no es una opción válida.
Prueba otra vez.
"""

nuevoMoroso = """
¿Cómo se llama la nueva persona?
""" 

def nuevoMorosoSuccess(nombre):
	return nombre + " se ha añadido a la lista de personas."

hacerCompra1 = """
Introduce los datos de la compra:
<Artículos>; <Precio>; <Comprador>; <Pagador>; <Gasto>.
"""

def registroHistorialSuccess(registro):
	return "Se ha añadido al historial el registro: " + registro

errorPersonaNoExiste = "Error: La persona buscada no existe."

#Aquí irian los datos de la compra guiada

devolverDinero = """
¡Por fin vas a pagar lo que debes!
Indica tu deuda a pagar de la siguiente manera:
<Pagador>; <Cantidad>; <Cobrador>.
"""

meterEnBote = """
¿Quién eres y cuanto vas a añadir al bote?
"""

def status(nombre, moroso, cantidad):
	if moroso:
		return nombre + " debe un total de " + str(cantidad) + " €"
	else:
		return "A " + nombre + " se le debe un total de " + str(cantidad) + " €"
		