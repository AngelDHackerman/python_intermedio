def read():
  numbers = []
  # ? with open() abre archivos de texto. "r" es para "Read", encoding="utf-8" es para leer caracteres especiales
  with open("./archivos/number.txt", "r", encoding="utf-8") as f:
    for line in f: # por cada linea en el archivo f.
      numbers.append(int(line)) # * append() agregara el numero a la lista.
  print(numbers)


def write():
  names = ['Facundo', 'Angel', 'Miguel', 'Pepe', 'Christian', 'Rocio', 'Mañana']
  with open('./archivos/names.txt', 'a', encoding='utf-8') as f: # todo: 'w' es para sobrescribir, 'a' es para append, y Aqui se crea un nuevo archivo llamado names.txt
    for name in names:
      f.write(name) # * escribira en el archivo 'f' los nombres del array
      f.write('\n')


def run ():
  read()
  write()



if __name__ == "__main__":
  run()