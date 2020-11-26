def most_popular(description, my_dict):
    words = [x for x in description if len(x) > 6]
    for word in words:
        if word not in my_dict.keys():
            my_dict.update({word : 1})
        else:
            my_dict[word] += 1

def printMostPopular(my_dict):
    most_popular_words = sorted(list(my_dict.items()), key=lambda x: x[1], reverse=True)[:10]
    print(f'Самые популярные слова в новостях: ')
    for item in most_popular_words:
        print(f'{item[0]} - {item[1]} раз')