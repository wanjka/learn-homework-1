"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
NO_ANSW_CODE = 0

GREET_MSG = 'Здравствуй, Путник!\nМного лет ты бесплодно рыскал по пустыням Интернета в поисках абсолютного знания, пока не\nпришёл ко мне. Задай, наконец, свои вопросы. Что тебя беспокоит?'
NO_ANSW_MSG = 'На твой вопрос не знаю я ответа'

def ask_user_dict():
    default_dict = {
        "как дела": "Прекрасно!",
        "что делаешь": "Исправно работаю",
        "может, сходим куда-нибудь": "Извини, сегодня не могу...",
        "в чём смысл жизни": "42",
    }
    print(GREET_MSG)
    while True:
        query = input('Пользователь: ').lower().replace('?', ' ').strip()
        response = default_dict.get(query, NO_ANSW_CODE)
        if response == NO_ANSW_CODE:
            print('Программа: ' + NO_ANSW_MSG)
        else:
            print('Программа: ' + response)

if __name__ == "__main__":
    ask_user_dict()
