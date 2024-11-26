from django.core.exceptions import ValidationError
import re


def calcular_digito_verificador(cuit_base):
	coeficientes = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
	cuit_digits = [int(digit) for digit in str(cuit_base)]
	suma = sum(cuit_digits[i] * coeficientes[i] for i in range(len(coeficientes)))
	resto = suma % 11
	
	if resto == 0:
		return 0
	elif resto == 1:
		return 9 if cuit_digits[0] in [2, 3] else 4
	else:
		return 11 - resto

def validar_cuit(cuit):
	cuit_str = str(cuit)
	
	#-- Validar que comience con los prefijos específicos y tenga 11 dígitos en total.
	if not re.match(r'^(20|23|24|25|26|27|30|33|34)\d{9}$', cuit_str):
		raise ValidationError("El CUIT debe comenzar con 20, 23, 24, 25, 26, 27, 30, 33 o 34, y tener 11 dígitos.")
	
	#-- Separar los primeros 10 dígitos y el dígito verificador.
	cuit_base = int(cuit_str[:-1])
	digito_verificador = int(cuit_str[-1])
	
	#-- Calcular el dígito verificador.
	digito_calculado = calcular_digito_verificador(cuit_base)
	
	#-- Validar el dígito verificador.
	if digito_verificador != digito_calculado:
		raise ValidationError("El CUIT no es válido.")

def calcular_digito_tarjeta(sucursal, socio, adicional):
    # Calcular nTarjeta
    n_tarjeta = (sucursal * 10000000) + (socio * 100) + adicional

    # Convertir nTarjeta a una cadena de 9 dígitos (izquierda alineada, relleno con espacios)
    # c_cadena = f"{n_tarjeta:9d}"
    c_cadena = str(n_tarjeta).zfill(9)  # Asegura 9 dígitos, rellenando con ceros a la izquierda

    # Inicializar variables
    n_suma = 0
    b = 1

    # Bucle para sumar según la lógica dada
    for i in range(9):
        n_nro = int(c_cadena[i])  # Extraer el dígito en la posición i
        n_suma += n_nro * b  # Multiplicar por el valor de 'b'
        b += 2  # Incrementar b por 2
        if b > 9:
            b = 3  # Reiniciar b si excede 9

    # Calcular nResto (equivalente a mitad de suma y su residuo)
    n_mitad = n_suma / 2
    n_resto = int(n_mitad % 10)

    # Calcular el valor total de la tarjeta con el dígito verificador
    n_tarjeta_verificada = (n_tarjeta * 10) + n_resto

    # Devolver los resultados
    return n_tarjeta_verificada
