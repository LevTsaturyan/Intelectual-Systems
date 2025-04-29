import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n)

def cyclic123_array(n): 
    """2. Генерирует numpy массив длины  3𝑛 , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2*n, 2)

def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    array = np.zeros((n, n), dtype=int)
    array[0, :] = 1
    array[-1, :] = 1
    array[:, 0] = 1
    array[:, -1] = 1
    return array

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    return (np.indices((n, n)).sum(axis=0)) % 2

def matrix_with_sum_index(n):
    """6. Создаёт n × n матрицу с (i,j)-элементами равными i + j"""
    return np.add.outer(np.arange(n), np.arange(n))

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычисляет cos(x) и sin(x) на интервале [a, b) с шагом dx
    и объединяет как две строки"""
    x = np.arange(a, b, dx)
    return np.vstack((np.cos(x), np.sin(x)))

def compute_mean_rowssum_columnssum(A):
    """8. Вычисляет среднее значение, сумму по строкам и по столбцам"""
    return np.mean(A), np.sum(A, axis=1), np.sum(A, axis=0)

def sort_array_by_column(A, j):
    """9. Сортирует массив по j-му столбцу"""
    return A[np.argsort(A[:, j])]

def compute_integral(a, b, f, dx, method):
    """10. Численно вычисляет интеграл функции f от a до b с шагом dx"""
    x = np.arange(a, b, dx)
    y = f(x)
    if method == 'rectangular':
        return np.sum(y) * dx
    elif method == 'trapezoidal':
        return (y[0] + y[-1]) * dx / 2 + np.sum(y[1:-1]) * dx
    elif method == 'simpson':
        if len(x) % 2 == 0:
            x = np.append(x, x[-1] + dx)
            y = f(x)
        return dx / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    else:
        raise ValueError("Метод должен быть 'rectangular', 'trapezoidal' или 'simpson'")
