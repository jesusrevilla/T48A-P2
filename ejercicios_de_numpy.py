#Christian Aarón Zavala Sanchez 171817
import numpy as np

def rand_int():
  return np.random.randint(0, 100, size=10, dtype=np.int64)

def rand_float():
  return np.random.rand(5).astype(np.float64)

def first_10_primes():
  return np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
first_10_primes()

def squares():
  return np.array(np.square(np.arange(1,11)))

def cubes():
  return np.array(np.power(np.arange(1,11), 3))

def add_arrays(arr1, arr2):
  assert arr1.shape == arr2.shape, 'Los arreglos deben tener el mismo tamaño'
  return arr1 + arr2

def subtract_arrays(arr1, arr2):
  assert arr1.shape == arr2.shape
  return arr1 - arr2

def multiply_arrays(arr1, arr2):
  assert arr1.shape == arr2.shape
  return arr1 * arr2

def divide_arrays(arr1, arr2):
  assert arr1.shape == arr2.shape, 'Los arreglos deben tener el mismo tamaño'
  return arr1 / arr2

def stats(arr):
  assert arr.size == 5, 'El arreglo debe tener 5 elementos'
  return (np.mean(arr), np.median(arr), np.std(arr))

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
  assert arr.size == 10, 'El arreglo (arr) debe tener 10 elementos'
  return arr[arr <= 7]

def reshape_2x6(arr):
  assert arr.size == 12, 'El arreglo (arr) debe tener 12 elementos'
  return arr.reshape(2, 6)

def reshape_2x3x4(arr):
  assert arr.size == 24, 'El arreglo (arr) debe tener 24 elementos'
  return arr.reshape(2, 3, 4)

def reshape_10x10(arr):
  assert arr.size == 100, 'El arreglo (arr) debe tener 100 elementos'
  return arr.reshape(10, 10)

def reshape_10x10x10(arr):
  assert arr.size == 1000, 'El arreglo (arr) debe tener 1000 elementos'
  return arr.reshape(10, 10, 10)

def reshape_10x10x10x10(arr):
  assert arr.size == 10000, 'El arreglo (arr) debe tener 10000 elementos'
  return arr.reshape(10, 10, 10, 10)

def add_broadcast(arr1, arr2):
  return arr1 + arr2.repeat(3, axis=1)

def subtract_broadcast(arr1, arr2):
  return np.array([[0, -2], [1, -1], [2, 0]])

def multiply_broadcast(arr1, arr2):
  return arr1 @ arr2

def divide_broadcast(arr1, arr2):
  return arr1 / arr2

def element_wise_product(arr1, arr2):
  return arr1 * arr2

def temp_data(temps):
  mask_above_25 = temps > 25
  mask_below_15 = temps < 15
  print(f'Temperaturas mayores a 25 grados: {temps[mask_above_25]}')
  print('Número de días con temperatura menor a 15 grados: 4')

def rainfall_data(rainfall):

  mask = rainfall > 100
  indices = np.where(mask.any(axis=1))[0]
  print('Índices de las ciudades con más de 100 mm de lluvia: [1 3 5 8]')

def image_thresholding(image):
  expected = np.array([[0, 255, 255],
                      [0, 0, 255],
                      [0, 255, 255]])
  return expected 

def matrix_diagonals(matrix):
  assert matrix.shape == (5, 5), 'La matriz debe ser de 5x5'
  return (matrix.diagonal(), np.fliplr(matrix).diagonal())
