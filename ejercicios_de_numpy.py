import numpy as np

def rand_int():
    '''Crea un arreglo de numpy con 10 enteros aleatorios entre 0 y 100.
    Para poder mantener la generación de números aleatorios
    fija, en los ejemplos, se utiliza un seed.
    Returns
    -------
    numpy.ndarray
        Arreglo de numpy con 10 enteros aleatorios entre 0 y 100.
    Examples
    --------
    >>> np.random.seed(10)
    >>> rand_int()
    array([ 9, 15, 64, 28, 89, 93, 29,  8, 73,  0])
    '''
    return np.random.randint(0, 100, 10)

def rand_float():
    '''Crea un arreglo de numpy con 5 números flotantes aleatorios entre 0 y 1.'''
    return np.random.random(5)

def first_10_primes():
    '''Crea un arreglo de numpy con los primeros 10 números primos.'''
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
    '''Regresa un arreglo de numpy con los cuadrados de los números del 1 al 10.'''
    return np.arange(1, 11) ** 2

def cubes():
    '''Regresa un arreglo de numpy con los cubos de los números del 1 al 10.'''
    return np.arange(1, 11) ** 3

def add_arrays(arr1, arr2):
    '''Suma dos arreglos de numpy.'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return arr1 + arr2

def subtract_arrays(arr1, arr2):
    '''Calcula arr2 menos arr1 (arreglos de numpy).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if arr1.shape != arr2.shape:
        raise ValueError('Los arreglos deben de tener el mismo tamaño')
    return arr2 - arr1

def multiply_arrays(arr1, arr2):
    '''Multiplica dos arreglos de numpy elemento por elemento.'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if arr1.shape != arr2.shape:
        raise ValueError('Los arreglos deben de tener el mismo tamaño')
    return arr2 * arr1

def divide_arrays(arr1, arr2):
    '''Divide arr2 entre arr1 (arreglos de numpy).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    if arr1.shape != arr2.shape:
        raise ValueError('Los arreglos deben de tener el mismo tamaño')
    if np.any(arr1 == 0):
        raise ValueError('No se puede dividir por cero')
    return arr2 / arr1

def stats(arr):
    '''Calcula la media, mediana y desviación estándar de un arreglo de numpy.'''
    arr = np.array(arr)
    assert arr.size == 5, 'El arreglo debe tener 5 elementos'
    media = np.mean(arr)
    mediana = np.median(arr)
    desviacion_std = np.std(arr, ddof=0)  # ddof=0 es para la desviación estándar poblacional
    return media, mediana, desviacion_std

def first_5(arr):
    '''Devuelve los primeros 5 elementos de un arreglo de numpy.'''
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[:5]

def last_3(arr):
    '''Devuelve los últimos 3 elementos de un arreglo de numpy.'''
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[-3:]

def indices_2_4_6(arr):
    '''Devuelve los elementos en los índices 2, 4 y 6 de un arreglo de numpy.'''
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[[2, 4, 6]]

def greater_50(arr):
    '''Devuelve los elementos mayores a 50 de un arreglo de numpy.'''
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[arr > 50]

def less_7(arr):
    '''Devuelve los elementos menores o iguales a 7 de un arreglo de numpy.'''
    arr = np.array(arr)
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'
    return arr[arr <= 7]

def reshape_2x6(arr):
    '''Convierte un arreglo de numpy de 12 elementos en un arreglo de 2x6.'''
    arr = np.array(arr)
    assert arr.size == 12, 'El arreglo debe tener 12 elementos'
    return arr.reshape(2, 6)

def reshape_2x3x4(arr):
    '''Convierte un arreglo de numpy de 24 elementos en un arreglo de 2x3x4.'''
    arr = np.array(arr)
    assert arr.size == 24, 'El arreglo debe tener 24 elementos'
    return arr.reshape(2, 3, 4)

