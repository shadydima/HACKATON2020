zagadki= [  {"text" : "сто одежек и все без застежек","answer" : "лук"} , {"text" : "На зелёной хрупкой ножке вырос шарик у дорожки","answer" : "одуванчик"},{"text" : "Мягкие лапки, а в лапках царапки","answer" : "кошка"}]
def run(zagadki):
    i=0
    while(i<=2)
        print("Первая загадка", zagadki[i]["text"])
        print("Выведи ответ")
        ans1=input()
        if ans1==zagadki[i]["answer"] :
            print("Ты отгадал!")
        else:
            print("Ты не отгадал")
