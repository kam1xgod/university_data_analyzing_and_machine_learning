import numpy as np


def print_task(number):
    print(f'\n\n\n--------------------------\n\t\t\t{number}\n--------------------------\n')


if __name__ == '__main__':
    # task 1.
    print_task(1)
    array = np.arange(1, 11, 1)
    print("array: \n", array)

    # task 2.
    print_task(2)
    arrayFact = np.cumsum(array)
    print("array's factorial: ", arrayFact)

    # task 3.
    print_task(3)
    arrayReverse = array[::-1]
    print("reversed array: \n", arrayReverse)

    # task 4.
    print_task(4)
    array = np.arange(-10, 11, 1)
    print("new array: \n", array)
    lessThenZero = array < 0
    lessThenZero = np.sum(array[lessThenZero])
    print("sum of els < 0: ", lessThenZero)
    biggerThenZero = array > 0
    biggerThenZero = np.sum(array[biggerThenZero])
    print("sum of els > 0: ", biggerThenZero)

    # task 5.
    print_task(5)
    array = np.random.randint(1, 100, [5, 5])
    print("new array: \n", array)
    minEl = np.min(array)
    print("array's min el: ", minEl)
    maxEl = np.max(array)
    print("array's max el: ", maxEl)
    arrayMean = np.mean(array)
    print("array's mean: ", arrayMean)

    # task 6.
    print_task(6)
    array = np.random.randint(1, 26, [5, 5])
    print("new array: \n", array)

    # task 7.
    print_task(7)
    rowsMin = np.argmin(array, 1).reshape(5, 1)
    rowsMax = np.argmax(array, 1).reshape(5, 1)
    rowsMin = np.take_along_axis(array, rowsMin, 1)
    rowsMax = np.take_along_axis(array, rowsMax, 1)
    print("every row's min: \n", rowsMin)
    print("every row's max: \n", rowsMax)

    # task 8.
    print_task(8)
    # array4RowsMinTrans = rowsMin.reshape(5, 1)
    # array4RowsMaxTrans = rowsMax.reshape(5, 1)
    array = (array - rowsMin) / rowsMax
    print("normalized array: \n", array)
    
    # quest 9.
    print_task(9)
    array = np.random.randint(0, 101, 10)
    print("new array: \n", array)
    array[np.argmin(array)] = 0
    array[np.argmax(array)] = 100
    print("edited array (min = 0; max = 100): \n", array)

    # quest 10.
    print_task(10)
    array = np.array([[1, 1],  # x1, y1
                      [4, 5]])  # x2, y2
    print("new array: \n", array)
    distance = np.sqrt(np.square(array[1, 0] - array[0, 0]) + np.square(array[1, 1] - array[0, 1]))
    print("distance: ", distance)

    # quest 11.
    print_task(11)
    array = np.arange(-2, 4)
    print("new array: \n", array)
    equation = 1/(1 + np.exp(array.sum(0) * (-1)))
    print("equation: ", equation)

    # quest 12
    print_task(12)
    array8 = np.array([[0, 21, 17],
                      [21, 0, 42],
                      [17, 42, 0]])
    print("new array: \n", array8)
    array8 = array8.argsort() + 1
    print("coords dist: \n", array8)
