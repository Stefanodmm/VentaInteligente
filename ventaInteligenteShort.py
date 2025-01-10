import requests
import time  # Importar la biblioteca time

# Variables configurables
par = 'BTCUSDT'  # Cambia esto por el par que desees
intervalo = 10  # Intervalo en segundos
porcentaje_arriba = 0.01  # Porcentaje por encima del precio actual (1%)

def obtener_precio(par):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={par}'
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return float(datos['price'])
    else:
        raise Exception(f'Error al obtener el precio: {respuesta.status_code}')

def monitorear_precio(par, intervalo, porcentaje_arriba):
    precio_anterior = obtener_precio(par)
    precio_objetivo = precio_anterior * (1 + porcentaje_arriba)  # Calcular el precio objetivo
    print(f'Precio inicial: {precio_anterior}, Precio objetivo para cerrar: {precio_objetivo}')

    while True:
        precio_actual = obtener_precio(par)
        print(f'El precio actual de {par} es: {precio_actual}')

        if precio_actual < precio_anterior:
            precio_anterior = precio_actual
            precio_objetivo = precio_anterior * (1 + porcentaje_arriba)  # Recalcular el precio objetivo
            print(f'Nuevo precio detectado: {precio_anterior}, Nuevo precio objetivo para cerrar: {precio_objetivo}')
        
        if precio_actual >= precio_objetivo:
            print(f'¡Cierra! El precio ha subido a {precio_actual}, que es igual o mayor que el precio objetivo de {precio_objetivo}.')
            break  # Salir del bucle si se debe cerrar

        time.sleep(intervalo)  # Esperar el intervalo especificado

# Llamar a la función
monitorear_precio(par, intervalo, porcentaje_arriba)  