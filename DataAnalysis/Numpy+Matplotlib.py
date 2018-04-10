Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> import matplotli.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import matplotli.pyplot as plt
ModuleNotFoundError: No module named 'matplotli'
>>> import matplotlib.pyplot as plt
>>> arr_1 = np.array([12,34,56,11,15,76,5])
>>> arr_1
array([12, 34, 56, 11, 15, 76,  5])
>>> arr_1 = np.array([12,34,56,11,15,76,5,'hi'])
>>> arr_1
array(['12', '34', '56', '11', '15', '76', '5', 'hi'], dtype='<U11')
>>> arr_1 = np.array([12,34,56,11,15,76,5])
>>> arr_1[0]
12
>>> arr_1[0:4]
array([12, 34, 56, 11])
>>> arr_2 = np.arange(2,10)
>>> arr_2
array([2, 3, 4, 5, 6, 7, 8, 9])
>>> arr_3 = np.zeros(5)
>>> arr_3
array([0., 0., 0., 0., 0.])
>>> arr_3 = np.zeros([5,5])
>>> arr_3
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> arr_3 = np.ones([5,5])
>>> arr_3
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>> arr_4 = np.linspace(0,5)
>>> arr_4
array([0.        , 0.10204082, 0.20408163, 0.30612245, 0.40816327,
       0.51020408, 0.6122449 , 0.71428571, 0.81632653, 0.91836735,
       1.02040816, 1.12244898, 1.2244898 , 1.32653061, 1.42857143,
       1.53061224, 1.63265306, 1.73469388, 1.83673469, 1.93877551,
       2.04081633, 2.14285714, 2.24489796, 2.34693878, 2.44897959,
       2.55102041, 2.65306122, 2.75510204, 2.85714286, 2.95918367,
       3.06122449, 3.16326531, 3.26530612, 3.36734694, 3.46938776,
       3.57142857, 3.67346939, 3.7755102 , 3.87755102, 3.97959184,
       4.08163265, 4.18367347, 4.28571429, 4.3877551 , 4.48979592,
       4.59183673, 4.69387755, 4.79591837, 4.89795918, 5.        ])
>>> arr_4 = np.linspace(0,5,5)
>>> arr_4
array([0.  , 1.25, 2.5 , 3.75, 5.  ])
>>> arr_4 = np.linspace(0,5,10)
>>> arr_4
array([0.        , 0.55555556, 1.11111111, 1.66666667, 2.22222222,
       2.77777778, 3.33333333, 3.88888889, 4.44444444, 5.        ])
>>> np.random.random()
0.5905194260064072
>>> np.random.random()
0.3211213606140856
>>> np.random.random()
0.14381268432211447
>>> np.random.random()
0.23057839637153366
>>> np.random.random() * 10
4.419003130089278
>>> np.random.random() * 10
6.516711179556936
>>> np.random.random() * 10
3.916134567796324
>>> np.random.randint(0,10)
5
>>> np.random.randint(0,10)
4
>>> np.random.randint(0,10)
7
>>> np.random.randint(0,10,5)
array([7, 4, 0, 1, 7])
>>> np.random.randint(0,10,10)
array([8, 3, 2, 0, 4, 5, 9, 4, 7, 2])
>>> arr_nd = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> arr_nd
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> list_nd = [[1,2,3],[4,5,6],[7,8,9]]
>>> list_nd
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> arr_nd[0]
array([1, 2, 3])
>>> arr_nd[0][1]
2
>>> arr_nd[0:2]
array([[1, 2, 3],
       [4, 5, 6]])
>>> arr_nd[0:2,0:2]
array([[1, 2],
       [4, 5]])
>>> arr_nd[:,0:2]
array([[1, 2],
       [4, 5],
       [7, 8]])
>>> np.ndarray(2)
array([7.74860419e-304, 7.74860419e-304])
>>> np.ndarray(4)
array([1.25, 2.5 , 3.75, 5.  ])
>>> np.ndarray(2,2)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    np.ndarray(2,2)
TypeError: data type not understood
>>> np.ndarray([2,2])
array([[1.25, 2.5 ],
       [3.75, 5.  ]])
