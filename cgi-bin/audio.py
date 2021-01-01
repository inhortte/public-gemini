#!/usr/bin/python

from pathlib import Path
import re
import os
import sys

if ('QUERY_STRING' in os.environ) and len(os.environ['QUERY_STRING']) > 0:
    try:
        p = open(f'/home/polaris/Elements/{os.environ["QUERY_STRING"]}', 'rb')
        print('20 audio/flac\r\n')
        with os.fdopen(sys.stdout.fileno(), "wb", closefd=False) as stdout:
            b = p.read(4096)
            while b:
                stdout.write(b)
                b = p.read(4096)
            stdout.flush()
    except Exception as e:
        print('31 gemini://thurk.org/cgi-bin/releases.py')                
