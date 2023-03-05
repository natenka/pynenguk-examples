# -*- coding: utf-8 -*-
from pprint import pprint
import sqlite3
import create_sw_inventory_ver2_functions as dbf

# MAC-адрес sw7 совпадает с MAC-адресом коммутатора sw3 в списке data
data2 = [
    ("0055.AAAA.CCCC", "sw5", "Cisco 3750", "London, Green Str"),
    ("0066.BBBB.CCCC", "sw6", "Cisco 3780", "London, Green Str"),
    ("0000.AAAA.DDDD", "sw7", "Cisco 2960", "London, Green Str"),
    ("0088.AAAA.CCCC", "sw8", "Cisco 3750", "London, Green Str"),
]


def write_rows_to_db(connection, query, data, verbose=False):
    """
    Функция ожидает аргументы:
     * connection - соединение с БД
     * query - запрос, который нужно выполнить
     * data - данные, которые надо передать в виде списка кортежей

    Функция пытается записать поочереди кортежи из списка data.
    Если кортеж удалось записать успешно, изменения сохраняются в БД.
    Если в процессе записи кортежа возникла ошибка, транзакция откатывается.

    Флаг verbose контролирует то, будут ли выведены сообщения об удачной
    или неудачной записи кортежа.
    """
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as e:
            if verbose:
                print(
                    "При записи данных '{}' возникла ошибка".format(", ".join(row), e)
                )
        else:
            if verbose:
                print("Запись данных '{}' прошла успешно".format(", ".join(row)))


con = dbf.create_connection("sw_inventory3.db")

query_insert = "INSERT into switch values (?, ?, ?, ?)"
query_get_all = "SELECT * from switch"

print("\nПроверка текущего содержимого БД")
pprint(dbf.get_all_from_db(con, query_get_all))

print("-" * 60)
print("Попытка записать данные с повторяющимся MAC-адресом:")
pprint(data2)
write_rows_to_db(con, query_insert, data2, verbose=True)
print("\nПроверка содержимого БД")
pprint(dbf.get_all_from_db(con, query_get_all))

con.close()
