#!/usr/bin/python

from pymongo import MongoClient
import urllib.parse
import pymongo
from datetime import date
import os
import re

# if ('QUERY_STRING' in os.environ) and len(re.findall("\?", os.environ['PATH_INFO'])) > 0:
if ('QUERY_STRING' in os.environ) and len(os.environ['QUERY_STRING']) > 0:
    client = MongoClient()
    martenblog = client['martenblog']
    # full_query = os.environ['QUERY_STRING'].split("?").pop();
    # query = urllib.parse.unquote(full_query)
    query = urllib.parse.unquote(os.environ['QUERY_STRING'])
    # query = full_query.split("=").pop();

    entries = martenblog.entry.find({ 'entry': re.compile(query, re.IGNORECASE) }).sort('created_at', pymongo.DESCENDING).limit(23)

    header = "20 text/gemini\r\n"
    print(header)

    print(f'# Search results for "{query}"\n\n', end='')

    for entry in entries:
        d = date.fromtimestamp(entry["created_at"] / 1000)
        fecha = "{:04}-{:02}-{:02}".format(d.year, d.month, d.day)
        print(f'=> gemini://thurk.org/blog/{int(entry["_id"])}.gmi {entry["subject"]} ( {fecha} )\n', end='')
else:
    print("10 For what do you search?\r\n")
