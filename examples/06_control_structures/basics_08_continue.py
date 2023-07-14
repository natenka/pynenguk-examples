# Приклад із циклом for
for num in range(5):
    if num == 3:
        continue
    else:
        print(num)


# Приклад із циклом while
i = 0

while i < 6:
    i += 1
    if i == 3:
        print("Пропускаємо 3")
        continue
        print("Це ніхто не побачить")
    else:
        print("Поточне значення: ", i)
