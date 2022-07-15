
      # * solamente guardar el cuadrado de los numeros que NO sean divisibles entre 3 

def run():
  # squares = []
  # for i in range(1,101):
  #   squares.append( i ** 2)

  squares = [i ** 2 for i in range(1, 100) if i % 3 != 0] # ? Estas son las comprehention list
  # ?    [element for element in interable if condition]

  print(squares)

      # * crear una lista de todos los multiplos de 4 que sean multiplos de 6 y multiplos de 9 pero solamente hasta 5 digitos
      # * el percentil es 36 porque es el factor comun de 4, 6 y 9.

  squares = [ i for i in range(1, 100000) if i % 36 == 0]
  print(squares)






if __name__ == "__main__":
  run()