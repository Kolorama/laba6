points = {
    1: ["а", "в", "е", "и", "н", "о", "р", "с", "т"],
    2: ["д", "к", "л", "м", "п", "у"],
    3: ["б", "г", "ё", "ь", "я"],
    4: ["й", "ы"],
    5: ["ж", "з", "х", "ц", "ч"],
    8: ["ш", "з", "ю"],
    10: ["ф", "щ", "ъ"]
}
x = input("Ваше число")
x = list(x)
d = 0
for i in x:
    for k in points:
        if i in points[k]:
            d = d + k
print("Ваше слово стоит ", d, "балла(-ов)")