>>> np.ndarray([5,5])
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>> np.ndarray([5,5,2])
array([[[0.        , 0.10204082],
        [0.20408163, 0.30612245],
        [0.40816327, 0.51020408],
        [0.6122449 , 0.71428571],
        [0.81632653, 0.91836735]],

       [[1.02040816, 1.12244898],
        [1.2244898 , 1.32653061],
        [1.42857143, 1.53061224],
        [1.63265306, 1.73469388],
        [1.83673469, 1.93877551]],

       [[2.04081633, 2.14285714],
        [2.24489796, 2.34693878],
        [2.44897959, 2.55102041],
        [2.65306122, 2.75510204],
        [2.85714286, 2.95918367]],

       [[3.06122449, 3.16326531],
        [3.26530612, 3.36734694],
        [3.46938776, 3.57142857],
        [3.67346939, 3.7755102 ],
        [3.87755102, 3.97959184]],

       [[4.08163265, 4.18367347],
        [4.28571429, 4.3877551 ],
        [4.48979592, 4.59183673],
        [4.69387755, 4.79591837],
        [4.89795918, 5.        ]]])
>>> np.ndarray([2,2,2])
array([[[0.00000000e+000, 0.00000000e+000],
        [0.00000000e+000, 0.00000000e+000]],

       [[0.00000000e+000, 6.97620692e-321],
        [1.11261027e-306, 1.05250991e-311]]])
>>> x = np.ndarray([2,2,2])
>>> x.shape
(2, 2, 2)
>>> x.ndim
3
>>> x = np.array([i for i in range(1,200)])
>>> y = np.random.randint(500,1000,200)
>>> len(x)
199
>>> len(y)
200
>>> x = np.array([i for i in range(1,201)])
>>> len(x)
200
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F086EBFC88>]
p
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F088667668>]
>>> plt.show()
>>> plt.plot(x,y,'o')
[<matplotlib.lines.Line2D object at 0x000001F08884A6D8>]
>>> plt.show()
>>> plt.plot(x,y,'ro')
[<matplotlib.lines.Line2D object at 0x000001F0885BF6D8>]
>>> plt.show()
>>> plt.plot(x,y,'ro', color='cyan')
[<matplotlib.lines.Line2D object at 0x000001F0889C2128>]
>>> plt.show()
>>> x
array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,
        14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,
        27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,
        40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,
        53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,  65,
        66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,
        79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,
        92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103, 104,
       105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
       118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
       131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
       144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156,
       157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169,
       170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
       183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195,
       196, 197, 198, 199, 200])
>>> y = x**2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F0888A5BA8>]
>>> plt.show()
>>> plt.plot(x,y,'ro')
[<matplotlib.lines.Line2D object at 0x000001F08894E588>]
>>> plt.show()
>>> plt.plot(x,y,'ro',s=50)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    plt.plot(x,y,'ro',s=50)
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3317, in plot
    ret = ax.plot(*args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1898, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1406, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 407, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 395, in _plot_args
    seg = func(x[:, j % ncx], y[:, j % ncy], kw, kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 302, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Python36\lib\site-packages\matplotlib\lines.py", line 431, in __init__
    self.update(kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 885, in update
    for k, v in props.items()]
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 885, in <listcomp>
    for k, v in props.items()]
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 878, in _update_property
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property s
>>> plt.plot(x,y,'ro',size=50)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    plt.plot(x,y,'ro',size=50)
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3317, in plot
    ret = ax.plot(*args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1898, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1406, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 407, in _grab_next_args
    for seg in self._plot_args(remaining, kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 395, in _plot_args
    seg = func(x[:, j % ncx], y[:, j % ncy], kw, kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 302, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Python36\lib\site-packages\matplotlib\lines.py", line 431, in __init__
    self.update(kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 885, in update
    for k, v in props.items()]
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 885, in <listcomp>
    for k, v in props.items()]
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 878, in _update_property
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property size
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x000001F088CCFD30>
>>> plt.show()
>>> plt.scatter(x,y,s=50)
<matplotlib.collections.PathCollection object at 0x000001F0896C5EF0>
>>> plt.show()
>>> plt.scatter(x,y,s=5)
<matplotlib.collections.PathCollection object at 0x000001F0898E4550>
>>> plt.show()
>>> 
