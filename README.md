# payme
Payme es una aplicación de gestión de deudas cuya funcionalidad se basa en llevar la cuenta del dinero que se deben los integrantes de un grupo de amigos, esta cuenta se basa en el principio de "El dinero que cada integrante a empleado en compras, debe ser igual al que esa misma persona ha tenido que pagar". Por lo que si una persona ha pagado más de lo que ha gastado significa que alguien le debe dinero, de la misma forma que si compras más de lo que pagas le debes dinero a alguien, sin embargo al estar en un grupo de confianza, quien fía a quien es irrelevante mientras que nadie esté pagando de más.

#Instrucciones
En esta versión demo para consola, se han implementado las siguientes funcionalidades:

##Registrar personas
Para que se puedan llevar cuentas es necesario primero registrar a la persona en la aplicación. Para ello basta con proporcionar un nombre identificativo, no será sensible a mayúsculas ni minúsculas.

Problemas pendientes de solucionar: Se admiten nombres vacíos y repetidos.

##Realizar compras
Las compras se definen mediante una tupla con formato: <Artículos>; <Precio>; <Comprador>; <Pagador>; <Gasto>.
Sin embargo dentro de artículos, precio y compradores puedes añadir varios separados por comas de forma que hagas una compra múltiple, ej:

	Introduce los datos de la compra:
	<Artículos>; <Precio>; <Comprador>; <Pagador>; <Gasto>.
	ar1, ar2, ar3; 12, 13, 255; Adri, Paco, Mireya; Eli; 300
	Se ha añadido al historial el registro: adri ha comprado por 12.0 €: ar1

	Se ha añadido al historial el registro: eli ha pagado 12.0 € por: ar1

	Se ha añadido al historial el registro: paco ha comprado por 13.0 €:  ar2

	Se ha añadido al historial el registro: eli ha pagado 13.0 € por:  ar2

	Se ha añadido al historial el registro: mireya ha comprado por 255.0 €:  ar3

	Se ha añadido al historial el registro: eli ha pagado 255.0 € por:  ar3

También se permite la compra en conjunto definiendo solo un articulo y precio.
	Introduce los datos de la compra:
	<Artículos>; <Precio>; <Comprador>; <Pagador>; <Gasto>.
	Pizzas; 31.30; Adri, Paco, Jony, Mireya; Mireya; 50           
	Se ha añadido al historial el registro: adri ha comprado por 7.825 €: Pizzas

	Se ha añadido al historial el registro: mireya ha pagado 7.825 € por: Pizzas

	Se ha añadido al historial el registro: paco ha comprado por 7.825 €: Pizzas

	Se ha añadido al historial el registro: mireya ha pagado 7.825 € por: Pizzas

	Se ha añadido al historial el registro: jony ha comprado por 7.825 €: Pizzas

	Se ha añadido al historial el registro: mireya ha pagado 7.825 € por: Pizzas

	Se ha añadido al historial el registro: mireya ha comprado por 7.825 €: Pizzas

	Se ha añadido al historial el registro: mireya ha pagado 7.825 € por: Pizzas

##Pagar Deudas
Para compensar directamente el dinero que debes, puedes utilizar esta función para registrar el pago de una deuda, que puede ser de cualquier cantidad. Esto permite además gestionar prestamos.

Problemas pendientes de solucionar: No se comprueba que las cantidades sean positivas. No se ha establecido un criterio para decimales.

##Status
Esta función simplemente nos mostrará como va actualmente la balanza de deudas para cada persona, indicándonos quien debe y a quien se le debe.