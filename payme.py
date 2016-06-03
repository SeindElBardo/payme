#!/usr/bin/env python
# -*- coding: utf-8 -*-

listaPersonas = []


def buscarPersona(nombre):
    """El objeto Persona sobre el que realizaremos ciertas operaciones se obtiene buscando en la lista a traves de su nombre"""
    for pringado in listaPersonas:
        if pringado.nombre == nombre:
            return pringado
    print "Error: La persona buscada no existe."
    return -1    

def pagarDeuda(pagador, cantidad, cobrador):
    """Una Persona pagara a otra Persona una cantidad x que se descontara de sus deudas, la cantidad es arbitraria"""
    pagador.apuntarPago(cantidad)
    cobrador.apuntarPago(-cantidad)#El dinero devuelto es dinero que ya no has pagado
    pago = Compra("x", cantidad, cobrador, pagador, "x")
    pago.registar(1)

def definirCompra():
    """Cuando se realice un compra se le ira indicando al usuario los pasos a seguir para introducir los datos y efectuar la operacion"""


def menu():
    """Menu de opciones"""


def agregarPersona(nombre):
    """Agragamos una persona a la lista de personas con sus valores a 0"""
    listaPersonas.append(Persona(nombre))

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
    """docstring for Compra"""
    def __init__(self, articulo, precio, comprador, pagador, gasto):
        self.articulo = articulo
        self.precio = precio
        self.comprador = comprador
        self.pagador = pagador
        self.gasto = gasto

    def registar(self, esDeuda = 0):
        if esDeuda:
            #comprador es la persona que devuelve el dinero
            #pagador la persona a la que se lo devuelve
            #precio es la cantidad a devolver


def meterEnBote():