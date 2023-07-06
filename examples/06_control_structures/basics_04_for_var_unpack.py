items = [[1, 100], [2, 200], [3, 300]]

# розпакування у змінні всередині циклу
for item in items:
    i1, i2 = item
    print(i1, i2)

# розпакування у змінні в циклі for
for i1, i2 in items:
    print(i1, i2)


london = {"name": "London1", "location": "London Str", "vendor": "Cisco"}

# перебираємо ключі словника, значення отримаємо всередині циклу
for key in london:
    value = london[key]
    print(key, value)

# перебираємо елементи items, розпакування у змінні всередині циклу
for item in london.items():
    key, value = item
    print(key, value)

# розпакування items у змінні в циклі for
for key, value in london.items():
    print(key, value)
