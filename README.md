# Evaluación Flask: Carrito de compras

En este ejercicio deberán completar la app correspondiente a un minisuper, la cual consiste en un carrito de compras. La app se encuentra incompleta y deberá completar algunos puntos.

## Configurar el entorno virtual

Para configurar el entorno para correr la app, antes de comenzar, deberá realizar los siguientes pasos:

1. Crear un entorno virtual para la aplicación:
```
python -m virtualenv venv
```
2. Activar el entorno virtual
3. Instalar las dependencias necesarias. El siguiente comando permitirá instalar todas las dependencias listadas en el archivo "requirements.txt"
```
python -m pip install -r requirements.txt
```
4. Una vez realizados estos pasos, puede ejecutar la aplicación mediante el comando ```run.bat```


## Completar los puntos faltantes

Como se dijo anteriormente, la app se encuentra incompleta faltando desarrollar los siguientes puntos:

1. Implemente el endpoint "/nosotros" referenciado por el menú de navegación. La plantilla coente (nosotros.html) ya tiene el contenido correspondiente, pero faltan algunas directivas para que la sección se visurrespondialice correctamente, es decir, junto con el resto de los elementos de la página (header, nav, etc.).

2. Crear un modelo para el formulario de ingreso para los datos de un nuevo producto llamado **FormularioCompra**.
    * El formulario debe tener dos campos: *nombre* y * cantidad*
    * El campo *nombre* corresponde al nombre del producto que se desea agregar al carrito. Es de tipo String y debe contar con las siguientes validaciones:
        - El campo es requerido.
    * El campo *cantidad* corresponde a la cantidad de unidades de un determinado tipo de producto que se desea agregar al carrito. Es de tipo Integer y debe contar con las siguientes validaciones:
        - El campo es requerido.
        - El campo debe ser un número entre 1 y 20.

3. En el endpoint "/agregar":
    * Valide que el formulario contenga datos válidos.
    * Si el formulario contiene datos válidos, obtenga los datos (nombre y cantidad) y colóquelos en un diccionario llamado "producto" que será luego agregado al arreglo de compras.

4. En el endpoint "/", implemente los cambios necesarios para que se muestre la lista de los productos (y sus cantidades) agregadas al carrito.

5. **Sólo para picantes**: el endpoint "/", implemente los cambios necesarios para que, al final de la lista, se muestre la cantidad total de productos (teniendo en cuenta las cantidades) agregadas al carrito.