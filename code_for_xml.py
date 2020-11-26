import xml.etree.ElementTree as ET
# Импортируем функции из другого файла
from function_most_popular import most_popular
from function_most_popular import printMostPopular
# Создадим parser, дерево XML и найдем текст новостей
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
items = root.findall('channel/item')
# Создадим словарь, в который будем записывать ключ = слово, значение = счетчик слова
news_dict = {}
# Для каждой новости запишем в news_dict слова с необходимым усоловием по длине и количеством этих слов. Если слова будут повторяться, то счетчик будет увеличиваться
for item in items:
    new_item = item.find('description').text.split()
    most_popular(new_item, news_dict)
# Отсортируем полученый словарь по значению (счетчику) и выведем сообщение в консоль
printMostPopular(news_dict)
