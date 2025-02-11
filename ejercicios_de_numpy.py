
import numpy as np

def rand_int():
    return np.random.randint(0, 100, 10)

def rand_float():
    return np.random.random(10)

def first_10_primes():
    n = 0
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primos = []
    while len(primos) < 10:
        n += 1
        if is_prime(n):
            primos.append(n)
    return np.array(primos)

def squares():
    return np.arange(1, 11) ** 2

def cubes():
    return np.arange(1, 11) ** 3

def add_arrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return arr1 + arr2

def subtract_arrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if arr1.shape != arr2.shape:
        raise ValueError('Los arreglos deben de tener el mismo tamaño')
    return arr1 - arr2

def multiply_arrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if arr1.shape != arr2.shape:
        raise ValueError('Los arreglos deben de tener el mismo tamaño')
    return arr2 * arr1

def divide_arrays(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if arr1.shape != arr2.shape:
        raise ValueError('Los arreglos deben de tener el mismo tamaño')
    if np.any(arr1 == 0):
        raise ValueError('No se puede dividir por cero')
    return arr1 / arr2

def stats(arr):
    arr = np.array(arr)
    assert arr.size == 5, 'El arreglo debe tener 5 elementos'
    media = np.mean(arr)
    mediana = np.median(arr)
    desviacion_std = np.std(arr, ddof=0)
    return media, mediana, desviacion_std

def first_5(arr):
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[:5]

def last_3(arr):
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[-3:]

def indices_2_4_6(arr):
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[[2, 4, 6]]

def greater_50(arr):
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[arr > 50]

def less_7(arr):
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[arr <= 7]

def reshape_2x6(arr):
    arr = np.array(arr)
    assert arr.size == 12, 'El arreglo debe tener 12 elementos'
    return arr.reshape(2, 6)

def reshape_2x3x4(arr):
    arr = np.array(arr)
    assert arr.size == 24, 'El arreglo debe tener 24 elementos'
    return arr.reshape(2, 3, 4)

def reshape_10x10(arr):
    arr = np.array(arr)
    assert arr.size == 100, 'El arreglo debe tener 100 elementos'
    return arr.reshape(10, 10)

def reshape_10x10x10(arr):
    arr = np.array(arr)
    assert arr.size == 1000, 'El arreglo debe tener 1000 elementos'
    return arr.reshape(10, 10, 10)

def reshape_10x10x10x10(arr):
    arr = np.array(arr)
    assert arr.size == 10000, 'El arreglo debe tener 10000 elementos'
    return arr.reshape(10, 10, 10, 10)

def add_broadcast(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (2, 1), 'arr2 debe tener la forma (2, 1)'
    return arr1 + arr2

def subtract_broadcast(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (3, 2), 'arr1 debe tener la forma (3, 2)'
    assert arr2.shape == (2, 3), 'arr2 debe tener la forma (2, 3)'
    arr2 = arr2.T
    return arr1 - arr2

def multiply_broadcast(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (3, 2), 'arr2 debe tener la forma (3, 2)'
    arr2 = arr2.T
    return arr1 * arr2

def divide_broadcast(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (2, 1), 'arr2 debe tener la forma (2, 1)'
    return arr1 / arr2

def element_wise_product(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (2, 3), 'arr2 debe tener la forma (2, 3)'
    return arr1 * arr2

def temp_data(temps):
    temps = np.array(temps)
    assert temps.size == 30, 'El arreglo (temps) debe tener 30 elementos'
    mayores_a_25 = temps[temps > 25]
    menores_a_15 = np.sum(temps < 15)
    print("Temperaturas mayores a 25 grados:", mayores_a_25)
    print("Número de días con temperaturas menores a 15 grados:", menores_a_15)

def rainfall_data(rainfall):
    rainfall = np.array(rainfall)
    assert rainfall.shape == (3, 12), 'El arreglo (rainfall) debe tener la forma (3, 12)'
    for i in range(rainfall.shape[0]):
        if np.any(rainfall[i] > 100):
            print(f"Ciudad {i} tuvo más de 100 mm de lluvia en algún mes.")

def image_thresholding(image):
    image = np.array(image)
    assert image.shape == (100, 100), 'El arreglo (image) debe tener la forma (100, 100)'
    threshold_value = 128
    binary_image = (image >= threshold_value).astype(np.uint8) * 255
    return binary_image

def matrix_diagonals(matrix):
    matrix = np.array(matrix)
    assert matrix.shape == (5, 5), 'La matriz debe ser de 5x5'
    diagonal_principal = matrix.diagonal()
    diagonal_antidiagonal = np.fliplr(matrix).diagonal()
    return diagonal_principal, diagonal_antidiagonal
