import numpy as np
import sympy as sp
import typing as tp
import random

from sympy import *
from numpy import *

class Task2:
    def __init__(self):
        pass

    def generate(self):
        flag = 1
        while (flag):
            items = [random.randint(-15, 15) for i in range (8)]

            A_1 = Matrix([[items[0], items[1]], [items[2], items[3]]])
            A_2 = Matrix([[items[4], items[5]], [items[6], items[7]]])

            Atemp = A_1 + A_2;

            if (Atemp.det() != 0):
                flag = false

            flagItems = true
            for i in range (8):
                if (items[i] == 0):
                    flagItems = false

            if (flagItems == false):
                flag = true

        flag = 1
        xy = []
        while (flag):
            xy = [np.random.randint(-15, 15) for i in range (4)]

            if ((xy[0] == 0) or (xy[1] == 0) or (xy[2] == 0) or (xy[3] == 0)):
              flag = 1
            else:
              flag = 0


        z_1 = sp.S(xy[0]) + sp.S(xy[1]) * sp.I
        z_2 = sp.S(xy[2]) + sp.S(xy[3]) * sp.I
        z = Matrix([[z_1], [z_2]])


        answer_text = f"${z}$\n"

        A = []

        A = A_1 + A_2 * sp.I;
        b = A * z
        b = simplify(b)



        x, y = sp.symbols('x y')

        task_text = f'Решить систему уравнений: ' \
                            f'$$\\begin{{cases}}' \
                            f'{latex(dot(A[0:2], [x, y]))} = {latex(b[0])} \\\\' \
                            f'{latex(dot(A[2:4], [x, y]))} = {latex(b[1])} \\\\' \
                            f'\\end{{cases}}$$'


        return task_text, answer_text

