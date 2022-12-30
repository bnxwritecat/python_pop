import random
language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
def random_word(language1):
    random_vybor = random.choice(language1)
    with open('styh.txt', 'a+') as k:
        k.write(f"{random_vybor}\n")
random_word(language)
############################ 2
f = open('text.txt', 'w')
f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsumhas been the industrs standard dummy text ever since the 1500s, when an unknownprinter took a galley of type and scrambled it to make a type specimen book. It hassurvived not only five centuries, but also the leap into electronic typesetting, remainingessentially unchanged. It was popularized in the 1960s with the release of Letrasetsheets containing Lorem Ipsum passages, and more recently with desktop publishingoftware like Aldus PageMaker including versions of Lorem Ipsum.')
f.close()
############################### 3 
with open('text.txt', 'w')as f:
    f.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsumhas been the industrs standard dummy text ever since the 1500s, when an unknownprinter took a galley of type and scrambled it to make a type specimen book. It hassurvived not only five centuries, but also the leap into electronic typesetting, remainingessentially unchanged. It was popularized in the 1960s with the release of Letrasetsheets containing Lorem Ipsum passages, and more recently with desktop publishingoftware like Aldus PageMaker including versions of Lorem Ipsum.\n')
############################ доп
with open('text.txt', 'r')as f,open('styh.txt', 'r')as v,open('wikipedia.txt', 'a+') as k:
    for i in f:
        k.write(i)
    for j in v:
        k.write(j)

