from sqlite3 import DatabaseError


DATA = [ # ? DATA  es mayusculas quiere decir que es una constante.
  {
      'name': 'Facundo',
      'age': 72,
      'organization': 'Platzi',
      'position': 'Technical Coach',
      'language': 'python',
  },
  {
      'name': 'Luisana',
      'age': 33,
      'organization': 'Globant',
      'position': 'UX Designer',
      'language': 'javascript',
  },
  {
      'name': 'Héctor',
      'age': 19,
      'organization': 'Platzi',
      'position': 'Associate',
      'language': 'ruby',
  },
  {
      'name': 'Gabriel',
      'age': 20,
      'organization': 'Platzi',
      'position': 'Associate',
      'language': 'javascript',
  },
  {
      'name': 'Isabella',
      'age': 30,
      'organization': 'Platzi',
      'position': 'QA Manager',
      'language': 'java',
  },
  {
      'name': 'Karo',
      'age': 23,
      'organization': 'Everis',
      'position': 'Backend Developer',
      'language': 'python',
  },
  {
      'name': 'Ariel',
      'age': 32,
      'organization': 'Rappi',
      'position': 'Support',
      'language': '',
  },
  {
      'name': 'Juan',
      'age': 17,
      'organization': '',
      'position': 'Student',
      'language': 'go',
  },
  {
      'name': 'Pablo',
      'age': 32,
      'organization': 'Master',
      'position': 'Human Resources Manager',
      'language': 'python',
  },
  {
      'name': 'Lorena',
      'age': 56,
      'organization': 'Python Organization',
      'position': 'Language Maker',
      'language': 'python',
  },
]

def run ():

  all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
  all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
  adults = list(filter(lambda worker: worker["age"] > 18, DATA))
  adults_name = list(map(lambda adulto: adulto["name"], adults))
  old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) # ? | es el pipe operator, solo funciona con python3.9 y suma los diccionarios de la funcion lambda

  
  for worker in all_python_devs:
    print(worker)

  
  print('\n')
  for worker in all_Platzi_workers:
    print(worker)


  print('\n')
  for adult in adults_name:
    print(adult)

  print('\n')
  for worker in old_people:
    print(worker) # ! Le agrego True o False a los elementos del diccionario original si eran mayores a 70 años 


if __name__ == '__main__':
  run()
