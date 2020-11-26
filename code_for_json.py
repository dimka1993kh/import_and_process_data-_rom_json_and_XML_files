import json
# Импортируем функции из другого файла
from function_most_popular import most_popular
from function_most_popular import printMostPopular
# Найдем текст всех новостей
with open('newsafr.json', encoding='utf-8') as f:
    data = json.load(f)
descriptions = data['rss']['channel']['items']
# Создадим словарь, в который будем записывать ключ = слово, значение = счетчик слова
news_dict = {}
# Для каждой новости запишем в news_dict слова с необходимым усоловием по длине и количеством этих слов. Если слова будут повторяться, то счетчик будет увеличиваться
for description in descriptions:
    new_item = description['description'].split(' ')
    most_popular(new_item, news_dict)
# Отсортируем полученый словарь по значению (счетчику) и выведем сообщение в консоль
printMostPopular(news_dict)

