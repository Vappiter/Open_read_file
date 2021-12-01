from pprint import pprint
import os
cook_book = {}
def get_shop_list_by_dishes():
    pass
def get_cook():
    pass
def My_input():
  """Function input processing"""
  var_input = input (f"\n Добрый! Данное приложение по кулинарной книги.\n\
Приложение поддерживает следующие команды:\n\
R - считать книгу рецептов из файла\n\
L - показать рецепты содержащиеся в книге\n\
A - добавить рецепт\n\
S - расчитатaь количество ингредиентов на количество гостей\n\
D - удалить рецепт\n\
Q - выйти из приложения\
\n Введите команду: ")
  var_input = var_input.upper()
  if var_input == 'R':
    file_read()
  elif var_input == 'A':
    add_cook()
  elif var_input == 'S':
    pass
  elif var_input == 'D':
    pass
  elif var_input == 'L':
   list_cook()
  elif var_input == 'Q':
    exit()
  else:
    print ('\n Вы ввели не правильную команду!!! \n')  
def file_read():
   count_plus = 0 
   os.chdir ("Z:\\2021-09-23_PYTHON\\Open_read_file")
   with open('recipes.txt', encoding='utf-8') as file_read:
        for work in file_read:
            name_cook = work.strip()
            if name_cook in cook_book:
             print(f'\nРецепт {name_cook} уже присутствует в книге')
             count_ingredient = int(file_read.readline().strip())
             for i1 in range (count_ingredient):    
               file_read.readline() 
             file_read.readline()  
            else: 
              count_plus += 1  
              count_ingredient = int(file_read.readline().strip())
              temp_data= []
              for i1 in range (count_ingredient):
                ingredient_name, quantity, measure = file_read.readline().split('|')
                temp_data.append ( {'ingredient_name':ingredient_name.strip(),'quantity':int(quantity.strip()), 'measure':measure.strip()})
                cook_book[name_cook] = temp_data
              file_read.readline()  
        print (f'\n Из файла перенесено в книгу {count_plus} рец.\n')    
def list_cook():
  if len(cook_book) == 0:
      print (f'Необходимо сначало считать рецепты из файла рецептов или ввести рецепт')  
  else:
      cook = cook_book.keys()   
      print ('Книга содержит такие рецепты:\n')
      i1 = 1
      for cook in cook_book.keys():
        print (f'{i1}. Рецепт {cook}')  
        i1+=1
def add_cook():
    temp_data = []
    var_name_cook = input('Введите название блюда:')        
    count_ingredient = int(input('Введите количество ингредиентов используемых в блюде:'))
    for i1 in range(count_ingredient):    
        ingredient_name = input('Введите наименование ингредиента:')
        quantity = input('Введите количество ингредиента:')
        measure = input('Введите единицу измерения ингредиента:')
        temp_data.append ( {'ingredient_name':ingredient_name.strip(),'quantity':int(quantity.strip()), 'measure':measure.strip()})
        cook_book[var_name_cook] = temp_data
    print (f'\n Рецепт {var_name_cook} добавлен в книгу рецептов.\n')    
    var_add_file = input ('\n Добавить рецепт в файл (Y/N)')    
    var_add_file =  var_add_file.upper()
    if var_add_file == 'Y':
      os.chdir ("Z:\\2021-09-23_PYTHON\\Open_read_file")  
      with open('recipes.txt', 'a', encoding='utf-8') as file_wr:
          file_wr.write ('\n')
          file_wr.write(var_name_cook + '\n')
          file_wr.write(str(count_ingredient) + '\n')
          for i1 in range(count_ingredient): 
            ingredient_name, quantity, measure = cook_book[var_name_cook][i1].values()
            file_wr.write(ingredient_name + '|' + str(quantity) + '|' + measure + '\n')       
    else:
        print (f'\n Рецепт {var_name_cook} не добавлен в файл рецептов.\n')
def del_cook():
#   if len(cook_book) == 0:
#       print (f'Книга рецептов пуста')  
#   else:
#       cook = cook_book.keys()   
#       print ('Книга содержит такие рецепты:\n')
#       i1 = 1
#       for cook in cook_book.keys():
#         print (f'{i1}. Рецепт {cook}')  
#         i1+=1          
#       var_del_cook = input('Какой рецепт удаляем, введите его №:')
  pass    

if __name__ == '__main__':
    while My_input() != "Q":
        My_input()
       
        