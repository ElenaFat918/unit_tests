import numbers


class ListOfNum:
    def __init__(self, lst):
        self.lst = lst

    def __check_list(self):
        cor_list = True
        for value in self.lst:
            cor_list *= isinstance(value, numbers.Number)  # а - истинно или в - истинно или с - истинно
        return cor_list

    def average_list(self):
        if self.__check_list() and len(self.lst) > 0:
            return sum(self.lst) / len(self.lst)
        else:
            return 0


def compare_avgs(lst_1, lst_2):
    if str(lst_1.average_list()) != '0' and str(lst_2.average_list()) != '0':
        if lst_1.average_list() == lst_2.average_list():
            return f'Средние значения равны'
        elif lst_1.average_list() > lst_2.average_list():
            return f'Первый список имеет большее среднее значение'
        else:
            return f'Второй список имеет большее среднее значение'
    else:
        return f'Эти списки нельзя сравнить'

#
# if __name__ == '__main__':
#     l = ListOfNum([1, -1])
#     w = ListOfNum([])
#     print(l.average_list())
#     print(w.average_list())
#     print(compare_avgs(l, w))