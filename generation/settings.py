from pylatex import Package

'''
Required TEX packages
'''
PACKAGES = [Package(name='babel', options='russian'),
            Package(name='latexsym'),
            Package(name='amsxtra'),
            Package(name='amscd'),
            Package(name='ifthen'),
            Package(name='amsfonts'),
            Package(name='verbatim', ),
            Package(name='amsmath'),
            Package(name='amsthm'),
            Package(name='amssymb'),
            Package(name='inputenc', options='utf8'),
            Package(name='mathptmx'),
            Package(name='fontenc', options='T1,T2A'),
            Package(name='pgf'),
            Package(name='float')
            ]

GROUP_COUNT = 10
STUDENTS_COUNT = 35
MAIN_SEED = 10002023
