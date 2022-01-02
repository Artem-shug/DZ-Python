

def thesaurus(*args):
    names = [*args]
    dict_names = {}
    for name in names:
        res = name[0]
        if res in dict_names:
            dict_names[res].append(name)
        else:
            dict_names[res] = [name]
    sort_dict_names = dict(sorted(dict_names.items(), key = lambda x:x[0]))

    return sort_dict_names

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Артем", "Дмитрий"))

