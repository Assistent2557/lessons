def get_answer(question):
    question = str(question).lower()
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока" : "Увидемся" }
    return answers[question]

result = get_answer(input('Введите текст: '))
print(result)