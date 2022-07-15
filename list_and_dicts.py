def run():
  my_list = [1, 'hello', True, 4.5]
  my_dict = {'firstname': 'Angel', 'lastname': 'Hernandez'}

  super_list = [
    {'firstname': 'Angel', 'lastname': 'Hernandez'},
    {'firstname': 'Dario', 'lastname': 'Santiago'},
    {'firstname': 'Bender', 'lastname': 'Rodriguez'},
    {'firstname': 'Ricardo', 'lastname': 'Diaz'},
    {'firstname': 'Martin', 'lastname': 'Martinez'},
  ]

  super_dict = {
    'natural_nums': [1, 2, 3, 4, 5],
    'integer_nums': [-1, -2, 0, 1, 2],
    'floating_nums': [1.1, 4.5, 6.43],
  }

  for key, value in super_dict.items(): # ? Asi se imprimen los objetos en python
    print(key, ' ', value)

  for value in super_list:
    print(value.items()) # ? asi se recorren las listas

if __name__ == "__main__":
  run()