from list_and_dicts import run


def run():
  # squares = []
  # for i in range(1,101):
  #   squares.append( i ** 2)

  squares = [i ** 2 for i in range(1, 100) if i % 3 != 0] # * Estas son las comprehention list
  # ?    [element for element in interable if condition]

  print(squares)


if __name__ == "__main__":
  run()

# solamente guardar el cuadrado de los numeros que NO sean divisibles entre 3 