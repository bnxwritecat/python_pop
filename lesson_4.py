# #множества set, frozenset
# a =  [1,3,4,5]
# b = [3,4,5,6]
# print(list(set(a+b)))

# numbers = [1,2,3,4,5,6,7,8,9,2]
# print(numbers)
# # print(numbers[:: - 1]) не потлерживает срезы

# names = {"Askhat", "kurmanbek" , "Baha" , "Asylbek"}
# print(names)
# names.add("Nurik")    # добавлеение     Nurik в set множество
# print(names)
# names.remove("Askhat") # удаление ASKHAT из множество
# print(names)
# names.pop() # удаляем случайное значение
# print(names)
# # names.update("kurmanbek") # добавление Kurmavbek и делит по букавам
# names.clear() # очищаем set
# print(names)

# # lst = []
# # print (type(lst))
# # hello = ""
# # print(type(hello))
# # st = {}
# # print(type(st))
# lst = [10,4.0,False,"Geek",[1,2,3],{1,2,3}]
# print(lst)
# st = {1, 1.0, False , "1"}
# print(st)
# print(sorted())
# frzn = frozenset([1,2,3,4,5,6])
# print(frzn)
# frzn.remove(2)
# print(frzn)

# #Tuple = Кортеж 
# numbers = (1,10,11,2,4,3,4,5)
# print(numbers)
# tup = (1,1.0,True,"Hello",{1,2,3},(10,20))
# print(tup)
# print(tup.count("Hello"))
# print(tup[2])
# print(tup[0:3])

# cars = ("bmv","Mersedes","ferrari")
# print(cars)
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append("Tiko")
# print(lst_cars)
# cars = tuple(lst_cars)
# print(cars)

# tup = (10,)
# print(type(tup))

# student = {"student" : "Askhat","age": 18}
# print(student)
# print(len(student)) # выводим длину словаря student
# print(student["age"]) # по ключу age выводим значение с словами student
# student.setdefault('language','Python') # добавляем с словарь новый ключ и значение
# print(student)
# student.pop('age') #удаляем по ключ age и его значение
# print(student)
# student['languaage'] = 'JavaScrip' # обновляем по ключу значение
# print(student)
# student['place_study'] = "GeekTech" # Если нужного ключа нету то он добавляет его
# print(student)
# print(student.keys())
# print(student.values())

# contact = {'Askhat' : "0778909091"}
# while True:
#     command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Введите имя: ")
#         add_number = input("Введите номер: ")
#         if add_name not in contact:
#             contact.setdefault(add_name, add_number)
#             print("Успешно добавлено")
#         else:
#             print("Такой контакт уже существует")
#     elif command == "3":
#         delete_contact = input("Кого удалить?: ")
#         if delete_contact in contact:
#             contact.pop(delete_contact)
#             print("Успешно удалено")
#         else:
#             print("Такого контакта нету")
#     elif command == "3":
#         if add_name not in contact:
#             contact.setdefault(add_name,add_number)
#             print("успешно Обновлен")
                                     #дз
# 1) Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужнопревратить кортеж в список и добавить новое значение ‘Tesla’, затемпревращаете список обратно в кортеж       
# it_company = ("Gogle","Amazon","Microsoft")
# print(it_company)
# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company.append("Tesla")
# print(lst_it_company)
# it_company = tuple(lst_it_company)
# print(it_company)

#2)Из 1 задания попробуйте вывести индекс ‘Amazon

# it_company = ("Gogle","Amazon","Microsoft")
# print(it_company[1:2])

#3) Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способами

# it_company = ["Gogle","Amazon","Microsoft"]
# removed = it_company.pop(0)
# it_company = {"Amazon","Microsoft"}
# it_company.add('Apple')
# print(it_company)
# print(removed)

# 4) Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft’

# it_company = ['Apple','Amazon','Microsoft']
# print(it_company[0:3:2])

# 5)  Есть кортеж  вам нужно посчитать сколько раз встречается слово python независимо от регистра

# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview')
# print(text_tuple.count("python"))

# #6) Даны два словаря
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd':600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)
#7
# numbers = {'num_1' : 1, 'num_2' : 2,'num_3' : 3, 'num_100' : 100}
# print(numbers['num_1']*5,numbers['num_2']*5,numbers['num_3']*5,numbers['3']*5,numbers['num_100']*5,numbers['num_100']*5)


# #8
# student = {'name' : 'Askhat', 'age' : 17}
# print(student['age']*2)

# #9
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student['age'])

# #10
# student =('name': 'Askhat','age':17)
# student.pop['age']
# print[student]

#11
# student = {'name' : 'Askhat'}
# student.pop('age')
# print(student)

#12
#             proverka_paroly = input("введите повторный пароль:")
#             if parol['first_p'] == proverka_paroly:
#                 print("ok")
#             else:
#                 print("различаються")
#         else:
#             print("простой пароль")
#     else:
#         print("короткий пароль")
#     print(parol)
#13
# contact = ["Askhat"]
# while True:
#     command = input("1-посмотреть контакт, 2-добавить в контакты, 3-удалить контакты, 4-обновить контакт")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         app_contact = input("Введите имя: ")
#         contact.append(app_contact)
#         print("Удачно добавлен")
#     elif command == "3":
#         pop_contact = input("Введите имя человека которого хотите удалить: ").title()
#         if pop_contact in contact:
#             contact.remove(pop_contact)
#             print("контакт удален")
#         else:
#             print("контакт не найден")
#     elif command == "4":
#         star_name = input("Введите старое имя: ")
#         new_name = input("Введите новые имя: ")
#         try:
#             contact[contact.index(star_name)] = new_name
#             print("контакт обновлен")
#         except ValueError:
#             contact.append(new_name)
#             print("был создан новый контак")
#     else:
#         print("err")
#         break
