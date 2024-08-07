import timeit
import random

def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr, ascending=True):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((ascending and arr[j] > key) or (not ascending and arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr, ascending=True):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if (ascending and arr[j] < arr[min_idx]) or (not ascending and arr[j] > arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr, ascending=True):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, ascending)
        merge_sort(R, ascending)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if (ascending and L[i] < R[j]) or (not ascending and L[i] > R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (ascending and x < pivot) or (not ascending and x > pivot)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if (ascending and x > pivot) or (not ascending and x < pivot)]
    return quick_sort(left, ascending) + middle + quick_sort(right, ascending)

def get_sorting_time(sort_function, arr, ascending=True):
    start_time = timeit.default_timer()
    sorted_arr = sort_function(arr.copy(), ascending)
    end_time = timeit.default_timer()
    return sorted_arr, end_time - start_time

def main():
    test_arrays = [
        [random.uniform(-100, 100) for _ in range(10)],
        [random.uniform(-1000, 1000) for _ in range(50)],
        [random.uniform(-10000, 10000) for _ in range(100)]
    ]

    print("Выберите один из тестовых массивов или введите свой собственный:")
    for i, arr in enumerate(test_arrays, start=1):
        print(f"{i}. {arr}")
    print("4. Ввести собственный массив")

    choice = int(input("Ваш выбор (1/2/3/4): "))

    if choice == 4:
        user_input = input("Введите числа, разделенные пробелами: ")
        arr = list(map(float, user_input.split()))
    else:
        arr = test_arrays[choice - 1]

    order_choice = input("Выберите порядок сортировки (в/у): ").strip().lower()
    ascending = True if order_choice == 'в' else False

    sort_functions = {
        "Пузырьковая сортировка": bubble_sort,
        "Сортировка вставками": insertion_sort,
        "Сортировка выбором": selection_sort,
        "Сортировка слиянием": merge_sort,
        "Быстрая сортировка": quick_sort
    }

    for name, func in sort_functions.items():
        sorted_arr, time_taken = get_sorting_time(func, arr, ascending)
        print(f"\n{name}:")
        print(f"Отсортированный массив: {sorted_arr}")
        print(f"Время сортировки: {time_taken:.6f} секунд")

if __name__ == "__main__":
    main()
