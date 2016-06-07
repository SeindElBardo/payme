#!/usr/bin/env python
# -*- coding: utf-8 -*-

import texts
import sys
#import readWrite


listaPersonas = []
registrosDeSesion = []

#Persona
class Persona():
    """"Cada uno de los individuos que participan en el programa se debe definir como una Persona"""
    def __init__(self, nombre, dineroGastado = 0, dineroPagado = 0, dineroEnBote = 0):
        self.nombre = nombre
        self.dineroGastado = float(dineroGastado) #Representa la cantidad de dinero que una persona ha gastado en comprar
        self.dineroPagado = float(dineroPagado) #Representa la cantidad de dinero que una persona ha pagado de más (por otras Personas)
        self.dineroEnBote = float(dineroEnBote)

    def getDeuda(self):
        return self.dineroGastado - self.dineroPagado

    def apuntarPago(self, cantidad):
        """Cuando una persona paga algo, se debe incluir en la cantidad de dineroPagado"""
        self.dineroPagado += cantidad

    def apuntarCompra(self, cantidad):
        """Cuando una persona hace una compra se debe incluir en la cantidad de dineroGastado"""
        self.dineroGastado += cantidad

#Compra
class Compra(): 
    """La Compra representa la adquisición de algo por parte de una Persona y que normalmente paga otra Persona"""
    def __init__(self, articulo, precio, comprador, pagador, gasto):
        self.articulo = articulo
        self.precio = precio
        self.comprador = comprador
        self.pagador = pagador
        self.gasto = gasto

##Registro en historial
    def registarCompra(self):
        registro = self.comprador.nombre + " ha comprado por " + str(self.precio) + " €: " + self.articulo + "\n"
        print texts.registroHistorialSuccess(registro)
        registrosDeSesion.append(registro)

    def registrarPago(self):
        registro = self.pagador.nombre + " ha pagado " + str(self.precio) + " € por: " + self.articulo + "\n"
        print texts.registroHistorialSuccess(registro)
        registrosDeSesion.append(registro)

    def registarDeuda(self):
        registro = self.pagador.nombre + " devuelve " + str(self.precio) + " € a " + self.comprador.nombre + "\n"
        print texts.registroHistorialSuccess(registro)
        registrosDeSesion.append(registro)


#Montaje y desmonaje
def mountPayme():
    """Para la persistencia de los datos, se deben instanciar al iniciar el programa las personas junto con sus datos de 
    sesiones anteriores"""
    try:
        fileHandle = open("personas.txt", "r")
    except:     
        fileHandle = open("personas.txt", "w")
        fileHandle.close()
        return

    lista = fileHandle.readlines()
    for persona in lista:
        persona = persona[:-1]#Quitamos el salto de línea    
        casiPersona = persona.split(',')#Creamos una lista con los datos de la persona
        #casiPersona[3].replace("\n", "")    
        moroso = Persona(casiPersona[0], casiPersona[1], casiPersona[2], casiPersona[3])
        listaPersonas.append(moroso)#Y añadimos el objeto al a lista
    fileHandle.close()

def unmountPayme():
    """Al terminar las operaciones todos los datos generados durante la sesión se graban en los ficheros correspondientes"""
    fileHandle = open("personas.txt", "w")
    datos = ""
    for persona in listaPersonas:
        datos += persona.nombre + ',' + str(persona.dineroGastado) + ',' + str(persona.dineroPagado) + ',' + str(persona.dineroEnBote) + '\n'
    fileHandle.write(datos)
    fileHandle.close()

    fileHandle = open("historial.txt", "a")
    for registro in registrosDeSesion:
        fileHandle.write(registro)
    fileHandle.close()
    sys.exit(1)
#Interfaz
def menu():
    """Menú de opciones, según la opción elegida se devolverá la función a ejecutar"""
    while True:
        opcion = raw_input(texts.menu)
        if opcion == "1":
            return agregarPersona
        elif opcion == "2":
            return definirCompra
        elif opcion == "3":
            return
        elif opcion == "4":
            return definirDeuda
        elif opcion == "5":
            return 
        elif opcion == "6":
            return status
        elif opcion == "7":
            loop = False
            return unmountPayme
        else:
            print texts.menuError    

