import numpy as np
import sympy as sp

ns = [3, 4, 6, 12]
alphas = [[0, sp.pi / 2, sp.pi], [0, sp.pi * 2 / 3, sp.pi, sp.pi * 4 / 3],
          [0, sp.pi, sp.pi * 3 / 2], [0]]


class Task5:
    def __init__(self):
        pass

    def task(self):
        choice = np.random.randint(0, 4)
        n, k = ns[choice], np.random.randint(0, ns[choice] - 1)
        alpha_z = alphas[choice][np.random.randint(0, len(alphas[choice]))]
        length = np.random.randint(1, 5)

        angle = 2 * sp.pi / n
        angle1 = (alpha_z + 2 * sp.pi * k) / n
        angle2 = (alpha_z + 2 * sp.pi * (k + 1)) / n

        z1 = length * (sp.cos(angle1) + sp.sin(angle1) * sp.I)
        z2 = length * (sp.cos(angle2) + sp.sin(angle2) * sp.I)

        z1_trig = f'{length} \\cdot ' \
                  f'\\left(\\cos\\left({sp.latex(angle1)}\\right) + ' \
                  f'i \\cdot\\sin\\left({sp.latex(angle1)}\\right)\\right)'

        z2_trig = f'{length} \\cdot ' \
                  f'\\left(\\cos\\left({sp.latex(angle2)}\\right) + ' \
                  f'i \\cdot\\sin\\left({sp.latex(angle2)}\\right)\\right)'

        result1 = sp.latex((length ** n) * (sp.cos(alpha_z) + sp.sin(alpha_z) * sp.I))
        result2 = f'{sp.latex(sp.Pow(length, n, evaluate=False))} \\cdot ' \
                  f'\\left(\\cos\\left({sp.latex(alpha_z)}\\right) + ' \
                  f'i \\cdot\\sin\\left({sp.latex(alpha_z)}\\right)\\right)'
        result3 = sp.latex(sp.Pow(length, n, evaluate=False) * sp.exp(sp.I * alpha_z))

        return [sp.latex(z1), sp.latex(z2)], [z1_trig, z2_trig, sp.latex(angle), n, result1, result2, result3]

    def generate(self):
        coefs5 = self.task()

        task_text = f'Даны числа $z_1 = {coefs5[0][0]}, \\:z_2 = {coefs5[0][1]}$ – ' \
                    f'соседние комплексные корни степени $n$ числа $z$. ' \
                    f'Найти степень $n$ и исходное число.'

        answer_text = f'\\begin{{itemize}}\n' \
                      f'\\item $z_1 = {coefs5[1][0]}$;\n' \
                      f'\\item $z_2 = {coefs5[1][1]}$;\n' \
                      f'\\item $\\text{{угол между радиус-векторами}} = {coefs5[1][2]}$;\n' \
                      f'\\item $n = {coefs5[1][3]}$;\n' \
                      f'\\item $z = {coefs5[1][4]} = {coefs5[1][5]} = {coefs5[1][6]}$\n\n\\bigskip\n\n' \
                      f'\\end{{itemize}}\n\n\\bigskip\n\n'

        return task_text, answer_text
