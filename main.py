def p_or_s(num1:int , num2:int) ->int: 
    operator = input("P or S:") 
    if operator == "P": 
        print ((2*num1) + (2*num2)) 
    elif operator == "S": 
        print(num1*num2) 
    else: 
        print("Неправильный оператор!!!")
#####################
lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
def a():
    return lst[::-1]
#############################
def time():
    hours = 7
    minut = 30
    second = 59
    def ask(hours, minut,second):
        return {hours * 3600 + minut * 60 + second}
    print(ask(hours,minut,second))
##########################
def chatbot():
    while True:
        text=input("Введите что-то:")
        if text.find("?")>=0:
            print("Конечно!")
        elif text.find("!")>=0:
            print("Успокойся")
        elif text == "":
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("Ну и что")
########################
def asko(b):
    c = b.title().split()
    for i in range(len(c)):
        print(c[i][0], end='')
#############################
menu = {
'beefstrogonoff': 350,
'burger': 200,
'meatloaf': 500,
'chicken pot pie': 400,
'beefshteks': 650}
new_menu = {k: v + 50 for k, v in menu.items()}

