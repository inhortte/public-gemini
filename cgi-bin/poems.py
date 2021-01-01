#!/usr/bin/python

from pathlib import Path
import re

print('20 text/gemini\r\n');
print('# Poems\n')

poems = Path('/home/polaris/arch-my-hive/poems')
for poem_path in poems.iterdir():
    if(re.match('^\.', poem_path.name)):
       continue
    display_name = " ".join(list(map(lambda p: p.capitalize(), re.compile('[-\s]').split(poem_path.stem))));
    print(f'=> gemini://thurk.org/cgi-bin/poem.py?{poem_path.stem} {display_name}')
