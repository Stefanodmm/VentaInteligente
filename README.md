# VentaInteligente
## Version 1:
* Sistema de calculo de cierre de operacion, en donde, calcula la subida de un precio (operacion long) y te dice cuando cerrar la operacion cuando el precio de la moneda baja un % editable por el usuario, mientras el precio de la moneda siga subiendo y la variacion del precio sea menor a ese %, no cerrara, pero cuando el precio baje al precio de cierre determinado por ese %, te dira que cierres operacion. Es recomendable usar esta funcion, unicamente despues de que una moneda llegue a un precio de tp en un bot automatizado, y no usarlo desde el inicio de la operacion, ya que puede afectar el rendimiento de la misma.
