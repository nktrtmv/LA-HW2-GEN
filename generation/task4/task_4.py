import numpy as np
import sympy as sp


class Task4:
    def __init__(self):
        pass

    def task(self):
        a = np.random.randint(-30, 30, size=2)
        b = np.random.randint(-30, 30, size=2)
        c = np.random.randint(-30, 30, size=2)
        while (a == b).all():
            a = np.random.randint(-30, 30, size=2)
            b = np.random.randint(-30, 30, size=2)
        while abs((b[0] - a[0]) * (c[1] - b[1])) == abs((c[0] - b[0]) * (b[1] - a[1])):  # A->B->C (неколлинеарные)
            c = np.random.randint(-30, 30, size=2)
        answers = [a + c - b, b + c - a, a + b - c]
        points = [a, b, c]
        latex_list = [sp.latex(point[0] + point[1] * sp.I) for point in points]
        answer_list = [sp.latex(point[0] + point[1] * sp.I) for point in answers]

        return latex_list, answer_list

    def generate(self):
        coefs4 = self.task()

        task_text = f'Даны $3$ комплексных числа: ${coefs4[0][0]}, \\:{coefs4[0][1]}, \\:{coefs4[0][2]}$. ' \
                    f'Найти число $z$, образующее параллелограмм с данными тремя на комплексной плоскости.'
        answer_text = f'Все числа $z$: ${coefs4[1][0]}, \\:{coefs4[1][1]}, \\:{coefs4[1][2]}$\n\n\\bigskip\n\n'

        return task_text, answer_text
