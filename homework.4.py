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
