#1) Напишите функцию, которая принимает фразу, и возвращает его сокращеннуюm форму.


#2)





#3)def a(w):
def a(w):
    b1 = list(w)
    b2 = set(w)
    if len(b1) == len(b2):
        return True
    return False
print(a(""))
#4
def a(w):
 return int(str(w)[::-1])
 print(a(123))
                            #доп
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
chatbot()                       