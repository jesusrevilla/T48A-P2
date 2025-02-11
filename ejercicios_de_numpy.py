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
"""2. Create a NumPy array of 5 random floating-point numbers between 0 and 1."""
def rand_float():
  return np.random.random(5)
"""3. Create a NumPy array of the first 10 prime numbers."""
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
        n = n+1
        if is_prime(n):
            primos.append(n)
    return primos
"""4. Create a NumPy array of the squares of the numbers from 1 to 10."""
def squares():
  '''Regresa un arreglo de numpy con los cuadrados de los números del 1 al 10.
  '''
  return np.arange(1, 11) ** 2
"""5. Create a NumPy array of the cubes of the numbers from 1 to 10."""
def cubes():
  '''Regresa un arreglo de numpy con los cubos de los números del 1 al 10.
  '''
  return np.arange(1, 11) ** 3

"""### NumPy Array Operations

1. Add two NumPy arrays together.
"""

def add_arrays(arr1, arr2):
  arr1 = np.array(arr1)
  arr2 = np.array(arr2)
  arr3 = arr1 + arr2
  return arr3

"""2. Subtract two NumPy arrays from each other, second argument less first."""

def subtract_arrays(arr1, arr2):
  '''Calcula arr2 menos arr1 (arreglos de numpy).
  '''
  if arr1.shape != arr2.shape:
    return print('Los arreglos deben de tener el mismo tamaño')
  arr3 = arr2 - arr1
  return arr3

"""3. Multiply two NumPy arrays together (element-wise)."""

def multiply_arrays(arr1, arr2):
  '''Multiplica dos arreglos de numpy elemento por elemento.
  '''
  if arr1.shape != arr2.shape:
    return print('Los arreglos deben de tener el mismo tamaño')
  arr3 = arr2 * arr1
  return arr3

"""4. Divide two NumPy arrays by each other (element-wise)."""

def divide_arrays(arr1, arr2):
  '''Divide arr2 antre arr1 (arreglos de numpy).

  Precondition
  ------------
    - arr2.any(0)
  '''
  if arr1.shape != arr2.shape:
    return print('Los arreglos deben de tener el mismo tamaño')
  if np.any(arr1 == 0):
    return print('No se puede dividir por cero')
  arr3 = arr2 / arr1
  return arr3

"""5. Create a NumPy array of the integer numbers from 1 to 5. Calculate the mean, median, and standard deviation."""

def stats(arr):
  assert arr.size == 5, 'El arreglo debe tener 5 elementos'
  media = np.mean(arr)
  mediana = np.median(arr)
  desviacion_std = np.std(arr, ddof=0)  # ddof=0 es para la desviación estándar poblacional

  return media, mediana, desviacion_std

def first_5(arr):
    
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'

    return arr[:5]  # Devuelve los primeros 5 elementos

"""2. Create a NumPy array of 10 random integers between 0 and 100. Select the last 3 elements of the array."""

def last_3(arr):
    '''Regresa los últimos 3 elementos de un arr (arreglo) de numpy que contiene 10
    números enteros aleatorios entre 1 y 100.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 10 elementos con números aleatorios del 1 al 100.

    Returns
    -------
    numpy.ndarray
        Un arreglo con los últimos 3 elementos de arr.

    Precondition
    ------------
        - arr.size == 10
    '''
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'

    return arr[-3:]  # Devuelve los últimos 3 elementos

"""3. Create a NumPy array of 10 random integers between 0 and 100. Select the elements at indices 2, 4, and 6."""

def indices_2_4_6(arr):
    '''Regresa los elementos en los índices 2, 4 y 6 de un arr (arreglo) que contiene
    10 números enteros aleatorios entre 1 y 100.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 10 elementos con números aleatorios del 1 al 100.

    Returns
    -------
    numpy.ndarray
        Un arreglo con los elementos en los índices 2, 4 y 6.

    Precondition
    ------------
        - arr.size == 10
    '''
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'

    return arr[[2, 4, 6]]  # Selecciona los índices 2, 4 y 6

