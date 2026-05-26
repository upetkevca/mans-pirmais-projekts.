# spelling.py

def spelling_task():
    score = 0

    print("\nPAREIZRAKSTĪBAS UZDEVUMI")

    word1 = input("Ievieto trūkstošo burtu: sk_ola -> ")

    if word1.lower() == "skola":
        print("Pareizi!")
        score += 1
    else:
        print("Nepareizi! Pareizā atbilde: skola")

    word2 = input("Izlabo vārdu: zimulis -> ")

    if word2.lower() == "zīmulis":
        print("Pareizi!")
        score += 1
    else:
        print("Nepareizi! Pareizā atbilde: zīmulis")

    return score
spelling_task()