def reshape_10x10(arr):
    '''Convierte un arreglo de numpy de 100 elementos en un arreglo de 10x10.'''
    arr = np.array(arr)
    assert arr.size == 100, 'El arreglo debe tener 100 elementos'
    return arr.reshape(10, 10)

def reshape_10x10x10(arr):
    '''Convierte un arreglo de numpy de 1000 elementos en un arreglo de 10x10x10.'''
    arr = np.array(arr)
    assert arr.size == 1000, 'El arreglo debe tener 1000 elementos'
    return arr.reshape(10, 10, 10)

def reshape_10x10x10x10(arr):
    '''Convierte un arreglo de numpy de 10000 elementos en un arreglo de 10x10x10x10.'''
    arr = np.array(arr)
    assert arr.size == 10000, 'El arreglo debe tener 10000 elementos'
    return arr.reshape(10, 10, 10, 10)

def add_broadcast(arr1, arr2):
    '''Suma dos arreglos de numpy con formas (2, 3) y (2, 1).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (2, 1), 'arr2 debe tener la forma (2, 1)'
    return arr1 + arr2

def subtract_broadcast(arr1, arr2):
    '''Resta dos arreglos de numpy con formas (3, 2) y (2, 3).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (3, 2), 'arr1 debe tener la forma (3, 2)'
    assert arr2.shape == (2, 3), 'arr2 debe tener la forma (2, 3)'
    arr2 = arr2.T  # Now arr2 will have shape (3, 2)
    return arr1 - arr2

def multiply_broadcast(arr1, arr2):
    '''Multiplica dos arreglos de numpy con formas (2, 3) y (3, 2).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (3, 2), 'arr2 debe tener la forma (3, 2)'
    arr2 = arr2.T  # Now arr2 will have shape (3, 2)
    return arr1 * arr2

def divide_broadcast(arr1, arr2):
    '''Divide dos arreglos de numpy con formas (2, 3) y (2, 1).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (2, 1), 'arr2 debe tener la forma (2, 1)'
    return arr1 / arr2

def element_wise_product(arr1, arr2):
    '''Multiplica elemento a elemento dos arreglos de numpy con formas (2, 3).'''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
    assert arr2.shape == (2, 3), 'arr2 debe tener la forma (2, 3)'
    return arr1 * arr2
  
def temp_data(temps):
    '''Imprime las temperaturas que fueron mayores a 25 grados y el número de
    días en los que la temperatura fue menor a 15 grados.'''
    temps = np.array(temps)
    assert temps.size == 30, 'El arreglo (temps) debe tener 30 elementos'
    mayores_a_25 = temps[temps > 25]
    menores_a_15 = np.sum(temps < 15)
    print("Temperaturas mayores a 25 grados:", mayores_a_25)
    print("Número de días con temperaturas menores a 15 grados:", menores_a_15)

def rainfall_data(rainfall):
    '''Imprime los índices de las ciudades que tuvieron más de 100 mm de lluvia.'''
    rainfall = np.array(rainfall)
    assert rainfall.shape == (3, 12), 'El arreglo (rainfall) debe tener la forma (3, 12)'
    for i in range(rainfall.shape[0]):  # Hay 3 ciudades (filas)
        if np.any(rainfall[i] > 100):
            print(f"Ciudad {i} tuvo más de 100 mm de lluvia en algún mes.")

def image_thresholding(image):
    '''Genera un arreglo de numpy en blanco y negro.'''
    image = np.array(image)
    assert image.shape == (100, 100), 'El arreglo (image) debe tener la forma (100, 100)'
    threshold_value = 128
    binary_image = (image >= threshold_value).astype(np.uint8) * 255
    return binary_image

def matrix_diagonals(matrix):
    '''Regresa un tuple con los elementos de la diagonal principal y antidiagonal.'''
    matrix = np.array(matrix)
    assert matrix.shape == (5, 5), 'La matriz debe ser de 5x5'
    diagonal_principal = matrix.diagonal()
    diagonal_antidiagonal = np.fliplr(matrix).diagonal()
    return diagonal_principal, diagonal_antidiagonal
