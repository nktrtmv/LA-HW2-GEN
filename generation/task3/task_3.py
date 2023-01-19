import numpy as np
import sympy as sp
#import matplotlib
import typing as tp
import random

from sympy import *
from numpy import *


class Task3:
    def __init__(self):
        pass
    '''
    def task(self) -> tuple[str, list[str]]:
        root1 = sp.S(np.random.randint(-3, 6))
        root2 = sp.S(np.random.randint(-3, 6))
        A = sp.S(np.random.randint(1, 4))
        b = sp.S(np.random.randint(-6, 6))
        c = sp.S(int((b ** 2) / 4 + sp.S(np.random.randint(1, 4))))
        x = sp.Symbol('x')
        equation = sp.latex(sp.expand(sp.S(A) * sp.S(x - root1) * sp.S(x - root2) * sp.S(x ** 2 + b * x + c)))
        complex_root1 = sp.S(-b / 2 + sp.S(sp.sqrt(b ** 2 - 4 * c) / 2))
        complex_root2 = sp.S(-b / 2 - sp.S(sp.sqrt(b ** 2 - 4 * c) / 2))
        real_answer = sp.latex(A * (x - root1) * (x - root2) * (x ** 2 + b * x + c))
        complex_answer = sp.latex(A * (x - root1) * (x - root2) * (x - complex_root1) * (x - complex_root2))

        return equation, [real_answer, complex_answer]
    '''
    
    def generate(self):
        R = 0
        while R == 0:
            flag = 1
            while (flag):
                xy1 = [np.random.randint(-5, 5) for i in range (2)]
                xy3 = [np.random.randint(-5, 5) for i in range (2)]
                if ((xy1[0] == 0) or (xy1[1] == 0) or (xy3[0] == 0) or (xy3[1] == 0)):
                  flag = 1
                else:
                  flag = 0

                if ((xy1[0] == xy3[0]) or (xy1[1] == xy3[1])):
                    flag = 1

                if ((xy1[0] == -xy3[0]) or (xy1[1] == -xy3[1])):
                    flag = 1

            z1 = sp.S(xy1[0]) + sp.S(xy1[1]) * sp.I
            z1c = z1.conjugate()
            z3 = sp.S(xy3[0]) + sp.S(xy3[1]) * sp.I
            z3c = z3.conjugate()

            flag = 1
            while (flag):
                z5 = np.random.randint(-5, 5)
                z6 = np.random.randint(-5, 5)
                a = np.random.randint(-5, 5)
                if ((z5 == 0) or (z6 == 0) or a == 0):
                  flag = 1
                else:
                  flag = 0


            x = sp.Symbol('x')
            Cwa = sp.latex((x - z1) * (x - z1c) * (x - z3) * (x - z3c) * (x - z5) * (x - z6))
            Rwa = simplify(x ** 2 - (z1 + z1c) * x + z1 * z1c) * simplify(x ** 2 - (z3 + z3c) * x + z3 * z3c) * (x - z5) * (x - z6)

            R = a * (x**2 - (z1 + z1c)*x + z1*z1c) * (x**2 - (z3 + z3c)*x + z3*z3c) * (x - z5) * (x - z6)

            task_text = f'Найти корни многочлена ${latex(expand(R))}$ и ' \
                                f'разложить его на множители над $\\mathbb{{R}}$ и $\\mathbb{{C}}$, ' \
                                f'если известны корни $x_1$ = ${latex(z1)}$, $x_2$ = ${latex(z3c)}$, $x_3$ = ${latex(z5)}$. '

            answer_text = f'Над $\\mathbb{{C}}$: ${a}$ * ${Cwa}$,\n \\newline \n ' \
                                  f'Над $\\mathbb{{R}}$: ${a}$ * ${sp.latex(Rwa)}$\n\n\\bigskip\n\n'


        
        return task_text, answer_text





