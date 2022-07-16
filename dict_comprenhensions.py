import math


def run():
  my_dict = {}

  # for i in range(1, 101):
  #   if i % 3 != 0:
  #     my_dict[i] = i ** 3

  # agregando solo los que NO son divisibles en 3 
  my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}  # todo: asi es la sintaxis de las dictionary comprehensions


  # agregando los numeros del 1 al 1000 con los valores que sean la raiz cuadrada de sus llaves
  my_dict_sqrt = {}
  my_dict_sqrt = {i: math.sqrt(i) for i in range(1, 201) }


  print(my_dict, '\n ')
  print(my_dict_sqrt)


if __name__ == '__main__':
  run()


# Reto 1: solamente guardar los numeros que no sean divisibles entre 3. 