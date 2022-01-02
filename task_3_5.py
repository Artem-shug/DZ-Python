
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
    for i in range(n):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        print(joke)
        list_2 = []
        if flag == True:
            list_2 = joke.split()
            for noun in nouns:
                for i in list_2:
                    if noun == i:
                        nouns.remove(noun)

            for adverb in adverbs:
                for i in list_2:
                    if adverb == i:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for i in list_2:
                    if adjective == i:
                        adjectives.remove(adjective)

get_jokes(5, flag=True)

