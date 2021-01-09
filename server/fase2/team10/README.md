# Server
+ Tiene como objetivo almacenar y transimitir peticiones del cliente desktop.
+ SO: Windows
 

## Librerias

```python
import socket
import sys
import json
import analizer.interpreter as interpreter
```

## Configuración de puerto

```python
serv_add = ('localhost', 10000)
serv.bind(serv_add)
serv.listen(1)
```


## Conexión
```python
while True:
    print("waiting for connection")
    connection, client_address = serv.accept()
```

+ Recibe la data del cliente que en este caso serian los querys, realiza el proceso del parser y retorna el resultado en un objeto json
```python
 try:
        print(client_address)
        while True:
            data = connection.recv(4096)
            print(data.decode('utf-8'))
            #recibimos el script del query tool y la decodificamos a utf 8 
            scritp_sql = data.decode('utf-8')
            #Realiza la interpretacion
            obj = interpreter.execution(scritp_sql)
            temp = {"obj": obj, "databases":importFile("Databases")} 
            json_data = json.dumps(temp, sort_keys=False, indent=2)
            #Imprimimos el json desde el server
            print("data %s" % json_data)
            if data:
                #mandamos la data obtenida del analisis como obj json
                connection.sendall(json_data.encode())
            else:
                print("end data")
                break
```

+ Se cierra la conexión
```python
    finally:
        connection.close()
```



## Método que permite leer la data en el archivo json

```python
def importFile(name):
    try:
        with open("./" + name + ".json", "r") as file:
            databases = json.load(file)
            return databases
    except:
        if name == "Databases":
            return []
        return {}
```

## Archivo json a leer
+ Contiene los datos de las bases de datos creadas 

```py
[
    {
        "name": "g",
        "mode": 1,
        "owner": null,
        "tables": []
    },
    {
        "name": "prueba",
        "mode": 1,
        "owner": null,
        "tables": []
    },
    {
        "name": "prueba2",
        "mode": 1,
        "owner": null,
        "tables": []
    },
    {
        "name": "prueba3",
        "mode": 1,
        "owner": null,
        "tables": []
    },
    {
        "name": "prueba4",
        "mode": 1,
        "owner": null,
        "tables": []
    }
]
```




### Comando para iniciar servidor
```
python server.py
```


