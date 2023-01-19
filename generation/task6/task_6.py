import numpy as np
import sympy as sp
import matplotlib
import typing as tp

matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

import matplotlib.pyplot as plt

angles = [sp.pi / 6, sp.pi / 4, sp.pi / 3, sp.pi / 2, sp.pi * 2 / 3, sp.pi * 3 / 4, sp.pi * 5 / 6]


class Task6:
    def __init__(self):
        pass

    def task(self):
        border = 7
        radius = np.random.randint(1, border - 3)
        center_line = np.random.randint(-border + 1, border, size=2)
        angle = angles[np.random.randint(0, len(angles))]
        center_circle = np.random.randint(-border + radius, border + 1 - radius, size=2)
        sp_center_line = center_line[0] + center_line[1] * sp.I
        sp_center_circle = center_circle[0] + center_circle[1] * sp.I

        task = [sp_center_circle, sp_center_line, radius, sp.latex(angle)]
        t = np.arange(-border, border, 0.01)
        plt.clf()
        if angle != sp.pi / 2:
            first_line = float(sp.tan(angle)) * (t - center_line[0]) + center_line[1]
            second_line = float(sp.tan(-angle)) * (t - center_line[0]) + center_line[1]
            plt.plot(t, first_line, color='black', linestyle='--')
            plt.plot(t, second_line, color='black', linestyle='--')
            if angle < sp.pi / 2:
                plt.fill_between(t, first_line, second_line, where=t > center_line[0],
                                 color='C0', alpha=0.3, interpolate=False)
            else:
                plt.fill_between(t, first_line, border, where=first_line >= center_line[1],
                                 color='C1', alpha=0.3, interpolate=True)
                plt.fill_between(t, second_line, -border, where=second_line < center_line[1],
                                 color='C1', alpha=0.3, interpolate=True)
                plt.axvspan(center_line[0], border, color='C1', alpha=0.3)
        else:
            plt.axvspan(center_line[0], border, color='C1', alpha=0.3)
        circle1 = plt.Circle((center_circle[0], center_circle[1]), radius, color='black', linestyle='--', alpha=0.5)
        plt.gca().add_patch(circle1)
        plt.xlim(-border, border)
        plt.ylim(-border, border)
        plt.xticks(range(-border, border + 1))
        plt.yticks(range(-border, border + 1))
        plt.savefig('answers/graph.pgf')

        answer = f'1) Область внутри окружности с центром в точке $({center_circle[0]}; \\,{center_circle[1]})$ ' \
                 f'радиуса {radius}\\newline' \
                 f'2) Область, ограниченная двумя прямыми, пересекающимися в точке ' \
                 f'$({center_line[0]}; \\,{center_line[1]})$ под углом $= \\pm {sp.latex(angle)}$'

        return task, answer

    def generate(self):
        coefs6 = self.task()

        z = sp.symbols('z')
        task_text = 'На комплексной плоскости нарисуйте область, заданную системой $(arg(z) \\in (-\\pi,\\,\\pi])$:' + \
                    f'$$\\begin{{cases}}' \
                    f'|{sp.latex(z - coefs6[0][0])}| < {coefs6[0][2]} \\\\' \
                    f'|arg({sp.latex(z - coefs6[0][1])})| < {coefs6[0][3]} \\\\ ' \
                    f'\\end{{cases}}$$'
        answer_text = f'{coefs6[1]}\n' \
                      '\\begin{figure}[H]\n' \
                      '\\begin{center}\n' \
                      '\\input{graph.pgf}\n' \
                      '\\end{center}\n' \
                      '\\end{figure}\n\n\\bigskip\n\n'

        return task_text, answer_text
