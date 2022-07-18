def read():
  numbers = []
  # ? with open() abre archivos de texto. "r" es para "Read", encoding="utf-8" es para leer caracteres especiales
  with open("./archivos/number.txt", "r", encoding="utf-8") as f:
    for line in f: # por cada linea en el archivo f.
      numbers.append(int(line))
  print(numbers)



def run ():
  pass



if __name__ == "__main__":
  run()