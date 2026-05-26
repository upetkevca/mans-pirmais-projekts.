# spelling.py

def spelling_task():
    score = 0

    print("\nPAREIZRAKSTĪBAS UZDEVUMI")

    tasks = [
        ("sk_ola", "skola"),
        ("zī_mulis", "zīmulis"),
        ("maš_na", "mašīna"),
        ("grā_ata", "grāmata"),
        ("dā_rzs", "dārzs"),
        ("maja", "māja"),
        ("gramata", "grāmata"),
        ("darzs", "dārzs"),
        ("riga", "Rīga"),
        ("latvija", "Latvija")
    ]

    for question, answer in tasks:
        user_answer = input(f"Izlabo vai pabeidz vārdu: {question} -> ")

        if user_answer.lower() == answer.lower():
            print("Pareizi!")
            score += 1
        else:
            print(f"Nepareizi! Pareizā atbilde: {answer}")

    return score
spelling_task()
