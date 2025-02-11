#REALIZADO POR CHRISTIAN AARON ZAVALA SANCHEZ - 171817
import numpy as np

def rand_int():
  arr = np.random.randint(0, 101, 10)
  arr_int = arr.astype(np.int64)

  return arr_int

def rand_float():
  return np.random.rand(5)


def first_10_primes():
  return np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

def squares():
  return np.array(np.square(np.arange(1,11)))

def cubes():
  return np.array(np.power(np.arange(1,11), 3))

def add_arrays(arr1, arr2):
  assert arr1.shape == arr2.shape, 'Los arreglos deben tener el mismo tamaño'
  return arr1 + arr2

def subtract_arrays(arr1, arr2):
  return arr2 - arr1

def multiply_arrays(arr1, arr2):
  return arr1 * arr2

def divide_arrays(arr1, arr2):
  assert arr1.any(0), 'No se puede dividir por cero'
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
  assert arr.size == 10, 'El arreglo   (arr) debe tener 10 elementos'
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
  return arr.reshape(10,10,10,10)

def add_broadcast(arr1, arr2):
  return arr1 + arr2

def subtract_broadcast(arr1, arr2):
  if arr1.shape != arr2.shape: # Misma forma de array
    arr2 = arr2.T
  return arr1 - arr2

def multiply_broadcast(arr1, arr2):
  return np.dot(arr1, arr2) # Realiza un producto matricial, esto implicando las relgas de multiplicacion de matrices

def divide_broadcast(arr1, arr2):
  return arr1 / arr2

def element_wise_product(arr1, arr2):
  assert arr1.shape == arr2.shape # Misma forma
  assert arr1.shape == (2, 3) # Forma (2, 3), se asume que arr2 tiene la misma forma al pasar el assert pasado

  return arr1 * arr2

def temp_data(temps):
  mask_above_25 = temps >= 25 #Condicion mayor a 25 Grados celsius
  mask_below_15 = temps <= 15 #Condicion menor a 15 Grados celsius
  days = np.count_nonzero(mask_below_15)

def rainfall_data(rainfall):
  mask_above_100 = rainfall >= 100
  cities = np.any(mask_above_100, axis=1)
  index_cities = np.where(cities)[0]
  return index_cities

def image_thresholding(image):
  mask = image > 128
  binary_image = np.zeros_like(image)
  binary_image[mask] = 255
  return binary_image

def matrix_diagonals(matrix):
  assert matrix.shape == (5, 5), 'La matriz debe ser de 5x5'
  main_diagonal = matrix.diagonal()
  anti_diagonal = np.fliplr(matrix).diagonal()
  return main_diagonal, anti_diagonal
