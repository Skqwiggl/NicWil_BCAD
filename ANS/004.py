"""Ask the user's name & age, then display their forthcoming age."""

import re as r

from random import uniform as u
from tqdm import tqdm as t

from time import sleep as s

nam_re_spec = r'^[a-zA-Z](?:[a-zA-Z][\ \' \-]{0,1})+[a-zA-Z]$'

while True:
    usr_str = input('Enter your name:\n')
    mat = r.fullmatch(nam_re_spec, usr_str)
    if mat:
        break
    else:
        print('Your name must be alphabetic. Else most contain;\nExt chars inclusive: -, \' \', \'; Must be accompanied'
              ' by a letter.')

whonam = mat.group(0)

ag_re_spec = r'^[0-9]{1,3}$'

mat_2 = False
while not mat_2:
    try:
        ag_inp = -1
        ag_num = f'How old are you, {usr_str.title()}?\n'
        while not 6 <= ag_inp <= 122:
            ag_inp = int(input(ag_num))
            if not 6 <= ag_inp <= 122:
                print(f'You cannot be {ag_inp}.')
        mat_2 = r.fullmatch(ag_re_spec, str(ag_inp))
        if mat_2:
            for _ in t(range(100), desc='Calculating Age'):
                s(u(.005, .004))
            new_ag = int(ag_inp) + 1
            print(f'{usr_str.title()} you\'ll be {new_ag} next year!')

    except ValueError:
        print('You may only enter ints.')

ag = mat.group(0)
