#!/usr/bin/env python
# -*- coding: utf-8 -*-

import texts
import readWrite

listaPersonas = []
mountPayme()
loop = True


def buscarPersona(nombres):
    """El objeto Persona sobre el que realizaremos ciertas operaciones se obtiene buscando en la lista a través de su nombre"""
    pringados = []
    for nombre in nombres:
        for pringado in listaPersonas:
            if pringado.nombre == nombre:
                pringados.append(pringado)
                break
        print "Error: La persona buscada no existe."
    return -1    

def pagarDeuda(pagador, cantidad, cobrador):
    """Una Persona pagará a otra Persona una cantidad x que se descontará de sus deudas, la cantidad es arbitraria"""
    pagador.apuntarPago(cantidad)
    cobrador.apuntarPago(-cantidad)#El dinero devuelto es dinero que ya no has pagado
    pago = Compra("x", cantidad, cobrador, pagador, "x")
    pago.registar(1)

def definirCompra():
    """Cuando se realice un compra se le irá indicando al usuario los pasos a seguir para introducir los datos y efectuar la operacion"""
    compra = raw_input(texts.hacerCompra1)
    atributos = compra.split(';')
    articulo = atributos[0].split(',')
    precio = atributos[1].split(',')
    comprador = buscarPersona(atributos[2].split(','))
    pagador = buscarPersona(atributos[3].split(','))#solamente para convertirlo en lista
    realizarCompra(articulo, precio, comprador, pagador, atributos[4])
    
def realizarCompra(articulos, precios, compradores, pagador, gasto):
    if len(articulos) == len(compradores): #1 Compra-1 comprador, o varias cosas compradas por varias personas (cena)
        for x in range(len(compradores)):
            compra = Compra(articulos[x], precios[x], compradores[x], pagador, gasto)
            compra.registarCompra()
            compra.registrarPago()
            compradores[x].apuntarCompra(precios[x])
            pagador.apuntarPago(precios[x])
    elif len(articulos) == 1 and 1 < len(compradores): #Varios compradores compramos una única cosa, varias cosas iguales (un regalo o pizza)
        for x in range(len(compradores)):
            compra = Compra(articulos[0], precios[0]/len(compradores), compradores[x], pagador, gasto)
            compra.registarCompra()
            compra.registrarPago()
            compradores[x].apuntarCompra(precios[0]/len(compradores))
        pagador.apuntarPago(precios[0])  


def menu():
    """Menú de opciones"""
    while True:
        opcion = raw_input(texts.menu)
        if opcion == "1":
            return agregarPersona
        elif opcion == "2":
            return definirCompra
        elif opcion == "3":
            return
        elif opcion == "4":
            return 
        elif opcion == "5":
            return 
        elif opcion == "6":
            return
        elif opcion == "7":
            loop = False
            return    
        else:
            print texts.menuError    


def agregarPersona(nombre):
    """Agragamos una persona a la lista de personas con sus valores a 0"""
    nombre = raw_input(texts.nuevoMoroso)#Quizá podríamos hacer un bucle para pedir confirmación
    listaPersonas.append(Persona(nombre))
    print texts.nuevoMorosoSuccess(nombre)

class Persona():
    """"Cada uno de los individuos que participan en el programa se debe definir como una Persona"""
    def __init__(self, nombre, dineroGastado = 0, dineroPagado = 0, dineroEnBote = 0):
        self.nombre = nombre
        self.dineroGastado = dineroGastado #Representa la cantidad de dinero que una persona ha gastado en comprar
        self.dineroPagado = dineroPagado #Representa la cantidad de dinero que una persona ha pagado de más (por otras Personas)
        self.dineroEnBote = dineroEnBote

    def getDeuda(self):
        return self.dineroPagado - self.dineroGastado

    def apuntarPago(self, cantidad):
        """Cuando una persona paga algo, se debe incluir en la cantidad de dineroPagado"""
        self.dineroPagado += cantidad

    def apuntarCompra(self, cantidad):
        """Cuando una persona hace una compra se debe incluir en la cantidad de dineroGastado"""
        self.dineroGastado += cantidad


class Compra(): 
    """La Compra representa la adquisición de algo por parte de una Persona y que normalmente paga otra Persona"""
    def __init__(self, articulo, precio, comprador, pagador, gasto):
        self.articulo = articulo
        self.precio = precio
        self.comprador = comprador
        self.pagador = pagador
        self.gasto = gasto

#    def registar(self, esDeuda = 0):
#        if esDeuda:
#            #comprador es la persona que devuelve el dinero
#            #pagador la persona a la que se lo devuelve
#            #precio es la cantidad a devolver

    def registarCompra(self):
        fileHandle = open("historial.txt", "w")
        registro = self.comprador.name + " ha compra por " + self.precio + " €, " + self.articulo
        fileHandle.write(registro)
        fileHandle.close()

    def registrarPago(self):
        fileHandle = open("historial.txt", "w")
        registro = self.pagdor.name + " ha pagado " + self.precio + " €, " + self.articulo
        fileHandle.write(registro)
        fileHandle.close()

    def registarDeuda(self):
        fileHandle = open("historial.txt", "w")
        registro = self.comprador.name + " devuelve " + self.precio + " € a self.pagador"
        fileHandle.write(registro)
        fileHandle.close()        


#def meterEnBote():


while loop:
    operacion = menu()
    operacion()