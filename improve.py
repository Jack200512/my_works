import math
import numpy as np
from sympy import *
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = (b**2)-(4*a*c)
g = []
if a > 0:
    a = -a
    b = -b
    c = -c
if d > 0:
    x = symbols('x')
    x_result = solve(a*(x**2)+b*x+c, x)
    x_range = np.arange(math.ceil(x_result[0]), math.floor(x_result[1]+1))
    for value_x in x_range:
        value_x = float(value_x)
        value = a*(value_x**2)+b*value_x+c

        def function(value1):
            if int(value1) == value1:
                y_range = np.arange(1, int(value1))
            else:
                y_range = np.arange(1, int(value1)+1)
            appendix = len(y_range)
            g.append(appendix)
        function(value)
    print("the final result is "+str(sum(g)))
else:
    print("no result!")