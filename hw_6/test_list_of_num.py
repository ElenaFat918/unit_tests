import pytest

from list_of_num import *


@pytest.fixture
def dif_lists():
    return ['a', 2, 3, 4, 5], [], [1, 2, 3, 4, 5], [5, 4, 3, 2, 0], [6, 7, 8, 9, 10]

def test_list(dif_lists):
    # Проверяем объект "Список значений"
    lst_error, lst_empty, lst, *box = dif_lists
    lst_test = ListOfNum(lst_error)
    assert lst_test.average_list() == 0, 'return value error'
    lst_test = ListOfNum(lst_empty)
    assert lst_test.average_list() == 0, 'return value error'
    lst_test = ListOfNum(lst)
    assert lst_test.average_list() == 3.0, 'return value error'


def test_compare_avgs(dif_lists):
    # Проверяем сравнение средних значений
    _, lst_empty, lst_1, lst_2, lst_3 = dif_lists
    assert compare_avgs(ListOfNum(lst_1), ListOfNum(lst_empty)) ==\
           'Эти списки нельзя сравнить', 'Результаты не совпадают'
    assert compare_avgs(ListOfNum(lst_1), ListOfNum(lst_1)) ==\
           'Средние значения равны', 'Результаты не совпадают'
    assert compare_avgs(ListOfNum(lst_1), ListOfNum(lst_2)) ==\
           'Первый список имеет большее среднее значение', 'Результаты не совпадают'
    assert compare_avgs(ListOfNum(lst_1), ListOfNum(lst_3)) ==\
           'Второй список имеет большее среднее значение', 'Результаты не совпадают'
