
# def draw_line(symbol, length):
#     print(symbol * length)


def draw_line(symbol="*", length=40):
    """
    Функція виводить на stdout лінію, що складається з symbol * length
    """
    print(str(symbol) * length)

draw_line()
draw_line("#", 40)
draw_line("-")
draw_line("1", length=50)
draw_line(length=50, symbol="1")


















































# for _ in range(4):
#     draw_line()


