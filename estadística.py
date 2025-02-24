python -m unittest test_numpy.py
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.13.1/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.13.1/x64/lib
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/unittest/__main__.py", line 18, in <module>
    main(module=None)
    ~~~~^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/unittest/main.py", line 103, in __init__
    self.parseArgs(argv)
    ~~~~~~~~~~~~~~^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/unittest/main.py", line 142, in parseArgs
    self.createTests()
    ~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/unittest/main.py", line 153, in createTests
    self.test = self.testLoader.loadTestsFromNames(self.testNames,
                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
                                                   self.module)
                                                   ^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/unittest/loader.py", line 207, in loadTestsFromNames
    suites = [self.loadTestsFromName(name, module) for name in names]
              ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.1/x64/lib/python3.13/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
  File "/home/runner/work/T48A-P2/T48A-P2/test_numpy.py", line 3, in <module>
    from ejercicios_de_numpy import (rand_int, rand_float, first_10_primes, squares, cubes,
    ...<5 lines>...
                             temp_data, rainfall_data, image_thresholding, matrix_diagonals)
  File "/home/runner/work/T48A-P2/T48A-P2/ejercicios_de_numpy.py", line 98
    return np.array([1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])
IndentationError: unexpected indent
Error: Process completed with exit code 1.