"""4. Create a NumPy array of 10 random integers between 0 and 100. Select the elements with values greater than 50."""

def greater_50(arr):
    '''Regresa los elementos del arr (arreglo) que contiene 10 números enteros
    aleatorios entre 1 y 100 que son mayores a 50.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 10 elementos con números aleatorios del 1 al 100.

    Returns
    -------
    numpy.ndarray
        Un arreglo con los elementos mayores a 50.

    Precondition
    ------------
        - arr.size == 10
    '''
    assert arr.size == 10, 'El arreglo debe tener 10 elementos'

    return arr[arr > 50]  # Filtra los elementos mayores a 50

"""5. Create a NumPy array of 10 random integers between 0 and 10. Select elements less than or equal to 7."""

def less_7(arr):
    '''Regresa los elementos del arr (arreglo) que contiene 10 números enteros
    aleatorios entre 1 y 100 que son menores o iguales a 7.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 10 elementos con números aleatorios del 1 al 100.

    Returns
    -------
    numpy.ndarray
        Un arreglo con los elementos menores o iguales a 7.

    Precondition
    ------------
        - arr.size == 10
    '''
    assert arr.size == 10, 'El arreglo (arr) debe tener 10 elementos'

    return arr[arr <= 7]  # Filtra los elementos menores o iguales a 7

"""### NumPy Array Reshaping

1. Create a NumPy array of 12 numbers. Reshape the array into a 2x6 matrix.
"""

def reshape_2x6(arr):
    '''Regresa un arreglo de numpy con 12 números y lo convierte en un arreglo de 2x6.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 12 elementos.

    Returns
    -------
    numpy.ndarray
        Un arreglo de forma (2, 6).

    Precondition
    ------------
        - arr.size == 12
    '''
    assert arr.size == 12, 'El arreglo (arr) debe tener 12 elementos'

    return arr.reshape(2, 6)  # Cambia la forma del arreglo a 2x6

"""2. Create a NumPy array of 24 numbers. Reshape the array into a 2x3x4 tensor."""

def reshape_2x3x4(arr):
    '''Convierte un arreglo de numpy con 24 números en un arreglo de 2x3x4.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 24 elementos.

    Returns
    -------
    numpy.ndarray
        Un arreglo con forma (2, 3, 4).

    Precondition
    ------------
        - arr.size == 24
    '''
    assert arr.size == 24, 'El arreglo (arr) debe tener 24 elementos'

    return arr.reshape(2, 3, 4)  # Cambia la forma del arreglo a 2x3x4

"""3. Create a NumPy array of 100 numbers. Reshape the array into a 10x10 matrix."""

def reshape_10x10(arr):
    '''Convierte un numpy array en un numpy array de 10x10.

    Parameters
    ----------
    arr: numpy.ndarray
        Arreglo de numpy de 100 elementos.

    Returns
    -------
    numpy.ndarray
        Un arreglo con forma (10, 10).

    Precondition
    ------------
        - arr.size == 100
    '''
    assert arr.size == 100, 'El arreglo (arr) debe tener 100 elementos'

    return arr.reshape(10, 10)  # Cambia la forma del arreglo a 10x10

"""4. Create a NumPy array of 1000 numbers. Reshape the array into a 10x10x10 tensor."""

def reshape_10x10x10(arr):
  '''(np.ndarray) -> np.ndarray
  Regresa un arreglo de 10x10x10.

  Parameters
  ----------
  arr: numpy.ndarray
   arreglo de numpy de 1000 elementos.

  Precondition
  ------------
    - arr.size == 1000
  '''
  assert arr.size == 1000, 'El arreglo (arr) debe tener 1000 elementos'
  return arr.reshape(10, 10, 10)  # Cambia la forma del arreglo a 10x10

"""5. Create a NumPy array of 10000 numbers. Reshape the array into a 10x10x10x10 tensor."""

