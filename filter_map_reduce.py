def run ():
  
  # * Filter, para devolver solo los numeros impares.

  my_list = [1, 4, 5, 6, 9, 13, 19, 21]


  impar = [ i for i in my_list if i % 2 != 0 ]
  print(impar)


  odd = list(filter(lambda x: x % 2 != 0, my_list)) # ? lamda son las funciones anonimas, y filter recibe 2 parametros el 1. una funcion y el 2. un iterable.
  print(odd)



  # * Map.
  # devolver una lista con los mismos numeros pero elevados al cuadrado.

  my_list2 = [1, 2, 3, 4, 5]

  squares = [ i ** 2 for i in my_list2]  # usando comprenhensions 
  print(squares)

  alCuadrado = list(map(lambda x : x ** 2, my_list2)) # ? map, usa 2 parametros, 1. una funcion anonima "Lambada", 2 el iterable para trabajar. 
  print(alCuadrado)


if __name__ == '__main__':
  run()