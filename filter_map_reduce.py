def run ():
  
  # ? Filter, para devolver solo los numeros impares.

  my_list = [1, 4, 5, 6, 9, 13, 19, 21]
  odd = list(filter(lambda x: x % 2 != 0, my_list)) # lamda son las funciones anonimas, y filter recibe 2 parametros el 1. una funcion y el 2. un iterable.
  print(odd)


  # ? Map.
  # devolver una lista con los mismos numeros pero elevados al cuadrado.

  


if __name__ == '__main__':
  run()