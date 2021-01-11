"""Ask user for their name then greet them"""

import re

from random import uniform
from tqdm import tqdm

from time import sleep

import sys

print('If you want to end, type \'!END\'.')
ans = '!END'

nam_re_spec = r'^[a-zA-Z0-9](?:\w[\ \-]{0,1})+[a-zA-Z]$'

match = False
while not match:
    usr_str = input('Enter your name:\n')
    if usr_str == ans.lower() or usr_str.upper() == ans:
        sys.exit()
    match = re.fullmatch(nam_re_spec, usr_str)
    if match:
        for _ in tqdm(range(100), desc='Processing name'):
            sleep(uniform(.005, .004))
        print(f'Hello {usr_str.title()}!')
    else:
        print('Your name must be alphabetic. Else most contain;\nExt chars inclusive: \'-\' & \' \', hyphen/dash and/'
              'or space; Must be accompanied by a letter.')

whonam = match.group(0)
