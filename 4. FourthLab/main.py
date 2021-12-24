import numpy as np
import matplotlib.pyplot as plt

# В ТЕКСТОВЫХ ФАЙЛАХ Я ЗАМЕНИЛ ЗАПЯТУЮ НА ТОЧКУ ДЛЯ ТОГО,
# ЧТОБЫ МОЖНО БЫЛО СПОКОЙНО ИМПОРТИТЬ ИХ
# ЧЕРЕЗ ВСТРОЕННУЮ В numpy ФУНКЦИЮ.

def print_task(number: int) -> None:
    print(f'\n\n\n--------------------------\n\t\t\t{number}\n--------------------------\n')


def mode(a, axis=0):
    scores = np.unique(np.ravel(a))  # get ALL unique values
    test_shape = list(a.shape)
    test_shape[axis] = 1
    old_most_freq = np.zeros(test_shape)
    old_counts = np.zeros(test_shape)

    for score in scores:
        template = (a == score)
        counts = np.expand_dims(np.sum(template, axis), axis)
        most_frequent = np.where(counts > old_counts, score, old_most_freq)
        old_counts = np.maximum(counts, old_counts)
        old_most_freq = most_frequent

    return most_frequent, old_counts


if __name__ == '__main__':
    # global preps:
    first_value = np.loadtxt('var5-rv1.txt', dtype=float)
    second_value = np.loadtxt('var5-rv2.txt', dtype=float)

    # task #1.1.
    print_task(1.1)
    first_mean = np.mean(first_value)
    second_mean = np.mean(second_value)
    print(first_mean, ' - mean of first value.')
    print(second_mean, ' - mean of second value.')

    # task #1.2.
    print_task(1.2)
    first_disp = np.var(first_value)
    second_disp = np.var(second_value)
    print(first_disp, ' - dispersion of first value.')
    print(second_disp, ' - dispersion of second value.')

    # task #1.3.
    print_task(1.3)
    first_median = np.median(np.sort(first_value))
    second_median = np.median(np.sort(second_value))
    print(first_median, ' - first value\'s median.')
    print(second_median, ' - second value\'s median')

    # task #1.4.
    print_task(1.4)
    first_mode = mode(first_value)
    second_mode = mode(second_value)
    print(first_mode, ' - mode of first value.')
    print(second_mode, ' - mode of second value.')

    # task #1.5.
    print_task(1.5)
    first_average = np.average(first_value)
    second_average = np.average(second_value)
    first_value_third_center_moment = np.average(pow((first_value - first_average), 3))
    first_asymm_coef = first_value_third_center_moment/(first_disp * np.sqrt(first_disp))
    second_value_third_center_moment = np.average(pow((second_value - second_average), 3))
    second_asymm_coef = second_value_third_center_moment/(second_disp * np.sqrt(second_disp))
    print(first_asymm_coef, ' - first coefficient of asymmetry.')
    print(second_asymm_coef, ' - second coefficient of asymmetry.')

    # task #1.6.
    print_task(1.6)
    first_value_fourth_center_moment = np.average(pow((first_value - first_average), 4))
    second_value_fourth_center_moment = np.average(pow((second_value - second_average), 4))
    first_axes_coef = first_value_fourth_center_moment/pow(first_disp, 2) - 3
    second_axes_coef = second_value_fourth_center_moment/pow(second_disp, 2) - 3
    print(first_axes_coef, ' - first value\'s axes coefficient.')
    print(second_axes_coef, ' - second value\'s axes coefficient.')

    # task #2.
    print_task(2)
    print('first file\'s min:', np.min(first_value))
    print('first file\'s max:', np.max(first_value))
    print('second file\'s min:', np.min(second_value))
    print('second file\'s max:', np.max(second_value))

    fig, ax1 = plt.subplots()
    fig, ax2 = plt.subplots()
    ax1.hist(first_value)
    ax2.hist(second_value)
    plt.show()

    # task #3.
    print_task(3)
    print('The first value according to the received data can be considered as a normally distributed, cuz median and '
          'mean values are quiet equal and asymmetry coefficient near to 0')
    print('The second value according to the received data can\'t be considered as a normally distributed, although '
          'median and mean values are quiet equal but asymmetry coefficient much more than 0.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
