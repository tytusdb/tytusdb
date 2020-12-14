# TYPE CHECKER

## Funcionalidad:
Verificar que el tipo de dato que se va a insertar en las columnas de una tabla y retornar si se debe o no realizar la operación. 

Los parámetros que utiliza el type checker son: 
* Lista de parámetros a buscar 
* Lista de los valores que se quieren insertar

### Ejemplo de uso:
*INSERT INTO nombreTabla VALUES(123,"hola");*

*INSERT INTO nombreTabla(id, nombre) VALUES(123,"hola");*

*UPDATE SET id = 123, nombre = "hola" ;*

### Parámetros que recibe:
**Tipos:**

Array con objetos tipes, los cuales contienen la metadata tipo, id, fila y columna.

*types = [t1, t2, ... , tn]*

**Valores:**

Array en donde se tendrán objetos tipo value, el cual continene la metadata de su tipo, valor, fila y columna.

*values =[v1,v2, ..., vn]*

### Algoritmo propuesto:

```
def check(types,values):
      index = 0
      error = false
      while index < types.length
            if types[index].type != values[index].type
                error = true
                errores.push("No coincide el tipo de la columna" + types[index].id + " de la tabla y el valor " + values[index].value + " en la fila " + values[index].row + " y columna " + values[index].column)
            index+=1
      return error
```