def reshape_10x10x10x10(arr):
  '''(np.ndarray) -> np.ndarray
  Regresa un arreglo de numpy de 10x10x10x10.

  Parameters
  ----------
  arr: numpy.ndarray
    arreglo de numpy de 10000 elementos.

  Precondition
  ------------
    - arr.size == 10000
  '''
  assert arr.size == 10000, 'El arreglo (arr) debe tener 10000 elementos'
  return arr.reshape(10, 10, 10, 10)  # Cambia la forma del arreglo a 10x10

"""### NumPy Array Broadcasting

1. Add a NumPy array of shape (2, 3) to a NumPy array of shape (2, 1).
"""

def add_broadcast(arr1, arr2):
  '''Suma de dos arreglos de numpy con formas (2, 3) y (2, 1).

  Parameters
  ----------
  arr1: numpy.ndarray
    arreglo de numpy de forma (2, 3).
  arr2: numpy.nd.array
    arreglo de numpy de forma (2, 1).
  '''
  assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
  assert arr2.shape == (2, 1), 'arr2 debe tener la forma (2, 1)'

  return arr1 + arr2  # Broadcasting ocurre automáticamente

"""2. Subtract a NumPy array of shape (3, 2) from a NumPy array of shape (2, 3)."""

def subtract_broadcast(arr1, arr2):
  '''(np.ndarray, np.ndarray) -> np.ndarray
  Regresa la resta de dos arreglos de numpy con formas (3, 2) y (2, 3).

  Parameters
  ----------
  arr1: numpy.ndarray
    arreglo de numpy de forma (3, 2).
  arr2: numpy.ndarray
    arreglo de numpy de forma (2, 3).
  '''
  assert arr1.shape == (3, 2), 'arr1 debe tener la forma (3, 2)'
  assert arr2.shape == (2, 3), 'arr2 debe tener la forma (2, 3)'
  arr2 = arr2.T  # Now arr2 will have shape (3, 2)
  return arr1 - arr2

"""3. Multiply a NumPy array of shape (2, 3) by a NumPy array of shape (3, 2)."""

def multiply_broadcast(arr1, arr2):
  '''Multiplica dos arreglos de numpy con formas (2, 3) y (3, 2).

  Parameters
  ---------
  arr1: numpy.ndarray
    arreglo de numpy de forma (2, 3).
  arr2: numpy.ndarray
    arreglo de numpy de forma (3, 2).
  '''
  assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
  assert arr2.shape == (3, 2), 'arr2 debe tener la forma (3, 2)'

  arr2 = arr2.T  # Now arr2 will have shape (3, 2)
  return arr1 * arr2

"""4. Divide a NumPy array of shape (2, 3) by a NumPy array of shape (2, 1)."""

def divide_broadcast(arr1, arr2):
  '''Divide dos arreglos de numpy con formas (2, 3) y (2, 1).

  Parameters
  ----------
  arr1: numpy.ndarray
    arreglo de numpy de forma (2, 3).
  arr2: numpy.ndarray
    arreglo de numpy de forma (2, 1).
  '''
  assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
  assert arr2.shape == (2, 1), 'arr2 debe tener la forma (2, 1)'

  arr2 = arr2.T  # Now arr2 will have shape (3, 2)
  return arr1 / arr2

"""5. Calculate the element-wise product of two NumPy arrays of shape (2, 3)."""

def element_wise_product(arr1, arr2):
  '''Multiplica elemento a elemento dos arreglos de numpy con formas (2, 3).

  Parameters
  ----------
  arr1: numpy.ndarray
    arreglo de numpy de forma (2, 3).
  arr2: numpy.ndarray
    arreglo de numpy de forma (2, 3).
  '''
  assert arr1.shape == (2, 3), 'arr1 debe tener la forma (2, 3)'
  assert arr2.shape == (2, 3), 'arr2 debe tener la forma (2, 3)'

  arr2 = arr2.T  # Now arr2 will have shape (3, 2)
  return arr1 * arr2

