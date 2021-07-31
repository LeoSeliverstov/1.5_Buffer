class Buffer:
    def __init__(self):
        self.buffer = []
        # конструктор без аргументов

    def add(self, *a):
        self.buffer.extend(a)
        while len(self.buffer) >= 5:
            print(sum(self.buffer[0:5]))
            del self.buffer[0:5]
        # добавить следующую часть последовательности

    def get_current_part(self):
        return(self.buffer)
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    buf = Buffer()
    buf.add(1, 2, 3)
    buf.get_current_part()  # вернуть [1, 2, 3]
    buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
    buf.get_current_part()  # вернуть [6]
    buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
    buf.get_current_part()  # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
    buf.get_current_part()  # вернуть [1]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
