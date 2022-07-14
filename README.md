# python_intermedio

## Creando un ambiente virtual en python en Linux

__Creacion de ambiente virtual:__

`python3 -m venv nombre_venv`

__Activar el ambiente virtual:__

`source nombre_venv/bin/activate`

__Desactivar el entorno virtual:__

Estando en la carpeta del entorno virtual: 
`deactivate` 


## Usando pip en el entorno virtual 

__pip__ es el __npm__ de javascript

`pip freeze` nos muestra los modulos instalados

#### Mostrando las dependencias instaladas

`pip freeze > requierements.txt` Copia las dependecias instaladas en un archivo .txt para que los demas devs puedan instalarlas.