from searches import *
import matplotlib.pyplot as plt
import numpy as np
import random
import time

Numbers_list = list(range(1000000))
random.shuffle(Numbers_list)
Data = []
target_value = random.choice(Numbers_list)
Sorted_numbers_list = sorted(Numbers_list)

for i in range(10000, 1000001, 10000):
    testing_array = Numbers_list[:i]
    sorted_testing_array = Sorted_numbers_list[:i]

    start_time = time.perf_counter_ns()
    binary_search(sorted_testing_array, target_value)
    sorted_time = time.perf_counter_ns() - start_time

    start_time = time.perf_counter_ns()
    binary_search(testing_array, target_value)
    unsorted_time = time.perf_counter_ns() - start_time

    Data.append((i, sorted_time, unsorted_time))

sizes, sorted_times, unsorted_times = zip(*Data)
coefficients_sorted = np.polyfit(np.log(sizes), sorted_times, 1)
coefficients_unsorted = np.polyfit(np.log(sizes), unsorted_times, 1)

plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.scatter(sizes, sorted_times, s=10, label='Время (отсортированный)')
plt.plot(sizes, coefficients_sorted[0] * np.log(sizes) + coefficients_sorted[1], color='red',
         label=f"Аппроксимация: {coefficients_sorted[0]:.2f}log(x) + {coefficients_sorted[1]:.2f}")
plt.xlabel("Количество элементов")
plt.ylabel("Время поиска (нс)")
plt.title("Зависимость времени поиска (отсортированный массив)")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(sizes, unsorted_times, s=10, label='Время (неотсортированный)')
plt.plot(sizes, coefficients_unsorted[0] * np.log(sizes) + coefficients_unsorted[1], color='red',
         label=f"Аппроксимация: {coefficients_unsorted[0]:.2f}log(x) + {coefficients_unsorted[1]:.2f}")
plt.xlabel("Количество элементов")
plt.ylabel("Время поиска (нс)")
plt.title("Зависимость времени поиска (неотсортированный массив)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
