#!/usr/bin/env python
# -*- coding: utf-8 -*-

import payme

def mountPayme():
	try:
		fileHandle = open("personas.txt", "r")
	except:		
		fileHandle = open("personas.txt", "w")
		fileHandle.close()
		return

	lista = fileHandle.readlines()
	for persona in lista:
		persona.replace("\n", "")#Quitamos el salto de línea
		casiPersona = persona.split(',')#Creamos una lista con los datos de la persona
		payme.listaPersonas.append(Persona(persona[0], persona[1], persona[2], persona[3]))#Y añadimos el objeto al a lista
	fileHandle.close()

def unmountPayme():
	fileHandle = open("personas.txt", "w")
	datos = ""
	for persona in payme.listaPersonas:
		datos += persona.nombre + ',' + persona.dineroGastado + ',' + persona.dineroPagado + ',' + persona.dineroEnBote + '\n'

	fileHandle.write(datos)
	fileHandle.close()

def registrarCompra():


#def registrarPago():
#
#    def registarCompra(self):
#        fileHandle = open("historial.txt", "w")
#        registro = self.comprador.name + " ha compra por " + self.precio + " €, " + self.articulo
#        fileHandle.write(registro)
#        fileHandle.close()
#
#    def registrarPago(self):
#        fileHandle = open("historial.txt", "w")
#        registro = self.pagdor.name + " ha pagado " + self.precio + " €, " + self.articulo
#        fileHandle.write(registro)
#        fileHandle.close()
#
#    def registarDeuda(self):
#        fileHandle = open("historial.txt", "w")
#        registro = self.comprador.name + " devuelve " + self.precio + " € a self.pagador"
#        fileHandle.write(registro)
#        fileHandle.close()