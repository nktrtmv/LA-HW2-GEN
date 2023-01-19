import numpy as np
import sympy as sp
import typing as tp

angles = [sp.pi / 6, sp.pi / 3, -sp.pi / 6, -sp.pi / 3]


class Task1:
    def __init__(self):
        pass

    def task(self):
        angle = angles[np.random.randint(0, 10) % 4]
        n = np.random.randint(4, 8)
        t = np.random.randint(2, 4)
        length = np.random.randint(1, 5)
        z = length * (sp.cos(angle) + sp.sin(angle) * sp.I)

        powered_angle = sp.S(angle * t / n)
        k = np.random.randint(-5, 5)
        angle1 = angles[np.random.randint(0, 10) % 4]
        result_arg = powered_angle + sp.pi * 2 * k / n + angle1

        denominator_length = np.random.randint(1, 5)
        denominator = denominator_length * (sp.cos(angle1) + sp.sin(-angle1) * sp.I)  # меняем знак при делении

        root = f'\\sqrt[{n}]{{z^{t}}}'
        fraction = f'\\dfrac{{{root}}}{{{sp.latex(denominator)}}}'

        answer_length = sp.root(length ** t, n)

        z_pow_t_angle = sp.S(angle * t)
        step_z_pow_t1 = f'{sp.latex(sp.Pow(length, t, evaluate=False))} \\cdot ' \
                        f'\\left(\\cos\\left({sp.latex(z_pow_t_angle)}\\right) + ' \
                        f'i \\cdot\\sin\\left({sp.latex(z_pow_t_angle)}\\right)\\right)'
        step_z_pow_t2 = sp.latex(
            sp.Pow(length, t, evaluate=True) * (sp.cos(z_pow_t_angle) + sp.sin(z_pow_t_angle) * sp.I))
        step_z_pow_t3 = sp.latex(sp.Pow(length, t, evaluate=False) * sp.exp(sp.I * z_pow_t_angle))

        k_symbol = sp.symbols('k', integer=True)

        z_root_n_angle = sp.S((angle + sp.pi * 2 * k_symbol) / n)
        step_z_root_n = f'\\left\\{{' \
                        f'{sp.latex(sp.root(length, n))} \\cdot ' \
                        f'\\left(\\cos\\left({sp.latex(z_root_n_angle)}\\right) + ' \
                        f'i \\cdot\\sin\\left({sp.latex(z_root_n_angle)}\\right)\\right) \\mid k \\in [0, \\,{n})' \
                        f'\\right\\}}'

        z_pow_root_angle = sp.S((angle * t + sp.pi * 2 * k_symbol) / n)
        step_z_pow_root = f'\\left\\{{' \
                          f'{sp.latex(answer_length)} \\cdot ' \
                          f'\\left(\\cos\\left({sp.latex(z_pow_root_angle)}\\right) + ' \
                          f'i \\cdot\\sin\\left({sp.latex(z_pow_root_angle)}\\right)\\right) \\mid k \\in [0, \\,{n})' \
                          f'\\right\\}}'

        answer_angle = powered_angle + sp.pi * 2 * k / n

        result1 = f'{sp.latex(answer_length)} \\cdot ' \
                  f'\\left(\\cos\\left({sp.latex(answer_angle)}\\right) + ' \
                  f'i \\cdot\\sin\\left({sp.latex(answer_angle)}\\right)\\right)'
        result2 = sp.latex(answer_length * (sp.cos(answer_angle) + sp.sin(answer_angle) * sp.I))
        result3 = sp.latex(answer_length * sp.exp(sp.I * answer_angle))

        return [sp.latex(z), root, fraction, sp.latex(result_arg)], [t, step_z_pow_t1, step_z_pow_t2, step_z_pow_t3,
                                                                     n, step_z_root_n, step_z_pow_root,
                                                                     sp.latex(denominator), sp.latex(-angle1), k,
                                                                     result1, result2, result3]

    def generate(self):
        coefs2 = self.task()

        task_text = f'Пусть $z = {coefs2[0][0]}$. ' \
                    f'Вычислить значение ${coefs2[0][1]}$, ' \
                    f'для которого число ${coefs2[0][2]}$ имеет аргумент ${coefs2[0][3]}$.'

        answer_text = f'\\begin{{itemize}}\n' \
                      f'\\item $z^{coefs2[1][0]} = {coefs2[1][1]} = {coefs2[1][2]} = {coefs2[1][3]}$;\n' \
                      f'\\item $\\sqrt[{coefs2[1][4]}]{{z}} = {coefs2[1][5]}$;\n' \
                      f'\\item $\\sqrt[{coefs2[1][4]}]{{z^{coefs2[1][0]}}} = {coefs2[1][6]}$;\n' \
                      f'\\item $arg\\left({coefs2[1][7]}\\right) = {coefs2[1][8]}$;\n' \
                      f'\\item $k = {coefs2[1][9]}$;\n' \
                      f'\\item $\\text{{Искомое значение}} = {coefs2[1][10]} = {coefs2[1][11]} = {coefs2[1][12]}$\n' \
                      f'\\end{{itemize}}\n\n\\bigskip\n\n'

        return task_text, answer_text
