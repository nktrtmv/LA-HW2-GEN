import numpy as np
import pylatex
from pylatex import Command
from pylatex.lists import Enumerate
from pylatex.utils import NoEscape

from settings import GROUP_COUNT, PACKAGES, MAIN_SEED, STUDENTS_COUNT

'''
import tasks HERE
All tasks must return a tuple of two strings (task, answer) in TEX format
'''

from task1.task_1 import Task1 as t1
from task2.task_2 import Task2 as t2
from task3.task_3 import Task3 as t3
from task4.task_4 import Task4 as t4
from task5.task_5 import Task5 as t5
from task6.task_6 import Task6 as t6
from task7.task_7 import Task7 as t7
from task8.task_8 import Task8 as t8
from task9.task_9 import Task9 as t9
from task10.task_10 import Task10 as t10

'''
END of import
'''


def setup_doc(doc: pylatex.document.Document):
    doc.append(NoEscape(r"\renewcommand\arraystretch{1.3}"))
    doc.append(NoEscape(r"\renewcommand\linespread{1.2}"))
    doc.append(NoEscape(r"\tolerance=500" + "\n"))
    doc.append(NoEscape(r"\unitlength=1mm" + "\n"))
    doc.append(NoEscape(r"\textwidth=16cm" + "\n"))
    doc.append(NoEscape(r"\textheight=770pt" + "\n"))
    doc.append(NoEscape(r"\oddsidemargin=-8mm" + "\n"))
    doc.append(NoEscape(r"\topmargin -32mm" + "\n"))
    doc.change_page_style("plain")
    return doc


if __name__ == "__main__":
    print("Started generation")
    np.random.seed(MAIN_SEED)
    tasks = [t1(), t2(), t3(), t4(), t5(), t6(), t7(), t8(), t9(), t10()]
    for group in range(1, GROUP_COUNT + 1):
        for variant in range(1, STUDENTS_COUNT + 1):
            geometry_options = {"tmargin": "3cm", "lmargin": "1cm"}
            main_doc = pylatex.document.Document(geometry_options=geometry_options)
            answer_doc = pylatex.document.Document(geometry_options=geometry_options)
            main_doc = setup_doc(main_doc)
            answer_doc = setup_doc(answer_doc)
            for pack in PACKAGES:
                main_doc.packages.append(pack)
                answer_doc.packages.append(pack)

            main_doc.append(NoEscape("\\textbf{Домашнее задание 2. Курс <<Алгебра>>. 2022--2023 учебный год.}"))
            main_doc.append(Command(command="newline"))
            main_doc.append(NoEscape(f"\\textbf{{БПИ-22{group}. Вариант {variant}}}"))
            main_doc.append(Command(command='bigskip'))
            main_doc.append(Command(command='bigskip'))

            answer_doc.append(NoEscape("\\textbf{Домашнее задание 2. Курс <<Алгебра>>. Ответы.}"))
            answer_doc.append(Command(command="newline"))
            answer_doc.append(NoEscape(f"\\textbf{{БПИ-22{group}. Вариант {variant}}}"))
            answer_doc.append(Command(command="newline"))

            all_tasks = []
            all_answers = []

            for task in tasks:
                task_text, task_answer = task.generate()
                all_tasks.append(task_text)
                all_answers.append(task_answer)

            with main_doc.create(Enumerate()) as enum:
                for item in all_tasks:
                    enum.add_item(NoEscape(item))

            with answer_doc.create(Enumerate()) as enum:
                for item in all_answers:
                    enum.add_item(NoEscape(item))

            main_doc.generate_pdf("tasks/{0}_var{1}".format("22" + str(group), variant),
                                  clean=True,
                                  clean_tex=True, compiler='pdflatex')
            answer_doc.generate_pdf("answers/{0}_var{1}".format("22" + str(group), variant),
                                    clean=True,
                                    clean_tex=True, compiler='pdflatex')
            print(variant, "variant ready")
        print("Group", group, "generated")
