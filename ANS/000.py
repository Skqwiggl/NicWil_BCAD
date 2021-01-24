"""Ask user for their name then greet them"""

import re as r

from random import uniform as u
from tqdm import tqdm as t

from time import sleep as s

nam_re_spec = r'^[a-zA-Z](?:[a-zA-Z][\ \' \-]{0,1})+[a-zA-Z]$'

mat = False
while not mat:
    usr_str = input('Enter your name:\n')
    mat = r.fullmatch(nam_re_spec, usr_str)
    if mat:
        for _ in t(range(100), desc='Processing name'):
            s(u(.005, .004))
        print(f'Hello {usr_str.title()}!')
    else:
        print('Your name must be alphabetic. Else most contain;\nExt chars inclusive: -, \' \', \'; Must be accompanied'
              ' by a letter.')

whonam = mat.group(0)
