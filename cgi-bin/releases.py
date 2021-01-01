#!/usr/bin/python

from pathlib import Path
import re

print('20 text/gemini\r\n')
print('# Flavigula Releases')

releases = Path('/home/polaris/Elements/flavigula/release')
for album_dir in releases.iterdir():
    if re.match('^\.', album_dir.name) or (not album_dir.is_dir()):
        continue
    album_name = " ".join(list(map(lambda p: p.capitalize(), re.compile('[-\s]').split(album_dir.stem))))
    print(f'\n## {album_name}')
    if album_dir.joinpath("description").is_file():
        print(album_dir.joinpath("description").read_text())
    for zip_or_dir in album_dir.iterdir():
        if re.match(".*zip$", zip_or_dir.suffix):
            print(f'=> release/{album_dir.name}/{zip_or_dir.name} Full Album')
        if zip_or_dir.is_dir():
            for piece in zip_or_dir.iterdir():
                if re.match('.*(flac|mp3|wav|ogg)$', piece.name):
                    piece_title = piece.stem
                    m = re.match('^(.+)_session.+$', piece.stem)
                    if m:
                        piece_title = m.group(1)
                    m = re.match('^\d+[-\s]+(.+)$', piece.stem)
                    if m:
                        piece_title = m.group(1)
                    m = re.match('^(.+)-range.*$', piece_title)
                    if m:
                        piece_title = m.group(1)
                    piece_title = " ".join(list(map(lambda p: p.capitalize(), re.compile('[-\s]').split(piece_title))))
                    piece_link_name = piece.name.replace(" ", r"\ ")
                    print(f'=> gemini://thurk.org/cgi-bin/audio.py?flavigula/release/{album_dir.name}/{zip_or_dir.name}/{piece_link_name} {piece_title}')

