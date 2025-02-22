import numpy as np

# 1. Crear un array de 10 enteros aleatorios entre 0 y 100
def rand_int():
    np.random.seed(10)
    return np.random.randint(0, 100, 10)

# 2. Crear un array de 5 números flotantes aleatorios entre 0 y 1
def rand_float():
    np.random.seed(10)
    return np.random.rand(5)

# 3. Crear un array de los primeros 10 números primos
def first_10_primes():
    primes = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    return primes

# 4. Crear un array con los cuadrados de los números del 1 al 10
def squares():
    return np.arange(1, 11) ** 2

# 5. Crear un array con los cubos de los números del 1 al 10
def cubes():
    return np.arange(1, 11) ** 3

# Operaciones con arrays
def add_arrays(arr1, arr2):
    assert arr1.shape == arr2.shape, 'Los arreglos deben tener el mismo tamaño'
    return arr1 + arr2

def subtract_arrays(arr1, arr2):
    '''Realiza una resta usando broadcasting en numpy.'''
    return arr1 - arr2


def multiply_arrays(arr1, arr2):
    return arr2 * arr1

def divide_arrays(arr1, arr2):
    assert not np.any(arr1 == 0), 'No se puede dividir por cero'
    return arr2 / arr1

# Estadísticas básicas
def stats(arr):
    assert arr.size == 5, 'El arreglo debe tener 5 elementos'
    return (np.mean(arr), np.median(arr), np.std(arr))

# Indexación y selección
def first_5(arr):
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[:5]

def last_3(arr):
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[-3:]

def indices_2_4_6(arr):
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[[2, 4, 6]]

def greater_50(arr):
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[arr > 50]

def less_7(arr):
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[arr <= 7]

# Redimensionamiento de arrays
def reshape_2x6(arr):
    assert arr.size == 12, 'El arreglo debe tener 12 elementos'
    return arr.reshape(2, 6)

def reshape_2x3x4(arr):
    assert arr.size == 24, 'El arreglo debe tener 24 elementos'
    return arr.reshape(2, 3, 4)

def reshape_10x10(arr):
    assert arr.size == 100, 'El arreglo debe tener 100 elementos'
    return arr.reshape(10, 10)

def reshape_10x10x10(arr):
    assert arr.size == 1000, 'El arreglo debe tener 1000 elementos'
    return arr.reshape(10, 10, 10)

def reshape_10x10x10x10(arr):
    assert arr.size == 10000, 'El arreglo debe tener 10000 elementos'
    return arr.reshape(10, 10, 10, 10)

# Broadcasting
def add_broadcast(arr1, arr2):
    return arr1 + arr2

def divide_broadcast(arr1, arr2):
    return arr1 / arr2

def element_wise_product(arr1, arr2):
    return arr1 * arr2

# Máscaras booleanas
def temp_data(temps):
    print("Temperaturas mayores a 25 grados:", temps[temps > 25])
    print("Número de días con temperatura menor a 15 grados:", np.sum(temps < 15))

def rainfall_data(rainfall):
    print("Ciudades con más de 100 mm de lluvia:", np.where(np.any(rainfall > 100, axis=1)))

# Umbralización de imágenes
def image_thresholding(image):
    return np.where(image >= 128, 255, 0)

# Indexación avanzada
def matrix_diagonals(matrix):
    assert matrix.shape == (5, 5), 'La matriz debe ser de 5x5'
    diagonal = matrix.diagonal()
    anti_diagonal = np.fliplr(matrix).diagonal()
    return (diagonal, anti_diagonal)

# Pruebas
import doctest
doctest.testmod()

