import re


def data_verification(arr: list):
    pattern = r"^(?:[а-яё]+[А-ЯЁ][а-яё]*|[а-яё]*[А-ЯЁ][а-яё]+)$"
    result = []

    for i in arr:
        match = re.match(pattern, i)
        if match:
            result.append(match[0])
    return result


array = ["Мама",
         "авТо",
         "гриБо",
         'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО',
         "агент007",
         "стриж",
         "ГТО",
         "Три богатыря"
         ]
print(data_verification(array))
