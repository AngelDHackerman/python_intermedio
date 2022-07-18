
# todo: Los asserts se traducen como las afirmaciones, su sintaxis es: assert: condition, error message

def divisors(num):
  divisors = []
  for i in range(1, num + 1):
    if num % i == 0:
      divisors.append(i)
  return divisors

def run():
  num = input('Ingresa un numero: ')
  assert num.isnumeric(), "Debes ingresar un numero"  # ? .isnumeric() Nos dice si el input recibe un numero en forma de string algo como  '5' o '10'
  print(divisors(int(num)))   # ? Debido a .isnumeric() hasta aqui casteamos el string a un numero.
  print('Termino mi programa')


if __name__ == "__main__":
  run()

