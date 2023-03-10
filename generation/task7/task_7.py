# -*- coding: utf-8 -*-
"""Task-7.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13vrgUbihonxXOLagxrW3QTD3cFcENCYe
"""

from sympy.printing.preview import latex
import numpy as np
import sympy as sp


class Task7:
    def __init__(self) -> None:
        pass

    def generate(self):
        o = sp.Point(0, 0, 0)
        while True:
            a = sp.Point(np.random.randint(-11, 11, size=3))
            b = sp.Point(np.random.randint(-10, 10, size=3))
            c = sp.Point(np.random.randint(-10, 10, size=3))
            delta = sp.det(sp.Matrix([[a.x, a.y, a.z],
                                  [b.x, b.y, b.z],
                                  [c.x, c.y, c.z]]))
            if  1 <= (list(a).count(0) + list(b).count(0) + list(c).count(0)) <= 2:
              if delta in [-6,-5,-4,-3,-2,-1,1,2,3,4,5,6]:
                    break
                
        
        alpha, beta, gamma = sp.symbols('alpha beta gamma')

        answer_matrix = sp.linsolve(sp.Matrix([[a.x, a.y, a.z, alpha],
                                               [b.x, b.y, b.z, beta],
                                               [c.x, c.y, c.z, gamma]]))
        
        delta1 = sp.det(sp.Matrix([[alpha, a.y, a.z],
                                   [beta, b.y, b.z],
                                   [gamma, c.y, c.z]]))
        delta2 = sp.det(sp.Matrix([[a.x, alpha, a.z],
                                   [b.x, beta, b.z],
                                   [c.x, gamma, c.z]]))
        delta3 = sp.det(sp.Matrix([[a.x, a.y, alpha],
                                   [b.x, b.y, beta],
                                   [c.x, c.y, gamma]]))
        
        matrix = sp.Matrix([[a.x, a.y, a.z, alpha],
                            [b.x, b.y, b.z, beta],
                            [c.x, c.y, c.z, gamma]]).rref()[0]

        task_text = f'Даны $3$ некомпланарных вектора $a = ({a.x}, \\,{a.y}, \\,{a.z}), \\:' \
                    f'b = ({b.x}, \\,{b.y}, \\,{b.z}), \\:c = ({c.x}, \\,{c.y}, \\,{c.z})$. ' \
                    f'Найдите вектор $x$, удовлетворяющий системе уравнений: ' \
                    f'$$(a, \\,x) = \\alpha, \\quad (b, \\,x) = \\beta, \\quad (c, \\,x) = \\gamma$$'

        answer_text = f'\\begin{{itemize}}\n' \
                      f'\\item $\\Delta = {sp.latex(delta)}$;\n' \
                      f'\\item $\\Delta_1 = {sp.latex(delta1)}$;\n' \
                      f'\\item $\\Delta_2 = {sp.latex(delta2)}$;\n' \
                      f'\\item $\\Delta_3 = {sp.latex(delta3)}$;\n' \
                      f'\\item $A \\to ' \
                      '\\renewcommand{\\arraystretch}{2.5}\n' \
                      + sp.latex(matrix) \
                          .replace('frac', 'dfrac') \
                          .replace('\\left[\\begin{matrix}', '\\begin{pmatrix}\n') \
                          .replace('\\end{matrix}\\right]', '\n\\end{pmatrix}') \
                      + '$;\n\\renewcommand{\\arraystretch}{1}\n' \
                        '\\item $x = \n' \
                        '\\renewcommand{\\arraystretch}{2.5}\n' \
                      + sp.latex(sp.Matrix(*answer_matrix)) \
                          .replace('frac', 'dfrac') \
                          .replace('\\left[\\begin{matrix}', '\\begin{pmatrix}\n') \
                          .replace('\\end{matrix}\\right]', '\n\\end{pmatrix}') \
                      + '$\n\\renewcommand{\\arraystretch}{1}\n' \
                        '\\end{itemize}\n'

        return task_text, answer_text