#funciones
def buscarPersona(nombres):
    """El objeto Persona sobre el que realizaremos ciertas operaciones se obtiene buscando en la lista a través de su nombre"""
    pringados = []
    for nombre in nombres:
        for pringado in listaPersonas:
            if pringado.nombre == nombre:
                pringados.append(pringado)
                break
            if pringado is None:
                print texts.errorPersonaNoExiste
                return -1
    return pringados
    
##Agregar Persona
def agregarPersona():
    """Agragamos una persona a la lista de personas con sus valores a 0"""
    nombre = raw_input(texts.nuevoMoroso)#Quizá podríamos hacer un bucle para pedir confirmación
    listaPersonas.append(Persona(nombre.lower()))
    print texts.nuevoMorosoSuccess(nombre)

##Realizar una compra
def definirCompra():
    """Cuando se realice un compra el usuario introducirá los datos solicitados y se tratarán para poder realizar la compra"""
    compra = raw_input(texts.hacerCompra1)
    argumentos = compra.split(';')
    articulo = argumentos[0].split(',')
    precio = argumentos[1].split(',')
    #Lo pasamos a minúsculas, para ahorrar problemas
    comprador = buscarPersona(argumentos[2].lower().replace(" ", "").split(','))
    pagador = buscarPersona(argumentos[3].lower().replace(" ", "").split(','))#solamente para convertirlo en lista y poder usar buscarPersona
    realizarCompra(articulo, precio, comprador, pagador[0], argumentos[4])
    
def realizarCompra(articulos, precios, compradores, pagador, gasto):
    """Teniendo los datos tratados, es necesario crear los objetos, efectuar las operaciones necesarias y registrar dichas compras
    en el historial"""
    if len(articulos) == len(compradores): #1 Compra-1 comprador, o varias cosas compradas por varias personas (cena)
        for x in range(len(compradores)):
            compra = Compra(articulos[x], float(precios[x]), compradores[x], pagador, gasto)
            compra.registarCompra()
            compra.registrarPago()
            compradores[x].apuntarCompra(float(precios[x]))
            pagador.apuntarPago(float(precios[x]))
    elif len(articulos) == 1 and 1 < len(compradores): #Varios compradores compramos una única cosa, varias cosas iguales (un regalo o pizza)
        for x in range(len(compradores)):
            compra = Compra(articulos[0], float(precios[0])/len(compradores), compradores[x], pagador, gasto)
            compra.registarCompra()
            compra.registrarPago()
            compradores[x].apuntarCompra(float(precios[0])/len(compradores))
        pagador.apuntarPago(float(precios[0]))


##Devolver Dinero
def definirDeuda():
    """Cuando se realice el pago de una deuda, el usuario introducirá los datos solicitados y se tratarán para poder gestionar
    el pago"""
    deuda = raw_input(texts.devolverDinero)
    argumentos = deuda.split(';')
    pagador = buscarPersona(argumentos[0].lower().replace(" ", "").split(','))
    cobrador = buscarPersona(argumentos[2].lower().replace(" ", "").split(','))
    pagarDeuda(pagador[0], float(argumentos[1]), cobrador[0])

def pagarDeuda(pagador, cantidad, cobrador):
    """Teniendo los datos tratados, es necesario crear los objetos, efectuar las operaciones necesarias y registrar dichas transacciones
    en el historial"""    
    pagador.apuntarPago(cantidad)
    cobrador.apuntarPago(-cantidad)#El dinero devuelto es dinero que ya no has pagado
    pago = Compra("x", cantidad, cobrador, pagador, "x")
    pago.registarDeuda()

##Añadir dinero al bote
#def meterEnBote():


##Status
def status():
    """Mostramos todos los usuarios con sus respectivas deudas. Hay que recordar la filosofía de que no se le debe
    a la persona que pago concretamente, debe dinero aquel que ha comprado más de lo que ha pagado y se le debe dinero
    a aquel que a pagado más de lo que ha comprado"""
    for pringado in listaPersonas:
        print texts.status(pringado.nombre, pringado.dineroGastado > pringado.dineroPagado, abs(pringado.getDeuda()))



#Progama principal. MAIN
mountPayme()
loop = True
while loop:
    try:
        operacion = menu()
        operacion()
    except SystemExit:#Hay que insistirle por estar dentro de un try
        sys.exit()    
    except:
        print texts.menuError 
