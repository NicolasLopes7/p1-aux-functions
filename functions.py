def replace(string, target, value):
    newString = ''
    for i in range(0, len(string)):
        if string[i] == target:
            newString += value
            continue
        newString += string[i]

    return newString


def count(string, searchTerm):
    count = 0
    for i in range(0, len(string)):
        if string[i] == searchTerm:
            count += 1
    return count


def index(array, element):
    for i in range(0, len(array)):
        if array[i] == element:
            return i
    return -1


def map(array, mapper):
    mappedArray = []

    for i in range(0, len(array)):
        mappedArray.append(mapper(array[i]))

    return mappedArray


def sort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def extend(original, carry):
    return original + carry


def _in(array, element):
    found = False
    for i in range(0, len(array)):
        if array[i] == element:
            found = True
            break
    return found


def min(array):
    min = array[0]
    for i in range(0, len(array)):
        if array[i] < min:
            min = array[i]
    return min


def max(array):
    biggestItem = array[0]
    for i in range(0, len(array)):
        if array[i] > biggestItem:
            biggestItem = array[i]
    return biggestItem


def join(array, separator):
    joined = ''
    for i in range(0, len(array)):
        joined += str(array[i])
        if i < len(array) - 1:
            joined += separator
    return joined


def insert(array, position, element):
    newArray = []
    for i in range(0, len(array)):
        if i == position:
            newArray.append(element)
        newArray.append(array[i])
    return newArray


def remove(array, element):
    newArray = []
    for i in range(0, len(array)):
        if array[i] != element:
            newArray.append(array[i])
    return newArray


def reverse(array):
    newArray = []
    for i in range(len(array) - 1, -1, -1):
        newArray.append(array[i])
    return newArray


def clear(array):
    return []


def copy(array):
    newArray = [] + array
    return newArray


def slice(array, start, end):
    newArray = []
    for i in range(start, end):
        newArray.append(array[i])

    if isinstance(array, str):
        return join(newArray, '')

    return newArray


def sum(array):
    total = 0
    for i in range(0, len(array)):
        total += array[i]
    return total