"""### Boolean Arrays and Masks

1. Temperature Data: You have a 1D NumPy array representing daily temperatures in Celsius.  Create a boolean mask that identifies days where the temperature was above 25 degrees Celsius.  Use this mask to print the temperatures on those days.  Also, calculate and print the number of days the temperature was below 15 degrees Celsius.
"""

def temp_data(temps):
    '''Imprime las temperaturas que fueron mayores a 25 grados y el número de
    días en los que la temperatura fue menor a 15 grados.

    Parameters
    ----------
    temps: numpy.ndarray
        arreglo de numpy de temperaturas en Celsius.
    '''
    # Aseguramos que el arreglo tenga 30 elementos
    assert temps.size == 30, 'El arreglo (temps) debe tener 30 elementos'

    # Filtrar las temperaturas mayores a 25 grados
    mayores_a_25 = temps[temps > 25]

    # Contar los días con temperaturas menores a 15 grados
    menores_a_15 = np.sum(temps < 15)

    # Imprimir los resultados
    print("Temperaturas mayores a 25 grados:", mayores_a_25)
    print("Número de días con temperaturas menores a 15 grados:", menores_a_15)

"""2. Rainfall Data: You have a 2D NumPy array representing monthly rainfall (in mm) for different cities.  Create a boolean mask to find the locations where rainfall exceeded 100 mm in any month.  Print the city indices (row numbers) that meet this condition."""

import numpy as np

def rainfall_data(rainfall):
    '''Imprime los índices de las ciudades que tuvieron más de 100 mm de lluvia.

    Parameters
    ----------
    rainfall: numpy.ndarray
        arreglo 2D de numpy de lluvia en mm y ciudades.
    '''
    # Aseguramos que el arreglo tenga la forma (3, 12)
    assert rainfall.shape == (3, 12), 'El arreglo (rainfall) debe tener la forma (3, 12)'

    # Iterar sobre cada ciudad (filas)
    for i in range(rainfall.shape[0]):  # Hay 3 ciudades (filas)
        # Verificamos si alguna lluvia en esa ciudad supera los 100 mm
        if np.any(rainfall[i] > 100):
            print(f"Ciudad {i} tuvo más de 100 mm de lluvia en algún mes.")

"""3. Image Thresholding:  Imagine a grayscale image represented as a 2D NumPy array.  Create a mask to select pixels with intensity values greater than a certain threshold (e.g., 128).  Set the values of these pixels to 255 (white) and the remaining pixels to 0 (black). This simulates a simple image thresholding operation."""

def image_thresholding(image):
    '''Genera un arreglo de numpy en blanco y negro.

    Parameters
    ----------
    image: numpy.ndarray
        arreglo 2D de numpy de una imagen en escala de grises.
    '''
    # Aseguramos que el arreglo tenga la forma (100, 100)
    assert image.shape == (100, 100), 'El arreglo (image) debe tener la forma (100, 100)'

    # Establecer el umbral (en este caso 128 para una imagen en escala de grises)
    threshold_value = 128

    # Generar la imagen en blanco y negro (binaria)
    binary_image = (image >= threshold_value).astype(np.uint8) * 255

    return binary_image

"""### Fancy Indexing

1. Matrix Diagonals: Create a 5x5 matrix with values from 1 to 25.  Use fancy indexing to extract the elements on the main diagonal and the elements on the anti-diagonal.
"""

def matrix_diagonals(matrix):
  '''Regresa un tuple con los elementos de la diagonal principal y antidiagonal.

  Parameters
  ----------
  matrix: numpy.ndarray
    arreglo 2D de numpy de 5x5.

  Precondition
  ------------
    - matrix.shape == (5, 5)
  '''
  assert matrix.shape == (5, 5), 'La matriz debe ser de 5x5'
  diagonal_principal = matrix.diagonal()
  diagonal_antidiagonal = np.fliplr(matrix).diagonal()

  return diagonal_principal, diagonal_antidiagonal
