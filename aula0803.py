grafico = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7':['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

import pandas as pd

notasAlunos = {
    'João': {'matematica': 90, 'português':85, 'ciências':88},
    'Maria': {'matematica': 95, 'português':92, 'ciências':89},
    'Pedro': {'matematica': 80, 'português':75, 'ciências':82}
}

print(notasAlunos)

notasAlunos['Ana'] = {'matematica': 88, 'português':91, 'ciências':85}
print(notasAlunos)

dados = pd.DataFrame(notasAlunos)