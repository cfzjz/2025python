import random, time


class Sort:
    def __init__(self, n):
        self.len = n
        self.arr = [0] * n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0, 99)

    def partition(self, left, right):
        arr = self.arr
        k = left
        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def qsort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.qsort(left, pivot - 1)
            self.qsort(pivot + 1, right)

    def adjust_max_heap(self, pos, length):
        arr = self.arr
        dad = pos
        son = pos * 2 + 1
        while son < length:
            if son + 1 < length and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1

            else:
                break

    def heap(self):
        arr = self.arr
        for i in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.len)
        arr[0], arr[self.len - 1] = arr[self.len - 1], arr[0]
        for i in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    def test_time_use(self, sortfunc, *args):
        start = time.time()
        sortfunc(*args)
        end = time.time()
        print(f'用时{end - start}')


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


def change_lower(str_n):
    return str_n.lower()


from operator import itemgetter, attrgetter


def use_sorted():
    my_list = 'This is a test string from Andrew'.split()
    print(my_list)

    print(sorted(my_list, key=str.lower))
    print(sorted(my_list, key=change_lower))

    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
    ]

    print(sorted(student_tuples, key=lambda x: x[2]))

    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]

    print(sorted(student_objects, key=lambda student: student.age))

    print('operator:')
    print(sorted(student_tuples, key=itemgetter(2)))
    print(sorted(student_objects, key=attrgetter('age')))
    print('多层：')
    print(sorted(student_tuples, key=itemgetter(1, 2)))
    print(sorted(student_tuples, key=lambda x: (x[1], -x[2]), reverse=True))

    print(sorted(student_objects, key=attrgetter('grade', 'age')))

    print('dict:')
    mydict = {'Li': ['M', 7],
              'Zhang': ['E', 2],
              'Wang': ['P', 3],
              'Du': ['C', 2],
              'Ma': ['C', 9],
              'Zhe': ['H', 7]}

    print(sorted(mydict.items(), key=lambda v: v[1][1]))

    print('dict_in_list')
    game_result = [
        {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
        {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
        {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
        {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]

    print(sorted(game_result, key=itemgetter('rating', 'name')))


if __name__ == '__main__':
    count = 10000
    my_sort = Sort(count)

    # print(my_sort.arr)
    # my_sort.qsort(0, 9)
    # print(my_sort.arr)
    my_sort.test_time_use(my_sort.qsort,0,count-1)
    # my_sort.heap()
    # print(my_sort.arr)
    # use_sorted()
