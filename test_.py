import functions


def test_replace():
    assert functions.replace('ooo', 'o', 'b') == 'bbb'
    assert functions.replace('batata', 'a', 'o') == 'bototo'


def test_count():
    assert functions.count('ooo', 'o') == 3
    assert functions.count('batata', 'a') == 3


def test_index():
    assert functions.index(['a', 'b', 'c'], 'b') == 1
    assert functions.index(['a', 'b', 'c'], 'd') == -1


def test_map():
    def square(x):
        return x**2

    assert functions.map([1, 2, 3], square) == [1, 4, 9]


def test_sort():
    assert functions.sort([3, 1, 2]) == [1, 2, 3]
    assert functions.sort([1, 3, 2]) == [1, 2, 3]


def test_extend():
    assert functions.extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_in():
    assert functions._in([1, 2, 3], 1) == True
    assert functions._in([1, 2, 3], 4) == False


def test_max():
    assert functions.max([1, 2, 3]) == 3
    assert functions.max([10, 2, 1]) == 10


def test_min():
    assert functions.min([1, 2, 3]) == 1
    assert functions.min([10, 2, -1]) == -1


def test_join():
    assert functions.join([1, 2, 3], ',') == '1,2,3'
    assert functions.join([3, 2, 1], ',') == '3,2,1'


def test_insert():
    assert functions.insert(['apple', 'banana', 'cherry'], 1, 'orange') == [
        'apple', 'orange', 'banana', 'cherry']


def test_remove():
    assert functions.remove(['apple', 'banana', 'cherry'], 'banana') == [
        'apple', 'cherry']


def test_reverse():
    assert functions.reverse([1, 2, 3]) == [3, 2, 1]
    assert functions.reverse(['eae', 'pae']) == ['pae', 'eae']


def test_clear():
    assert functions.clear([1, 2, 3]) == []


def test_copy():
    originalArray = [1, 2, 3]
    newArray = functions.copy(originalArray)
    newArray.append(1)
    assert originalArray == [1, 2, 3]


def test_slice():
    assert functions.slice([1, 2, 3], 1, 2) == [2]
    assert functions.slice('nicolas', 1, 7) == 'icolas'


def test_sum():
    assert functions.sum([30, 40, 50]) == 120

def test_split():
    assert functions.split('eae','') == ['e','a','e']
    assert functions.split('e a e',' ') == ['e','a','e']