#!/usr/bin/python

import os
import re

if('QUERY_STRING' in os.environ) and len(os.environ['QUERY_STRING']) > 0:
    try:
        poem = open(f'/home/polaris/arch-my-hive/poems/{os.environ["QUERY_STRING"]}.txt', 'r')
        print('20 text/gemini\r\n')
        flag = False
        for line in poem:
            if flag:
                print(line.capitalize(), end='')
            else:
                if re.match('^-', line):
                    flag = True
                    print
                    print("```")
                else:
                    if re.match('^\d\d\d\d-', line):
                        print(f'## {line}')
                    else:
                        print(f'# {line}')
        print("\n```")
    except FileNotFoundError:
        print('31 gemini://thurk.org/cgi-bin/poems.py\r\n')

else:
    print('31 gemini://thurk.org/cgi-bin/poems.py\r\n')
